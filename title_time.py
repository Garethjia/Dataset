import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('0620b.csv') 

df['Time'] = pd.to_datetime(df['Time'])

fig = plt.figure(figsize=(20, 14))



plt.subplot(5, 1, 1)
plt.plot(df['Time'], df['Altitude'], label='Altitude',linewidth=1.5)
plt.ylabel('Altitude (m)')
fig.text(0, 1, f'a)', fontsize=15, fontweight='bold', va='top', ha='left')
plt.grid(True)


plt.subplot(5, 1, 2)
df = df.sort_values('Time')
plt.plot(df['Time'], df['SPO2'], label='SPO2', color='orange',linewidth=0.8)
plt.ylabel('SPO2 (%)')
fig.text(0, 0.8, f'b)', fontsize=15, fontweight='bold', va='top', ha='left')
plt.grid(True)


plt.subplot(5, 1, 3)
df = df.sort_values('Time')
plt.plot(df['Time'], df['Heart rate'], label='Heart rate', color='green',linewidth=0.8)
plt.ylabel('Heart rate')
fig.text(0, 0.6, f'c)', fontsize=15, fontweight='bold', va='top', ha='left')
plt.grid(True)


plt.subplot(5, 1, 4)
df = df.sort_values('Time')
plt.plot(df['Time'], df['Respiratory rate'], label='Respiratory rate', color='red',linewidth=0.8)
plt.ylabel('Respiratory rate')
fig.text(0, 0.4, f'd)', fontsize=15, fontweight='bold', va='top', ha='left')
plt.grid(True)


plt.subplot(5, 1, 5)
df = df.sort_values('Time')
plt.plot(df['Time'], df['O2'], label='O2', color='purple',linewidth=0.8)
plt.xlabel('Time')
plt.ylabel('O2 (%)')
fig.text(0, 0.2, f'e)', fontsize=15, fontweight='bold', va='top', ha='left')
plt.grid(True)


plt.tight_layout()
plt.show()
