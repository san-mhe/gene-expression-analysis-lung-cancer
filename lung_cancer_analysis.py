import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load and clean data
file_path = 'data/GSE60486_normalized.txt.gz'
data = pd.read_csv(file_path, sep='\t', skiprows=6, low_memory=False)
data.columns = data.iloc[0]
data = data[1:]
data.reset_index(drop=True, inplace=True)
data.rename(columns={'ID_REF': 'Gene_ID'}, inplace=True)

expression_data = data.drop(columns=['Gene_ID']).apply(pd.to_numeric, errors='coerce')
data_cleaned = pd.concat([data['Gene_ID'], expression_data], axis=1)
data_cleaned = data_cleaned.loc[:, ~data_cleaned.columns.str.contains('ABS_CALL')]



plt.savefig('histogram_expression.png')
plt.savefig('boxplot_expression.png')
plt.savefig('heatmap_top20_genes.png')







