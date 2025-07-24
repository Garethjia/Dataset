import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('0620b.csv') 


corr_matrix = df[['Altitude', 'O2', 'SPO2', 'Heart rate', 'Respiratory rate']].corr(method='pearson')
print("Pearson Correlation Matrix:")
print(corr_matrix)


plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix,
    annot=True, 
    fmt='.2f',
    cmap='coolwarm', 
    vmin=-1, vmax=1 
)
plt.title('Heatmap of Pearson Correlation')
plt.show()
