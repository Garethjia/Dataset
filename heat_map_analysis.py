import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('0620b.csv') 

height_bins = [5000, 5500, 6000, 6500, 7000, 7500]
o2_bins = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

df["Altitude1"] = pd.cut(df["Altitude"], bins=height_bins, right=False)
df["O21"] = pd.cut(df["O2"], bins=o2_bins, right=False)

metric_heat = df.groupby(["Altitude1", "O21"])[["SPO2", "Heart rate", "Respiratory rate"]].mean().unstack()


plt.figure(figsize=(10, 6))
ax = sns.heatmap(metric_heat["SPO2"], annot=True, cmap='viridis', fmt=".1f", linewidths=.5)
ax.invert_yaxis()
plt.title("Average SPO2 heat maps")
plt.xlabel("O2")
plt.ylabel("Altitude")
plt.show()