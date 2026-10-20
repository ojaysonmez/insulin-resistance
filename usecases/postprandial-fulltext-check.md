# Full-text check of draft rows D1, D2, D4, D5

Scope: `usecases/postprandial-additions-draft.md`, rows D1, D2, D4, D5 only. Not merged, not skeptic-reviewed. Quotes are verbatim output of `tools/pmc_text.py`. The helper shows at most 6-10 matches per call and repeats overlapping windows, so "N matches" below means the helper's reported total, and only the shown ones were read. DOIs are copied from the draft and were not re-verified here.

Measure types: D1 post-load (OGTT) and post-meal (MMTT) glucose with insulin; D2 post-load OGTT C-peptide (and insulin for the model); D4 post-load OGTT insulin and C-peptide; D5 stimulated C-peptide (MMTT, glucagon).

## Sources that could not be read or were wrong
- PMC5444099 (Insel 2015 staging statement): the PMCID resolves to a different article ("Challenges in Enforcing Home Smoking Rules in a Low-Income Population"). Pattern "stage|C-peptide|OGTT|metabolic": 0 matches. The staging statement was NOT read. The PMCID in the task or candidates file is wrong; I did not guess another one.
- Cryer 2009 Endocrine Society guideline (PMID 19088155, https://doi.org/10.1210/jc.2008-1410): one web fetch attempt returned only a cross-host redirect notice (to academic.oup.com/jcem/article/94/3/709/2596247). No guideline text, not even an abstract, was seen. Not retried, per instruction. Guideline text for D1: not read.
- PMC11564166 (post-bariatric review): only 2 helper calls; 106 and 24 matches reported, 8 and 8 shown. Not exhaustively read.
- PMC12690183 (ADA Standards 2026 section 2): web-page source; 156 matches for the first pattern, 10 shown; second pattern 6 of 6 shown. Not exhaustively read, so absence statements below are limited to the shown matches.

## D1 reactive hypoglycaemia, MMTT / OGTT with insulin

Verbatim passages
- PMC8067537, 1. Introduction: "The main drawback in RH diagnostic process is lack of standardized biochemical test and lack of glucose cut off value, which should be implemented."
- PMC8067537, 1. Introduction: "...the definition of MMTT remains unclear; there are no specific guidelines according to meal composition and measurement that should be conducted during postprandial period. It should be highlighted that there is no gold standard for duration of these tests (neither OGGT nor MMTT) and subsequent interpretation of glucose and insulin values according to RH."
- PMC8067537, 1. Introduction: "...diagnosis requires exclusion of other conditions that may have impact on hypoglycemic episodes (e.g., previous gastrointestinal surgery, peptic ulcer disease, hormonal disorders, and alcoholism)."
- PMC8067537, 2.2: "The cut off glucose value for hypoglycemia during OGTT was set on <=55 mg/dL [18]." and "RH was confirmed if the patient manifested hypoglycemic symptoms and had glucose level <=55 mg/dL during OGTT." (source text uses the "less than or equal" symbol).
- PMC8067537, 3.5: "Hypoglycemia has been found in twelve (30%) subjects from SG. Those patients have also manifested hypoglycemic symptoms during OGTT..."; "Ten (25%) patients from SG had pseudohypoglycemic symptoms but without glucose decline during the test".
- PMC12986748, 1. Introduction: "First, there is no consensus definition of RH and there is a lack of gold standard diagnostic criteria."
- PMC12986748, 2.6: "we defined reactive hypoglycemia using the following criteria. Participants were classified as exhibiting RH if either of the following conditions was met: (1) the post-peak rate of glucose decline was <=-1.2 mg/dL per minute, and the early nadir ... was at least 5 mg/dL below the participant's fasting (baseline) glucose concentration;" (second condition not printed).
- PMC12986748, 2.6: "In our cohort of otherwise healthy adults with obesity, the median rate of decline was -1.2 mg/dL/min."
- PMC12986748, 4. Discussion: "individuals with RH have greater sensitivity to insulin and greater insulin secretion per degree of insulin sensitivity" and "RH may not just be a pathological state but may represent a distinct metabolic phenotype associated with high insulin sensitivity."
- PMC11564166, Diagnosis > Blood glucose testing: "Standard tests in actual practice include the oral glucose tolerance test (OGTT), the mixed meal tolerance test (MMTT) (63), and continuous glucose monitoring (CGM)". Also: "The OGTT is commonly used to diagnose hypoglycemia." (sentence continues about over-diagnosis; cut off in the print).

Support check
- Supported: 30% had symptoms with glucose <=55 mg/dL (12 of 40, SG group); criteria non-standardised; non-surgical case (surgery is an exclusion in the quoted text).
- Qualified: the <=55 mg/dL cut-off is the authors' own choice (citing ref 18), not a guideline threshold. Draft wording "criteria are non-standardized" is fine but should say who set the cut-off.
- Qualified: 41829992 defines RH by a rate of glucose decline and early nadir (a study-specific curve definition), derived from the cohort's own median (-1.2 mg/dL/min). It is a research definition. It also used IVGTT, and the population is "healthy adults with obesity". The 69 and 19 counts in the draft were not seen in the shown matches (not checked, not contradicted).
- Insulin role: in 41829992 insulin is used to characterise RH (higher insulin sensitivity and disposition index), not to diagnose it. Not found in the screened full texts (PMC8067537 pattern "55 mg|30%|standardi|Whipple", 9 matches; PMC12986748 patterns above, 127 and 19 matches): an insulin or C-peptide threshold for diagnosing reactive hypoglycaemia.
- Guideline: not read (Cryer 2009 inaccessible). No passage from a guideline, consensus or regulatory text recommends insulin measurement during an OGTT/MMTT for this decision.

Proposed status: research-only (unchanged).
Proposed wording: "Adults without diabetes or gastric surgery with suspected reactive hypoglycaemia: OGTT or MMTT with glucose (insulin optional) to document low glucose with symptoms (Whipple triad). No standard test, meal or glucose cut-off exists in the two full texts read (authors' words); the 55 mg/dL OGTT cut-off in PMC8067537 is study-specific. Insulin values describe the phenotype and did not set a diagnosis. Guideline text (Cryer 2009) not read."

## D2 type 1 diabetes stage 1/2 progression, OGTT C-peptide

Verbatim passages
- PMC12690183 (ADA 2026 s2), Type 1 Diabetes > Recommendations: "2.6 Screen for presymptomatic type 1 diabetes by testing autoantibodies against insulin (IA), glutamic acid decarboxylase (GAD), islet antigen 2 (IA-2), or zinc transporter 8 (ZnT8). B" and "2.7 Autoantibody-based screening for presymptomatic type 1 diabetes should be offered to those with a family history of type 1 diabetes or otherwise known elevated genetic risk. B"
- PMC12690183, Table 2.4 header: "Autoimmunity Normoglycemia Presymptomatic | Autoimmunity Dysglycemia Presymptomatic | Autoimmunity Overt hyperglycemia Symptomatic"
- PMC9643141 (Index60), Abstract: "Median Index60 values of DPT-1 (1.44) and TNPTP (1.05) progressors to T1D 1.5 years prediagnosis ... were used as thresholds to identify individuals at high risk for T1D in the full cohort at baseline (5-year risk of 0.75-0.88 for those above thresholds)."
- PMC9643141, Abstract: "AUC C-peptide ... decreased from 1.5 to 0.5 years prediagnosis (DPT-1, P = 0.017; TNPTP, P = 0.093)."
- PMC9643141, Conclusions: "A transition from an increase to a decrease in AUC C-peptide ~1.5 years prediagnosis was validated in two independent cohorts. The median Index60 value at that time point can be used as a pathophysiologic-based threshold for identifying individuals at high risk for T1D."
- PMC9643141, Results: "These median values were then used as risk thresholds for T1D at the baseline OGTTs of the full TNPTP (n = 6,567) and DPT-1 (n = 711) cohorts"; "To achieve independence, we removed the baseline values of the 82 TNPTP progressors fro..." (cut off in print).
- PMC12527456 (oral minimal model), front: "C-peptide during dynamic tests such as the OGTT or the mixed-meal tolerance test (MMTT) has been accepted as a surrogate endpoint to quantify residual beta cell function in Stage 3 - clinical - diabetes (7), but it has shown low predictive values for disease progression in preclinical T1D when compared with measures that include both glucose and C-peptide (8)."
- PMC12527456, Selection: "The final selection included n = 30 Stage 1 and n = 27 Stage 2 individuals."
- PMC12527456, Risk Determinants: "φ total was the only one significantly associated with the risk of progression. Specifically, each 10-unit increase in φ total was linked to an 8-fold reduction in the odds of disease progression (OR 0.92 [0.86, 0.98], P = .016)... Other variables, including age, BMI, sex, AUC C-peptide, OMM-derived insulin sensitivity, and stage, did not show significant associations with progression risk."
- PMC12527456, Discussion: "...we likely included only those with a more advanced disease progression, thus limiting the generalizability of our findings."

Support check
- Supported: Index60 medians 1.44 and 1.05; 5-year risk 0.75-0.88; AUC C-peptide rises then falls about 1.5 years before diagnosis; n = 72 and 82.
- Qualified (draft caveat about circularity): the thresholds come from progressors' medians, but they were applied to the full cohorts after removing the progressors' baseline values "to achieve independence". "Validated in two independent cohorts" refers to the inflection point, not to a prospective test of the threshold in a new population. Still no external clinical validation seen. Pattern "Index60|validation|threshold|external" in PMC9643141: 35 matches, 10 shown.
- Qualified: the fall from 1.5 to 0.5 years was not significant in TNPTP (P = 0.093).
- Qualified/contradicting for the model row text: in PMC12527456 AUC C-peptide was not associated with progression; only φ total was (OR 0.92, 0.86-0.98). The sentence "8-fold reduction" with OR 0.92 is the authors' wording and looks internally inconsistent per 10 units; I did not recompute it. The sample is small (30 + 27) and the authors state limited generalisability. Draft claim "separated stage 2 from stage 1 where standard indices did not" was not seen in the shown matches.
- Guideline/consensus: ADA 2026 recommends autoantibody screening (2.6, 2.7), not OGTT C-peptide indices for risk prediction. Pattern "stage 1 type 1|stage 2 type 1|presymptomatic|autoantibod.{0,40}screen": 6 matches, 6 shown, none recommends OGTT C-peptide or Index60. First pattern (156 matches, 10 shown) showed only the OGTT glucose diagnostic criteria for diabetes. The Insel 2015 statement was not read (wrong PMCID).

Proposed status: limited (unchanged); not established.
Proposed wording: "Autoantibody-positive relatives (stage 1/2): OGTT with C-peptide (Index60, AUC C-peptide) or oral-minimal-model beta-cell metrics for progression risk. Evidence: cohort studies (DPT-1, TrialNet). ADA Standards 2026 recommend autoantibody screening but, in the passages read, do not recommend these C-peptide indices. Thresholds are cohort-derived medians; small model study (n = 57)."

## D4 OGTT before distal pancreatectomy

Verbatim passages
- PMC10876401, Participants: "Based on the exclusion criteria shown in Fig. 1, 56 patients were included in the study."
- PMC10876401, Results: "In total, 33 patients developed diabetes during the 36-month follow-up. The cumulative incidence rates of new-onset diabetes after DP were 30.4% at 1 month, 52.7% at 6 months, 61.1% at 12 months, ... and 74.1% at 36 months"
- PMC10876401, Results: "The presence of IGT before surgery (HR 2.650, 95% CI 1.216-5.772, P < .05) was detected as a significant factor in Model 1, and the AUCs for glucose in the 75-g OGTT up to 180 minutes (HR 1.002, 95% CI 1.001-1.004, P < .05) in Model 3"
- PMC10876401, Results: "the incidence was significantly higher (P < .05) in IGT, at 86.9% at 36 months postoperatively"
- PMC10876401, Results: "the insulinogenic index and adaptation indices were significantly lower at 1 month postoperatively (insulinogenic index: 15.2 +/- 1.8 vs 9.1 +/- 0.9 mIU/mmol, P < .01..."
- PMC10876401, Results: "Furthermore, when analyzing the incidence rate for each diagnostic index, it appears that 2 hours after the 75-g OGTT, HbA1c, and FBG play more significant roles in the development of new diabetes, in that order."
- PMC13178281, Methods: "a subgroup of 37 patients (CP; n = 12; DP; n = 25) underwent endocrine function testing using an OGTT before and 1 month after surgery, including measurement of blood glucose (BG), immunoreactive insulin (IRI), and C-peptide immunoreactivity (CPR) levels."
- PMC13178281, Introduction: "we retrospectively compared the short- and long-term outcomes of CP and DP"
- PMC13178281, Results: "In the CP group, no significant differences were observed between the preoperative and postoperative AUC values for BG (p = 0.351), IRI (p = 0.723), or CPR (p = 0.900)... In contrast, the DP group showed a significant postoperative increase in BG AUC (p < 0.001) and significant decreases in IRI AUC (p = 0..." (cut off).
- PMC13178281, Discussion: "In our cohort, the incidence was even higher (50.9%)" (DP new-onset diabetes) and "33 patients (74.1%) developed new-onset DM [20]".

Support check
- Supported: 56 patients, 33 with diabetes, 74.1% at 36 months; 37 patients with OGTT, DP versus CP AUC changes; 50.9% for DP.
- Contradicts or qualifies the draft: the draft says a "lower insulinogenic index at 1 month" predicted diabetes. In the shown text, the preoperative predictors named are glucose-based (IGT, HR 2.650; glucose AUC, HR 1.002). The insulinogenic index fall (15.2 to 9.1) is shown as a group change after surgery; I did not see a statement that it predicted diabetes (pattern "insulinogenic|predict|hazard|cutoff|threshold", 37 matches, 10 shown; second call "cutoff value|HR |74\.1|56 patients|impaired glucose tolerance at 1", 20 matches, 8 shown). Treat the insulin-based prediction claim as unverified.
- Qualified: the 2-h OGTT glucose, HbA1c and FBG were named as stronger indicators than insulin measures in the shown sentence. So the glucose part of the OGTT carries the preoperative prediction; insulin and C-peptide mostly describe postoperative loss.
- Not seen (not contradicted): the 14.8% figure for central pancreatectomy; the pattern "50\.9|14\.8|AUC|insulin" had 33 matches, 8 shown. 42146813 is described by its authors as retrospective in design with a prospective cohort source (KIP-MEP), single centre. ROC cutoffs were computed in 37889837 but the numeric values were not printed in the shown matches: no threshold quoted.
- Guideline: none in these sources. Pattern search found no recommendation text.

Proposed status: limited (unchanged), with narrower wording.
Proposed wording: "Adults without diabetes scheduled for distal pancreatectomy: 75 g OGTT before surgery. Preoperative impaired glucose tolerance (glucose-based) predicted new diabetes (HR 2.650; 86.9% at 36 months); insulin and C-peptide AUCs fell after distal but not central pancreatectomy. An insulin-based preoperative prediction was not confirmed in the full text read. Single-centre Japanese cohorts (n = 56, n = 37); no validated cut-off."

## D5 stimulated C-peptide in LADA

Verbatim passages
- PMC4297398, Background: "limited data are available regarding fasting or stimulated C-peptide secretion in LADA [2-8]. Stimulated C-peptide is currently accepted as the reference outcome for assessing beta-cell secretory response in trials studying the prevention of beta-cell loss in established autoimmune diabetes [9]."
- PMC4297398, Background: "no studies have assessed the insulin secretory response using the standardised mixed-meal tolerance test (MMTT) in patients with LADA."
- PMC4297398, Methods: "C-peptide was measured by a chemiluminescence assay (Immulite 2000...), with reference values of 0.30 - 2.4 nmol/l"
- PMC4297398, Results Table 1: "AUC C-peptide, nmol/l 41.3 (46.4) [T1D] 275.5 (121.2) [T2D] 140.8 (102.2) [LADA]" (column order from the table header "Type 1 diabetes, Type 2 diabetes, LADA"); "Insulin treatment, n (%) 33 (100%) 8 (26.7%) 20 (62.5%)".
- PMC12940418, Introduction: "When this study was initiated, LADA was commonly classified as an intermediate form of diabetes; current consensus now recognizes it as a slowly progressive autoimmune variant of T1DM [16,17]. Accordingly, LADA was initially analyzed within the autoimmune diabetes group and subsequently examined as a separate subgroup"
- PMC12940418, 2.1: "fasting C-peptide concentration (2.64 ng/mL vs. 0.87 ng/mL, p < 0.001), C-peptide concentration 6 min after glucagon administration (4.6 ng/mL vs. 1.35 ng/mL, p < 0.001)" (T2DM versus T1DM group; LADA included in the T1DM group).
- PMC12940418, 2.1: "In accordance with current recommendations, patients with LADA were classified within the T1DM group for the main comparative analyses."
- PMC12940418, 2.4: "fasting C-peptide concentration (2.86 vs. 0.10 ng/mL, p < 0.001)" after about seven years (T2DM versus T1DM).
- PMC12940418, Introduction: "While detection of islet autoantibodies remains the diagnostic standard for autoimmune diabetes, antibody testing is not universally available"

Support check
- Supported: MMTT C-peptide in LADA is intermediate between T1D and T2D (AUC 41.3, 140.8, 275.5); stimulated 1.35 versus 4.6 ng/mL (T1DM group versus T2DM); fasting 0.10 ng/mL at about 7 years in T1DM.
- Qualified: in PMC12940418 LADA is pooled in the T1DM group for the main comparison, so the draft's 1.35 (T1D) and 1.86 (LADA) split was not verified (the 1.86 and 4.60 patterns returned only the 4.6 and 1.35 figures in the shown matches; 46 matches, 6 shown). The draft's "T1D fasting C-peptide fell from 0.95" was not seen; the shown fasting value at diagnosis for the T1DM group is 0.87 ng/mL. Treat 0.95 as unverified and prefer 0.87 only after checking the group definition.
- Cut-offs: no treatment-selection cut-off found. PMC4297398 patterns "C-peptide|cut|LADA" (86 matches, 8 shown) and "Conclusion|intermediate|nmol|ng/mL|treatment|cut-off" (28 matches, 8 shown): the only "cut-off" is for antibody positivity (5 and 15 U/mL). PMC12940418 patterns "cut|threshold|stimulated|treatment" (47 matches, 10 shown): no C-peptide treatment threshold shown.
- Guideline: none read; "current consensus" is the authors' statement, not a quoted consensus text. The draft's second-hand ADA/EASD cut-offs (<0.2, >0.6 nmol/L) remain unverified [from the 40781799 abstract, not re-read here].
- The MMTT-versus-glucagon difference matters: 25572256 used MMTT, 41752170 used glucagon (6-min value). Values are not interchangeable.

Proposed status: research-only for treatment choice (unchanged); classification and prognosis of decline stay limited, descriptive, linked to rows 6 and 31.
Proposed wording: "Adults with LADA or newly diagnosed diabetes: MMTT or glucagon-stimulated C-peptide to describe residual beta-cell function (LADA intermediate between T1D and T2D in MMTT AUC). Stimulated C-peptide is the accepted trial outcome for beta-cell preservation (authors' statement). No C-peptide cut-off that selects treatment was found in the full texts read. Assay and protocol (MMTT vs glucagon) must be stated."

## Summary
- No row qualifies as established: no quoted guideline, consensus or regulatory text recommends these tests for these decisions. ADA 2026 recs 2.6 and 2.7 concern autoantibody screening only.
- Corrections to the draft: D4 insulinogenic-index prediction not confirmed (glucose-based predictors seen); D5 numbers 1.86 and 0.95 not verified, LADA pooled with T1DM in 41752170; D2 AUC C-peptide was not associated with progression in the model study, and the Index60 thresholds were applied to the full cohort after removing progressors.
- Unread: Insel 2015 (wrong PMCID PMC5444099), Cryer 2009 (redirect not followed).
- Tool calls used: 25 including the file read, the web fetch, the write and the final hand-off.
