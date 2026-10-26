# FT9 full-text review (C061, C062, C075, C125, C153, C157, C158, C174, C184)

All nine texts were read locally. C153 and C157 are partly garbled two-column PDF text; the rest are good. No score proposals (score files not opened; assumed not tied to these papers).

## Per paper
- C061 MAFLD consensus (confirms): HOMA-IR 2.5 is one of seven criteria; at least two are needed in lean adults only. Fasting-based, optional. The Korean-criticism sentence is not from this paper.
- C062 Mendelian randomization (adds nuance): ORs confirmed (CAD 1.79, SAO 1.80). The authors' own sensitivity analyses lose the signal with the lipid-free 28-SNP and the 5-SNP clamp instruments, and they attribute it mainly to lipids.
- C075 HOMA-IR change and fibrosis (adds nuance): n=15,728, 86% men confirmed. Fibrosis by NFS and APRI only, retrospective; the two scores disagreed; shared components admitted by the authors.
- C125 eGDR in type 1 diabetes (adds nuance): MACE HR 0.79 per unit (I2 63%), not significant in studies of 1,000 or more; four equations; authors recommend routine eGDR monitoring on observational data only. Non-insulin surrogate.
- C153 breast metformin window trial (adds nuance): HOMA fell; but exploratory subgroups tie baseline fasting glucose above 5.3 mmol/L and on-treatment insulin fall to tumour response. Baseline insulin or HOMA was not reported as a predictor.
- C157 endometrial pilot (confirms): fasting insulin fell 13.36 to 5.2 mU/l in 11 patients; no insulin-as-predictor test.
- C158 intranasal detemir (adds nuance): the measure is named in the full text (HOMA-IR, plus OGTT insulin AUC adjusted for glucose AUC). APOE-4 moderated the main effect. Which index r=0.54 uses is not stated in the passages read.
- C174 TOBOGM (adds nuance): first primary outcome met (24.9% vs 30.5%; RD -5.6, -10.1 to -1.2), the other two not. Glucose OGTT only; no insulin.
- C184 STAMPEDE metformin (adds nuance): OS null (HR 0.91, 0.80-1.03); PFS signal in high-volume disease (interaction p=0.012); no insulin subgroup.

## Claim issues (all in merged-conclusion.md; exact wording in FT9.json)
1. Line 100: state that the two-criteria rule is for lean adults; drop nothing else (C061; GL-40, EV-35).
2. Line 101: add that the lipid-free and clamp-based instruments lose the association (C062; EV-38). Lowers confidence that the signal is IR-specific.
3. Line 105: add the heterogeneity, non-significance in larger studies and HbA1c-in-score caveat (C125; EV-40).
4. Line 106: add NFS/APRI-only, retrospective, discordant scores (C075; EV-41).
5. Line 97: read level is full text; add the exploratory glucose and insulin-fall links and the STAMPEDE high-volume PFS signal (C153, C157, C184; TRI-43, TRI-44, EV-35).
6. Line 109: replace "IR measure not named" with HOMA-IR plus OGTT insulin AUC; APOE-4 was the moderator (C158; ABS-15).
7. Line 109: TOBOGM did show benefit on the first primary outcome (C174; ABS-14).

Tool calls used: about 12 (reads, greps, two writes).
