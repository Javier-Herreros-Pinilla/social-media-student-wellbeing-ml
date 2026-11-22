# Team Change Log & Responsibility Tracker  -  Milestone 2 (KDD Pipeline)

This document serves as a shared template for tracking individual progress and documenting all changes made to the **Python Notebook** (`Entrega_2_Pipeline_KDD_EDA_Preproceso.ipynb`) and the **Technical Report** (`Entrega_2_Informe_Estado_Practica_KDD.docx`).

> **How to use this template:**
> 1. Locate your assigned section below.
> 2. Check off tasks (`- [x]`) as you complete them and update your status in the **Overview Table**.
> 3. Every time you make a change (code, figures, CSV outputs, or report sections), add a new row to your **Change Log** table with the date, modified files, a concise description of what changed, and any open issues or handoff notes for the next module.

---

## Overview & Deadlines

| # | Member | Role | KDD Stage / Module | Deadline | Status |
| :-: | :--- | :--- | :--- | :---: | :---: |
| 1 | **Abdelmouiz kobry** | Ingestion & Integration Engineer | Selection & Integration (Module 1) | Nov 20 (20:00) | ⬜ Pending |
| 2 | **Ernesto** | Quality & EDA Analyst | Cleaning & Exploration (Module 2) | Nov 20 (22:00) | ⬜ Pending |
| 3 | **Pablo** | Transformation Engineer | Preprocessing & Feature Eng. (Module 3) | Nov 21 (20:00) | ✅ Completed |
| 4 | **Yeni** | Data Card Architect | Reduction & Projection (Module 4) | Nov 22 (20:00) | ⬜ Pending |
| 5 | **Javier** | ML Strategist & Coordinator | Mining & Final Editing (Module 5) | Nov 23 (22:00) | ⬜ Pending |

*(Status legend: `⬜ Pending` · `🟨 In Progress` · `✅ Completed`)*

---

## 1. Abdelmouiz kobry  -  Ingestion & Integration Engineer
- **KDD Stage:** Selection & Integration (Module 1)
- **Deadline:** Nov 20 (20:00)

### Assigned Tasks
- **Python Notebook (`.ipynb`)**
  - [ ] Download Kaggle CSV ($N=4,500$, $d=16$).
  - [ ] Remove `Student_ID` (prevents overfitting in trees).
  - [ ] Normalize UTF-8 keys and execute a Left Join with Open Data sources (INE, SIIU, and OEDA-ESTUDES).
- **Word Report (`.docx`)**
  - [ ] Section 1 (~1.0 page): Justification of baseline variables, prevention of leakage between targets, and Macro-to-Micro enrichment table.

### Change Log
| Date (YYYY-MM-DD) | Files Modified | Summary of Changes | Notes / Handoff |
| :--- | :--- | :--- | :--- |
| *YYYY-MM-DD* | *e.g. `.ipynb`, `.docx`* | *Describe the changes made...* | *Any blockers or notes for Module 2* |

---

## 2. Ernesto  -  Quality & EDA Analyst
- **KDD Stage:** Cleaning & Exploration (Module 2)
- **Deadline:** Nov 20 (22:00)

### Assigned Tasks
- **Python Notebook (`.ipynb`)**
  - [ ] Audit nulls (0%) and duplicates.
  - [ ] Validate physical rules (`Usage + Sleep <= 24h`).
  - [ ] Detect outliers with IQR and LOF (`k=20`), tagging `LOF_Outlier_Flag`.
  - [ ] Generate LOWESS curves and H1 boxplots.
- **Word Report (`.docx`)**
  - [ ] Sections 2.1 and 2.4 (~1.5 pages): Quality audit, retention criteria for extreme clinical profiles, and multi-panel Figure 1 (300 DPI).

### Change Log
| 2026-11-20 | Entrega_2_Pipeline_KDD_EDA_Preproceso.ipynb, Entrega_2_Informe_Estado_Practica_KDD.docx, Figura_1_EDA_H1.png | Completed Module 2 using the normalized Module 1 data. Audited 4,500 records, found no exact duplicates or 24-hour rule violations, and flagged 88 of 4,369 complete records with LOF. Updated sections 2.1 and 2.4 and exported Figure 1 at 300 DPI. | The new analysis uses df_base. Modules 3 and 4 still use the earlier df_integrated pipeline. The new LOF flag includes GPA in its calculation and is for exploratory analysis only. |
| :--- | :--- | :--- | :--- |
| *YYYY-MM-DD* | *e.g. `.ipynb`, `.docx`* | *Describe the changes made...* | *Any blockers or notes for Module 3* |

---

## 3. Pablo  -  Transformation Engineer
- **KDD Stage:** Preprocessing & Feature Engineering (Module 3)
- **Deadline:** Nov 21 (20:00)

### Assigned Tasks
- **Python Notebook (`.ipynb`)**
  - [X] Compute aggregations (`Weekly_Total_Hours`, `Weekend_Binge_Ratio`) and H1 indices (`DSDI`, `CWU`, `Relative_Usage_Delta`).
  - [X] Discretize PSS using Cohen's clinical thresholds.
  - [X] Implement One-Hot Encoding (OHE) and dual scaling (Z-score / Min-Max).
- **Word Report (`.docx`)**
  - [X] Sections 2.2 and 2.3 (~1.0 page): Mathematical formulation of synthetic variables, derived attributes table, and justification for dual scaling.

### Change Log
| Date (YYYY-MM-DD) | Files Modified | Summary of Changes | Notes / Handoff |
| :--- | :--- | :--- | :--- |
| 2026-11-21 | Entrega_2_Pipeline_KDD_EDA_Preproceso.ipynb, Entrega_2_Informe_Estado_Practica_KDD.docx | Module 3 rebuilt on the real data (df_base): aggregations, DSDI, CWU and clinical PSS tiers (52.69% low, 41.22% moderate, 5.07% high, 1.02% NaN). Removed Relative_Usage_Delta and GPA_Cohort_Delta (they depend on aggregated INE/SIIU means). Added One-Hot encoding (14 columns), stratified 70/30 split, median imputation and Z-score/Min-Max scaling, all fitted on train only (X_train/X_test, X_train_z/X_test_z, X_train_mm/X_test_mm, y_clf_*, y_reg_*; 29 features). Rewrote sections 2.2 and 2.3 of the report with real figures. | For Module 4: the split and scaling are now done in my cell; please reuse those variables instead of repeating them. INE_Benchmark_*, Expected_Cohort_GPA, ESTUDES_Risk_Prior, Relative_Usage_Delta and LOF_Outlier_Flag are not in the feature set; remove them from your column list. Class balance in train: Beneficial 81.8%, Neutral 14.5%, Negative 3.7%, so use Macro F1 and stratification. |

---

## 4. Yeni  -  Data Card Architect
- **KDD Stage:** Reduction & Projection (Module 4)
- **Deadline:** Nov 22 (20:00)

### Assigned Tasks
- **Python Notebook (`.ipynb`)**
  - [ ] Compute Mutual Information and Random Forest feature importance.
  - [ ] Fit PCA (13 PCs >= 85.4% variance).
  - [ ] Execute stratified 70/30 Holdout split + 10-fold CV without data leakage.
  - [ ] Export `tarjeta_datos_consolidada_H2.csv`.
- **Word Report (`.docx`)**
  - [ ] Section 3 (~1.0 page): Data Card technical sheet (31 predictors + 2 targets), table by functional blocks, and Figure 2 (PCA and ranking).

### Change Log
| Date (YYYY-MM-DD) | Files Modified | Summary of Changes | Notes / Handoff |
| :--- | :--- | :--- | :--- |
| 2026-11-22 | *e.g. `.ipynb`, `.docx`, `.csv`* | *Describe the changes made...* | *Any blockers or notes for Module 5* |

---

## 5. Javier  -  ML Strategist & Coordinator
- **KDD Stage:** Mining & Final Editing (Module 5)
- **Deadline:** Nov 23 (22:00)

### Assigned Tasks
- **Python Notebook (`.ipynb`)**
  - [ ] Run baseline prototypes in 10-fold CV (CART, k-NN, Random Forest, and k-Means), verifying the executability of the final CSV.
  - [ ] Freeze global seed (`RANDOM_SEED = 42`).
- **Word Report (`.docx`)**
  - [ ] Section 4 (~0.8 pages): Definition of the 4 Lines of Work (Fayyad) + Traceability matrix with evaluation criteria.
  - [ ] Global 5-page review.

### Change Log
| Date (YYYY-MM-DD) | Files Modified | Summary of Changes | Notes / Handoff |
| :--- | :--- | :--- | :--- |
| *YYYY-MM-DD* | *e.g. `.ipynb`, `.docx`* | *Describe the changes made...* | *Final integration & submission notes* |
