# Home C-peptide sampling precedents: ITAD and INNODIA (2026-10-25)

Purpose: confirm how the two precedents named in `usecases/scoring/metsulin-fit.md` (candidates N1, N2, N6) sample C-peptide at home. Read 2026-10-25 by the main session; 3 look-ups (PMC full text of the ITAD protocol through `tools/pmc_text.py`; PubMed record of Hendriks 2025). Measure type: capillary (finger-prick) dried blood spot (DBS) C-peptide, fasting and post-meal.

## ITAD: Interleukin-2 Therapy of Autoimmunity in Diabetes
Source: Marcovecchio et al., Wellcome Open Research 2020, protocol, PMID 32399500, DOI 10.12688/wellcomeopenres.15697.1, PMC7194454. Read level: full text (PMC XML, keyword passages and the visit table).
- Design: phase 2, multicentre, double-blind, placebo-controlled, randomised 2:1; 45 children and adolescents aged 6-18 with type 1 diabetes diagnosed within 6 weeks; ultra-low-dose aldesleukin (IL-2) twice weekly for 6 months, given at home by a research nurse.
- Primary endpoint: "Differences in slopes of dried blood spot (DBS) C-peptide over the 6 month-treatment period between the active and placebo groups", from "weekly assessments of fasting and post-prandial C-peptide from DBS".
- Home collection: participants are taught at the baseline visit to collect DBS for C-peptide weekly at home, with a record of finger-prick blood glucose; the first home DBS is supervised by a research nurse; samples are stored and analysed in batches.
- Schedule: weekly DBS between the monthly visits up to 6 months, then monthly from months 7 to 12 (about 30 to 32 home sample sets in year 1, a derivation from the schedule).
- Stimulus: Ensure Plus liquid meal or a list of standardised breakfasts for the post-prandial sample. The exact sampling time after the meal was not found in the passages read.
- Rationale stated by the authors: venous C-peptide and the mixed-meal test "are invasive and not feasible in the home setting"; weekly DBS "provides a dense profile of C-peptide changes where the slope ... is the metric on which trial power calculations can be based". The DBS method was validated against venous C-peptide and the mixed-meal test in their earlier work (reference 35 of the protocol; the project lists Willemsen 2018, PMID 29860430, DOI 10.1210/jc.2018-00500, for this).
- Not found in the passages read: the C-peptide assay and laboratory, and trial results. ITAD is not in the 72-trial count (`usecases/scoring/t1d-preservation-trials.md`), because its protocol predates the 2021 window.

## INNODIA home DBS study
INNODIA is a European research network on type 1 diabetes (Innovative Medicines Initiative), not a single trial; its linked trials include MELD-ATG and Ver-A-T1D.
Source: Hendriks et al., Diabetes Care 2025;48(9):1484-1492, PMID 40402094, DOI 10.2337/dc25-0214. Read level: abstract only (no PubMed Central copy; full text not read).
- Population: 292 people with newly diagnosed type 1 diabetes (recruited within 6 weeks of diagnosis; mean age 12.7, range 1.2 to 43.8 years) in the INNODIA cohort.
- Home collection: finger-prick DBS at home, fasting and 60 minutes after a liquid meal; median 6.5 card pairs per participant over 12 months (IQR 2 to 9).
- Reference: venous mixed-meal test at 12 months (C-peptide AUC and peak).
- Result: the 6-month slope of stimulated (post-meal) DBS C-peptide predicted 12-month mixed-meal AUC and peak C-peptide (P < 0.01), adjusted for simultaneous glucose, age and baseline fasting C-peptide; the fasting DBS slope did not.
- Authors' conclusion: feasible; potential for optimising trial design; "further validation is needed".
- Laboratory: the author list includes the NIHR Cambridge Biomedical Research Centre Core Biochemistry Assay Laboratory (affiliation only; assay not read).

## What this means for a home capillary C-peptide test
- The post-meal sample, not the fasting one, carries the signal; a home product needs a standard meal or drink and a fixed sampling time (60 minutes in INNODIA).
- Glucose is recorded with every sample in both (finger-prick glucose in ITAD; adjustment for simultaneous glucose in INNODIA).
- Real-world adherence is lower than protocol: ITAD plans weekly samples; INNODIA participants returned a median of 6.5 pairs in a year. A device that is easier than a mailed DBS card could improve this; that is a hypothesis.
- Both are academic and European (UK and EU); no US or industry precedent was found in the registry count.
