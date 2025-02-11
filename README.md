# gene-expression-analysis_lung-cancer
# Gene Expression Data Analysis

This project analyzes gene expression data from the **GSE60486** dataset using Python. The analysis focuses on identifying highly expressed genes and visualizing expression patterns across samples.

## Dataset
- **Source:** [GEO Dataset GSE60486](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE60486)
- **Description:** Preprocessed gene expression data from lung cancer samples.

## Methods
- **Data Cleaning:** Removed metadata rows and converted expression values to numeric format.
- **Exploratory Data Analysis (EDA):**
  - **Histogram** of overall gene expression values.
  - **Boxplot** of gene expression across samples.
  - **Heatmap** of the top 20 highly expressed genes.

## Key Findings
- The top 10 highly expressed genes include:
  1. **AFFX-hum_alu_at** – Mean Expression: 13.47
  2. **201429_s_at** – Mean Expression: 13.37
  3. **212869_x_at** – Mean Expression: 13.36
  *(See the full list in the analysis.)*

## Visualizations
- **Histogram:** Distribution of gene expression values.
- **Boxplot:** Variability of gene expression across selected samples.
- **Heatmap:** Top 20 highly expressed genes.



Acknowledgements
Dataset from NCBI GEO.
Analysis performed using Python and open-source libraries.

