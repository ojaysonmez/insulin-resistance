# RS-D1S: proposed D1 and S changes (proposal only; no score changed)

Sources read: usecases/scoring-rubric.md (D1 and S anchors, clarifications 11, 12, 15, 18, 26 to 29), DECISIONS.md D-37 to D-39, usecases/scoring/V*.json, U*.json and ranking.json (files only; no analyst reports in analysis/). Current values are the means in ranking.json.

| Row | Dim | Current | Proposed | Default action | Confidence |
|---|---|---|---|---|---|
| 8 | D1 | 1 | 1 | No patient decision; trial-level endpoint (stimulated C-peptide, MMTT AUC). | medium |
| 28 | D1 | 1 | 1 | Classify from clinical features and antibodies; read C-peptide uncorrected in CKD. | medium |
| 46 | D1 | 2.5 | 3 | Insulin and DKA treatment (same with or without the result). | medium |
| 6 | S | 2.5 | 2 | Insulin-treated patient of unclear type stays on insulin. | low |
| 13 | S | 2.5 | 1 | Pioglitazone given on the other guideline trigger (stroke or TIA with prediabetes) without a HOMA-IR value, or at clinician judgement. | low |
| 31 | S | 1.5 | 1 | Continue insulin in an adult of doubtful diabetes type. | low |
| 32 | S | 1.5 | 1 | Continue insulin until evaluated, after DKA in a person with suspected ketosis-prone diabetes. | low |

## Reasons

- **Row 8 D1** (1 to 1): Clarification 29: D1 is 1 at most for a research endpoint and no individual patient decision is named. Both scorers (V23, V24) gave 1; V23 noted 0 as an alternative, but counselling about residual function keeps 1. Unchanged. Measure type: C-peptide, post-meal stimulated.

- **Row 28 D1** (1 to 1): Interpretation limit (kidney clearance raises C-peptide); no validated eGFR correction and no accepted action depends on an adjusted value, so no individual decision is named (clarification 29). Both scorers (V17, V18) gave 1. Unchanged. Measure type: C-peptide, glucose/C-peptide ratio, UCPCR.

- **Row 46 D1** (2.5 to 3): Current 2.5 is the mean of V17 (3) and V18 (2). Clarification 28 and D-38: low C-peptide is criterion 3 of 3 in the Japan Diabetes Society fulminant T1D criteria, a national diagnostic criterion elsewhere, so D1 is 3, the same reading as row 47. The US reading (no guideline uses it; treatment unchanged) belongs in D3, D7 and S, not D1. Measure type: C-peptide (urinary or serum, stimulated).

- **Row 6 S** (2.5 to 2): Current 2.5 is the mean of U4 (2) and U5 (3). Under clarifications 18 and 26 the harm is that of the default without the result: unnecessary insulin (hypoglycaemia, burden) or a missed MODY or non-insulin option, moderate and delayed. DKA arises from a wrong result or a wrong withdrawal, not from absent information, so it is not the marginal harm. Moves rank-relevant S from 0.625 to 0.5 on the 0-1 scale.

- **Row 13 S** (2.5 to 1): Current 2.5 is the mean of U4 (2) and U5 (3), and U5 scored recurrent-stroke severity, which clarification 18 forbids. Both scorers noted that clinicians can treat without HOMA-IR, and no source read shows benefit differs by HOMA-IR stratum. Marginal harm is treating a low-IR patient who gains less (oedema, weight, fracture risk) or leaving out a patient who would benefit if the default is not to treat; symptomatic or reversible, 1. If the default were withholding pioglitazone, S would be 2; recorded as the alternative.

- **Row 31 S** (1.5 to 1): Current 1.5 is the mean of V4 (1) and V5 (2). The default (continue insulin) is not itself dangerous; the marginal harm is unnecessary insulin with injection burden and hypoglycaemia, symptomatic and reversible. Withdrawal-related DKA belongs to a different default and is not scored. Alternative 2 if hypoglycaemia in older patients is weighted as moderate.

- **Row 32 S** (1.5 to 1): Current 1.5 is the mean of V4 (1) and V5 (2). Same default and same harm as row 31: unnecessary lifelong insulin in patients with preserved function, reversible. DKA recurrence (3) applies only if empirical withdrawal were the default; not scored. Consistent with row 31.

## Notes
- Unchanged: rows 8 and 28 D1 (1), row 47 D1 (3, D-38). Row 46 D1 raised to 3 to match row 47.
- S changes lower rows 6, 13, 31 and 32 by 0.5 to 1.5 points (0.125 to 0.375 on the 0-1 scale, 0.025 to 0.075 composite at weight 0.20); row 13 falls most. Ranking effects are not computed here.
- All S proposals are low confidence: each rests on a named default that the analysts did not test against data.
