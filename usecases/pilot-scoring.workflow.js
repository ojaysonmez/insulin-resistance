// DRAFT (2026-10-19): scoring pilot for the use-case rubric. NOT RUN. Review before running.
// Run it with the Workflow tool: {scriptPath: "usecases/pilot-scoring.workflow.js"}, optional args:
//   {rows: [6, 5, 13], maxSearchesPerRow: 6, outDir: "usecases/pilot"}
// Design follows usecases/scoring-rubric.md (Process, steps 2 and 3): one agent scores a set of dimensions
// for ALL pilot rows, so scores are comparable; the endocrinologist and the PCP score the same dimensions
// independently; one skeptic reviews all score files afterwards. Six agents in total.

export const meta = {
  name: 'usecase-scoring-pilot',
  description: 'Score use-case rows 6, 5 and 13 on the rubric with five independent role agents, then one skeptic review',
  phases: [
    { title: 'Score', detail: 'five role agents, each scoring its dimensions for every pilot row, independently' },
    { title: 'Review', detail: 'one skeptic reviews all score files and the rubric anchors' },
  ],
}

const ROWS = (args && args.rows) || [6, 5, 13]
const MAX_SEARCHES = (args && args.maxSearchesPerRow) || 6
const OUT = (args && args.outDir) || 'usecases/pilot'

const SCORE_SCHEMA = {
  type: 'object',
  properties: {
    report_file: { type: 'string' },
    scores: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          row: { type: 'integer' },
          dimension: { type: 'string', enum: ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'S'] },
          score: { type: ['integer', 'null'] },
          reason: { type: 'string' },
          sources: { type: 'array', items: { type: 'string' } },
          confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
          origin: { type: 'string', enum: ['project files', 'new search', 'both'] },
          estimate: { type: 'string' },
        },
        required: ['row', 'dimension', 'score', 'reason', 'sources', 'confidence', 'origin'],
      },
    },
    anchor_issues: { type: 'array', items: { type: 'string' } },
    assumptions: { type: 'array', items: { type: 'string' } },
    searches: { type: 'array', items: { type: 'string' } },
  },
  required: ['report_file', 'scores', 'anchor_issues', 'assumptions'],
}

const REVIEW_SCHEMA = {
  type: 'object',
  properties: {
    report_file: { type: 'string' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          row: { type: ['integer', 'null'] },
          dimension: { type: 'string' },
          problem: { type: 'string' },
          severity: { type: 'string', enum: ['must fix', 'should fix', 'note'] },
          suggested_change: { type: 'string' },
        },
        required: ['dimension', 'problem', 'severity'],
      },
    },
    anchor_rewrites: { type: 'array', items: { type: 'string' } },
    verdict: { type: 'string' },
  },
  required: ['report_file', 'findings', 'anchor_rewrites', 'verdict'],
}

const COMMON = [
  'You are scoring use cases of insulin or C-peptide measurement for a pilot of the rubric in usecases/scoring-rubric.md.',
  'Read usecases/scoring-rubric.md (dimensions, anchors, rules) and the rows ' + ROWS.join(', ') + ' of usecases-verified.md (first column is the row number).',
  'Score ONLY your assigned dimensions, for EVERY pilot row. Score the use of the measurement in that clinical situation, not the disease.',
  'Every score needs: the number, one or two sentences of reasoning, sources (PMID with DOI and the read level; guideline name and year; or file and section), a confidence, and whether it came from the project files or a new search. If the sources cannot support a score, set score to null and say why; do not guess.',
  'Do not infer a score from the status column in usecases-verified.md. Name the measure type the evidence used (fasting-based, post-load or mixed-meal, non-insulin surrogate, C-peptide).',
  'Coverage and reimbursement are out of scope. Commonality is United States only.',
  'Independence: do not read any other file under ' + OUT + '/ and do not read reviews/ files about the pilot. Work only from the rubric, the use-case file and your own searches.',
  'Searching: at most ' + MAX_SEARCHES + ' searches per row. Log every search string and the number of records screened in your report. State negatives as "not found in the screened records".',
  'Record in anchor_issues every place where a rubric anchor was ambiguous or did not fit, with the row and what you chose. Record assumptions in assumptions.',
  'Write your report to the file named below (create the folder if needed). Do not edit usecases-verified.md, merged-conclusion.md, the rubric or any other existing file. Do not commit.',
  'This is an unattended run: never stop to ask a question. Record assumptions and failures in the report and continue. Return the structured result; report_file is the path you wrote.',
].join('\n')

const SCORERS = [
  {
    key: 'searcher',
    agentType: 'ir-evidence-searcher',
    dims: 'D7 (United States patients per year; give the number, its source, a range, and mark a range wider than one bin as low confidence) and D3 (guideline or regulatory status, from guideline full text where possible)',
  },
  {
    key: 'biostatistician',
    agentType: 'ir-biostatistician',
    dims: 'D2 (evidence that the result changes decisions or outcomes, not mere association) and D8 (added value over alternatives such as clinical features, HbA1c, glucose, other tests)',
  },
  {
    key: 'clinical-chemist',
    agentType: 'ir-clinical-chemist',
    dims: 'D4 (analytical feasibility: assay, sample, protocol, standardization)',
  },
  {
    key: 'endocrinologist',
    agentType: 'ir-endocrinologist',
    dims: 'D1 (decision change), D5 (workflow fit), D6 (safety and burden, higher = safer) and S (stakes: harm if the right decision is not made)',
  },
  {
    key: 'pcp',
    agentType: 'ir-pcp',
    dims: 'D1 (decision change), D5 (workflow fit), D6 (safety and burden, higher = safer) and S (stakes). Another role scores the same dimensions independently; give your own reading as a primary care physician',
  },
]

phase('Score')
const scored = await parallel(SCORERS.map(s => () =>
  agent(
    COMMON + '\n\nYour assigned dimensions: ' + s.dims + '.\nReport file: ' + OUT + '/' + s.key + '-scores.md',
    { label: 'score:' + s.key, phase: 'Score', agentType: s.agentType, schema: SCORE_SCHEMA }
  )
))
const ok = scored.filter(Boolean)
const failed = SCORERS.length - ok.length
if (failed) log(failed + ' of ' + SCORERS.length + ' scorers returned nothing; the review covers the rest')

phase('Review')
const files = ok.map(r => r.report_file).filter(Boolean)
const review = await agent(
  [
    'Review the pilot scores for use-case rows ' + ROWS.join(', ') + ' against usecases/scoring-rubric.md and usecases-verified.md.',
    'Score files to review: ' + files.join(', ') + '.',
    'Check: (1) each score is justified by its cited source and fits its anchor; (2) PMID and DOI are both recorded with a read level; (3) the measure type behind each claim is named; (4) the D7 numbers have a US source and a range; (5) the endocrinologist and the PCP scores for D1, D5, D6 and S, and any difference of more than one point between roles on the same dimension; (6) which anchors were ambiguous (collect the anchor_issues from all files) and a proposed rewrite for each; (7) whether a score was inferred from the status column instead of from sources.',
    'Do not search for new evidence unless a cited source cannot be checked from the files. Write your review to ' + OUT + '/skeptic-review.md. Do not edit any score file, the rubric or the deliverables. Never stop to ask a question; record assumptions and continue.',
  ].join('\n'),
  { label: 'review:skeptic', phase: 'Review', agentType: 'ir-skeptic', schema: REVIEW_SCHEMA }
)

// Plain-code summary: scores by row and dimension, and disagreements of more than one point between roles.
const byKey = {}
ok.forEach(r => {
  (r.scores || []).forEach(sc => {
    const k = sc.row + '|' + sc.dimension
    ;(byKey[k] = byKey[k] || []).push(sc.score)
  })
})
const table = Object.keys(byKey).sort().map(k => {
  const vals = byKey[k].filter(v => v !== null && v !== undefined)
  const spread = vals.length > 1 ? Math.max(...vals) - Math.min(...vals) : 0
  return { key: k, scores: byKey[k], spread: spread, flag: spread > 1 ? 'DISAGREE' : '' }
})

return {
  rows: ROWS,
  report_files: files,
  scorers_failed: failed,
  table: table,
  disagreements: table.filter(t => t.flag),
  anchor_issues: ok.flatMap(r => r.anchor_issues || []),
  skeptic: review,
}
