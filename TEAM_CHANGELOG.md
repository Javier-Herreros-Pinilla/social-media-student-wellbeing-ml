# Team Change Log & Responsibility Tracker - Milestone 2 (KDD Pipeline)

This document serves as a shared template for tracking individual progress and documenting all changes made to the **Python Notebook** (`Entrega_2_Pipeline_KDD_EDA_Preproceso.ipynb`) and the **Technical Report** (`Entrega_2_Informe_Estado_Practica_KDD.docx`).

---

## Overview & Deadlines

| # | Member | Role | KDD Stage / Module | Deadline | Status |
| :-: | :--- | :--- | :--- | :---: | :---: |
| 1 | **Abdelmouiz kobry** | Ingestion & Integration Engineer | Selection & Integration (Module 1) | Nov 20 (20:00) | ✅ Completed |
| 2 | **Ernesto** | Quality & EDA Analyst | Cleaning & Exploration (Module 2) | Nov 20 (22:00) | ✅ Completed |
| 3 | **Pablo** | Transformation Engineer | Preprocessing & Feature Eng. (Module 3) | Nov 21 (20:00) | ✅ Completed |
| 4 | **Yeni** | Data Card Architect | Reduction & Projection (Module 4) | Nov 22 (20:00) | ✅ Completed |
| 5 | **Javier** | ML Strategist & Coordinator | Mining & Final Editing (Module 5) | Nov 23 (22:00) | ✅ Completed |

*(Status legend: `⬜ Pending` · `🟨 In Progress` · `✅ Completed`)*

---

## 1. Abdelmouiz kobry - Ingestion & Integration Engineer
- **KDD Stage:** Selection & Integration (Module 1)
- **Deadline:** Nov 20 (20:00)

### Assigned Tasks
- **Python Notebook (`.ipynb`)**
  - [x] Verify & ingest public CSV mirror ($N=4,500$, $d=16$) via `src/fuente_auditoria.py` (no synthetic fallback; bit-for-bit match with Kaggle original not certified).
  - [x] Remove `Student_ID` and normalize category labels (`src/seleccion_normalizacion.py`).
  - [x] Execute `LEFT JOIN` contextual integration with Spanish Open Data sources (INE 2025, SIIU 2024/25, OEDA-ESTUDES 2025) in a descriptive-only view excluded from predictors (`src/integracion_contextual.py`).
- **Word Report (`.docx`)**
  - [x] Section 1 (~1.0 page): Justification of baseline variables, prevention of leakage between targets, and descriptive Macro-to-Micro table (integrated into root `Entrega_2_Informe_Estado_Practica_KDD.docx`).

### Change Log
| Date (YYYY-MM-DD) | Files Modified | Summary of Changes | Notes / Handoff |
| :--- | :--- | :--- | :--- |
| 2026-11-19 / 2026-11-20 | `modulo1_abdelmouiz_kobry/*`, `Entrega_2_Pipeline_KDD_EDA_Preproceso.ipynb`, `README.md`, `TEAM_CHANGELOG.md` | PR #1 & PR #2: Added audited CSV ingestion, category normalization & `Student_ID` removal, descriptive-only INE/SIIU/ESTUDES joins, unit tests, and `Seccion_1_Abdelmouiz_kobry.docx`. | Moved into unified `src/`, `data/`, and `tests/` folders on Nov 25; Section 1 merged into root `.docx`. |
| 2026-11-23 | `tarjeta_datos_consolidada_H2.csv`, `Entrega_2_Pipeline_KDD_EDA_Preproceso.ipynb`, `README.md` | PR #5 & PR #6: Rebuilt `tarjeta_datos_consolidada_H2.csv` (4,500 x 32: 29 predictors, `Split`, 2 targets; 85 NaNs preserved in `Target_GPA`) and unified the full M0–M5 notebook pipeline on the verified real data. | Handed off to Javier for final CV pipeline refinement and `.docx` consolidation. |

---

## 2. Ernesto - Quality & EDA Analyst
- **KDD Stage:** Cleaning & Exploration (Module 2)
- **Deadline:** Nov 20 (22:00)

### Assigned Tasks
- **Python Notebook (`.ipynb`)**
  - [x] Audit nulls (131 incomplete rows: 85 `Academic_Performance_GPA`, 46 `Perceived_Stress_Score`) and duplicates (0 exact duplicates).
  - [x] Validate physical rules (`Usage + Sleep <= 24h`: max 19.5h, 0 violations).
  - [x] Detect outliers with IQR and LOF (`k=20`, `contamination=0.02`), tagging `LOF_Outlier_Flag` (88 flagged of 4,369 complete rows; 131 `<NA>`).
  - [x] Generate LOWESS curves and H1 boxplots / stacked bar chart (`Figura_1_EDA_H1.png`).
- **Word Report (`.docx`)**
  - [x] Sections 2.1 and 2.4 (~1.5 pages): Quality audit, retention criteria for extreme clinical profiles, and multi-panel Figure 1 (300 DPI).

### Change Log
| Date (YYYY-MM-DD) | Files Modified | Summary of Changes | Notes / Handoff |
| :--- | :--- | :--- | :--- |
| 2026-11-20 | `Entrega_2_Pipeline_KDD_EDA_Preproceso.ipynb`, `Entrega_2_Informe_Estado_Practica_KDD.docx`, `Figura_1_EDA_H1.png` | PR #3: Completed Module 2 using the normalized Module 1 data (`df_base`). Audited 4,500 records, found no exact duplicates or 24-hour rule violations, and flagged 88 of 4,369 complete records with LOF. Updated Sections 2.1 and 2.4 and exported Figure 1 at 300 DPI. | Completed. `LOF_Outlier_Flag` is exploratory only and excluded from model predictors. |

---

## 3. Pablo - Transformation Engineer
- **KDD Stage:** Preprocessing & Feature Engineering (Module 3)
- **Deadline:** Nov 21 (20:00)

### Assigned Tasks
- **Python Notebook (`.ipynb`)**
  - [x] Compute aggregations (`Weekly_Total_Hours`, `Weekend_Binge_Ratio`) and H1 indices (`DSDI`, `CWU`; `Relative_Usage_Delta` & `GPA_Cohort_Delta` dropped as they depend on aggregated INE/SIIU means).
  - [x] Discretize PSS using Cohen's clinical thresholds (`PSS_Clinical_Tier` / `PSS_Clinical_Ord`).
  - [x] Implement One-Hot Encoding (14 columns), stratified 70/30 split, median imputation, and dual scaling (Z-score / Min-Max) fitted on Train only (29 predictors total).
- **Word Report (`.docx`)**
  - [x] Sections 2.2 and 2.3 (~1.0 page): Mathematical formulation of synthetic variables, derived attributes table, and justification for dual scaling.

### Change Log
| Date (YYYY-MM-DD) | Files Modified | Summary of Changes | Notes / Handoff |
| :--- | :--- | :--- | :--- |
| 2026-11-21 | `Entrega_2_Pipeline_KDD_EDA_Preproceso.ipynb`, `Entrega_2_Informe_Estado_Practica_KDD.docx` | PR #4: Module 3 rebuilt on the real data (`df_base`): aggregations, DSDI, CWU and clinical PSS tiers (52.69% low, 41.22% moderate, 5.07% high, 1.02% NaN). Removed `Relative_Usage_Delta` and `GPA_Cohort_Delta`. Added One-Hot encoding (14 columns), stratified 70/30 split, median imputation and Z-score/Min-Max scaling, all fitted on Train only (29 features). Rewrote Sections 2.2 and 2.3 of the report with real figures. | Class balance in Train: Beneficial 81.81%, Neutral 14.54%, Negative 3.65%. |

---

## 4. Yeni - Data Card Architect
- **KDD Stage:** Reduction & Projection (Module 4)
- **Deadline:** Nov 22 (20:00)

### Assigned Tasks
- **Python Notebook (`.ipynb`)**
  - [x] Compute Mutual Information and Random Forest feature importance (`Perceived_Stress_Score`, `Mental_Health_Index`, `Weekly_Total_Hours`, `Daily_Usage_Hours`, `DSDI` top features).
  - [x] Fit PCA (`14` PCs >= 85.18% variance on the 29 real predictors).
  - [x] Reuse stratified 70/30 Holdout split + run 10-fold CV without leakage (`Pipeline`).
  - [x] Export `tarjeta_datos_consolidada_H2.csv` (4,500 x 32: 29 predictors + `Split` + 2 targets) and `Figura_2_PCA_Ranking.png`.
- **Word Report (`.docx`)**
  - [x] Section 3 (~1.0 page): Data Card technical sheet (29 predictors + 2 targets), table by functional blocks, and Figure 2 (PCA and ranking) — consolidated into root `Entrega_2_Informe_Estado_Practica_KDD.docx`.

### Change Log
| Date (YYYY-MM-DD) | Files Modified | Summary of Changes | Notes / Handoff |
| :--- | :--- | :--- | :--- |
| 2026-11-22 | `Figura_2_PCA_Ranking.png`, `modul4-yeni/Entrega_2_Informe_Estado_Practica_KDD.docx`, `modul4-yeni/Entrega_2_Pipeline_KDD_EDA_Preproceso (3).ipynb` | Added `Figura_2_PCA_Ranking.png`, updated Section 3 table (29 predictors across 6 blocks), Section 3.1 (RF/MI metrics, 14 PCs = 85.2% variance), and embedded Figure 2. | Notebook code & CSV integrated in PR #5/#6; Section 3 & Figure 2 consolidated into root `.docx` and `modul4-yeni/` removed on Nov 25. |

---

## 5. Javier - ML Strategist & Coordinator
- **KDD Stage:** Mining & Final Editing (Module 5)
- **Deadline:** Nov 23 (22:00)

### Assigned Tasks
- **Python Notebook (`.ipynb`)**
  - [x] Run baseline prototypes in 10-fold CV with per-fold `SimpleImputer` + scaler `Pipeline` on `X_train_raw` (CART F1-Macro `0.8483`, k-NN `0.6595`, Random Forest `0.8885`, k-Means Silhouette `0.2023`) and verify `tarjeta_datos_consolidada_H2.csv`.
  - [x] Freeze global seed (`RANDOM_SEED = 42`).
- **Word Report (`.docx`)**
  - [x] Consolidate Section 1 (Abdelmouiz) and Section 3 + Figure 2 (Yeni) into root `Entrega_2_Informe_Estado_Practica_KDD.docx`.
  - [x] Update top KPI banner, header metadata (Nov 27 deadline), and fix Section 3 predictor count (`29`).
  - [x] Section 4 (~0.8 pages): Update 4 Lines of Work (remove outdated `SIIU` predictor reference) + update Traceability Matrix with verified Module 5 metrics and unified repo evidence.
  - [x] Unify repository structure (`src/`, `data/`, `tests/`, `requirements.txt`, `.gitignore`), remove duplicate per-member folders, update `README.md`, and run all tests + full notebook end-to-end.

### Change Log
| Date (YYYY-MM-DD) | Files Modified | Summary of Changes | Notes / Handoff |
| :--- | :--- | :--- | :--- |
| 2026-11-25 | `src/*`, `data/*`, `tests/*`, `requirements.txt`, `.gitignore`, `Entrega_2_Pipeline_KDD_EDA_Preproceso.ipynb`, `Entrega_2_Informe_Estado_Practica_KDD.docx`, `README.md`, `TEAM_CHANGELOG.md` | Unified repository structure into root (`src/`, `data/`, `tests/`), removed `modulo1_abdelmouiz_kobry/` and `modul4-yeni/`, added optional `statsmodels` fallback in Module 2 EDA, fixed per-fold median imputation `Pipeline` in Module 4 & Module 5 CV, verified `tarjeta_datos_consolidada_H2.csv` + 11/11 unit tests + full notebook execution, consolidated all 4 sections & figures into `Entrega_2_Informe_Estado_Practica_KDD.docx`, and updated `README.md`. | Ready for Milestone 2 submission (Nov 27, 2026). |
