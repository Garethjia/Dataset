import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('0620b.csv') 
df['SPO2'] = df['SPO2'].round().astype(int)

metrics = ['O2', 'SPO2', 'Heart rate', 'Respiratory rate']
fig = plt.figure(figsize=(9, 6)) 

plt.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.05, wspace=0.3, hspace=0.3)

plt.subplot(2, 2, 1) 
sns.boxplot(x='Altitude', y='O2', data=df, palette='viridis')
plt.xlabel('Altitude', fontsize=12)
plt.ylabel('O2', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7) 
fig.text(0.02, 0.96, f'a)', fontsize=15, fontweight='bold', va='top', ha='left')

plt.subplot(2, 2, 2) 
sns.boxplot(x='SPO2', y='O2', data=df, palette='viridis')
plt.xlabel('SPO2', fontsize=12)
plt.ylabel('O2', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7) 
fig.text(0.50, 0.96, f'b)', fontsize=15, fontweight='bold', va='top', ha='left')

plt.subplot(2, 2, 3) 
sns.boxplot(x='Altitude', y='Heart rate', data=df, palette='viridis')
plt.xlabel('Altitude', fontsize=12)
plt.ylabel('Heart rate', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7) 
fig.text(0.02, 0.47, f'c)', fontsize=15, fontweight='bold', va='top', ha='left')

plt.subplot(2, 2, 4)
sns.boxplot(x='SPO2', y='Heart rate', data=df, palette='viridis')
plt.xlabel('SPO2', fontsize=12)
plt.ylabel('Heart rate', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
fig.text(0.50, 0.47, f'd)', fontsize=15, fontweight='bold', va='top', ha='left')

plt.tight_layout() 
plt.show()

