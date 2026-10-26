# FT5 full-text review (C001, C007, C010, C016, C034, C085, C088, C101, C135)

Reader: full-text reader. Text files read locally; no web use. Machine-readable version: `usecases/scoring/ft-review/FT5.json`.

## Per paper

| ID | Paper | Text | Verdict | What changed |
|---|---|---|---|---|
| C001 | Matsuda 1999 (10480510) | partial (garbled tables) | adds nuance | r 0.73 is from the derivation sample (n=153), no independent validation; fasting ISI(HOMA) r 0.69 in same data. Post-load index. |
| C007 | Sumner 2005 (15983289) | good | confirms | TG and TG/HDL-C AUC 0.55 and 0.56 in 98 African American adults, BMI 25 or more; reference FSIVGTT, not clamp; fasting insulin AUC 0.85. |
| C010 | Wilson 2007 (17533210) | good | adds nuance | Insulin WAS included (fasting insulin, Gutt, HOMA-IR). Outcome is incident T2D, not CVD. AROC 0.850-0.854 vs 0.85. Resolves "not verified". |
| C016 | Kalogeropoulos 2009 (19700136) | good | adds nuance | The OGTT measure is 2-h glucose; insulin was fasting only. It is a fasting insulin/HOMA null, not a post-load insulin result. n=2386, age 70-79. |
| C034 | Schmiegelow 2015 (25944628) | good | confirms | HR after HDL-C adjustment 1.06 (insulin, HOMA-IR); delta c 0.001-0.002; weak gain only in simpler models. |
| C085 | Wang 2022 (35700159) | good | adds nuance | 1.04 (0.92-1.18) in NGT confirmed; it is an association study, 3.6-year follow-up, no BMI/lipid/BP in main model. |
| C088 | Gonzalez-Gonzalez 2022 (36181637) | good | adds nuance | Numbers correct; I2 94% (T2D), 84% (non-fatal MACE); fatal MACE HR 1.31 (0.96-1.77); authors call clinical utility questionable. |
| C101 | Tobias 2023 (37794253) | good | adds nuance | TyG "moderate evidence" is for CVD prognosis in people with T2D; not a recommendation for clinical use. |
| C135 | Liu 2026 (42569452) | good | adds nuance | Numbers correct; pooled base models were mixed (not all Framingham); I2 99.1%; authors call gain clinically trivial; some p/CI inconsistencies in own-cohort NRI. |

No paper contradicts the project. No score proposals (proposals list empty).

## Claim issues (exact replacements are in the JSON)

1. EV-14 (Health ABC): OGTT measure is 2-h glucose, no post-load insulin; it is a fasting null.
2. EV-15 / EV-28 (Framingham Offspring): insulin included; outcome is diabetes, not CVD.
3. EV-28 (Wang 2022): association study with a glucose-tolerance interaction, not incremental prediction; add follow-up and adjustment scope.
4. GL-34 / line 26 (ADA/EASD 2023): TyG statement is for people with T2D; GL-34 wrongly calls ATTICA a null.
5. EV-18 / EV-25 (Liu 2026): the pooled analysis is not "against Framingham"; add I2 99.1% and the mixed base models.
6. EV-29 (HOMA-IR meta-analysis): add heterogeneity and the fatal MACE interval.
7. MEAS-04 (Matsuda): in-sample r; HOMA-based index r 0.69.
8. MEAS-02 (Sumner): add scope (n=98, age 20-50, FSIVGTT, tertile).

Confidence effect (no figures proposed): items 1 and 2 slightly lower the weight of those two papers as evidence on post-load prediction (the files hold no post-load insulin prediction result from them); items 5 and 6 leave the fasting and TyG statements as they are; the rest are scope notes.

Tool calls used: 20 (18 reads/searches, 2 writes).
