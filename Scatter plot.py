import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse


# 读取数据
df = pd.read_csv('./Code/0620b.csv')

# 3. 分阶段分析SPO2变化
def analyze_spo2_segments(df, altitude_column='Altitude'):
    altitude_levels = [4500, 5000, 5500, 6000, 6500, 7000, 7500]

    # 创建存储分段的列表
    segments = []

    for i in range(len(altitude_levels) - 1):
        lower = altitude_levels[i]
        upper = altitude_levels[i + 1]

        # 筛选该高度区间内的数据
        segment = df[(df[altitude_column] == lower)].copy()
        segment['segment'] = f"{lower}m"
        segments.append(segment)

    # 合并所有高度分段
    segmented_df = pd.concat(segments, ignore_index=True)

    return segmented_df

segmented_df = analyze_spo2_segments(df)

def draw_confidence_ellipse(x, y, ax, n_std=2.0, facealpha=0.12, edgealpha=0.9, **kwargs):
    """
    根据 (x,y) 的均值与协方差，在 ax 上绘制 n_std 标准差的置信椭圆。
    n_std=1/2/3 分别近似 68/95/99.7% 覆盖。
    """
    x = np.asarray(x)
    y = np.asarray(y)
    if x.size < 3 or y.size < 3:
        return  # 点太少不画
    # 均值与协方差
    cov = np.cov(x, y)
    vals, vecs = np.linalg.eigh(cov)           # 特征分解
    order = vals.argsort()[::-1]
    vals, vecs = vals[order], vecs[:, order]
    # 椭圆主轴角度（度）
    theta = np.degrees(np.arctan2(vecs[1, 0], vecs[0, 0]))
    # 宽高（2 * n_std * sqrt(特征值)）
    width, height = 2 * n_std * np.sqrt(vals)
    # 中心点
    mean_x, mean_y = x.mean(), y.mean()

    e = Ellipse((mean_x, mean_y), width=width, height=height, angle=theta,
                facecolor=kwargs.get('color', None), edgecolor=kwargs.get('color', None),
                lw=2, alpha=edgealpha)
    # 面填充用淡透明度
    if e.get_facecolor() is not None:
        fc = list(e.get_facecolor())
        fc[-1] = facealpha
        e.set_facecolor(tuple(fc))
    ax.add_patch(e)

fig, axes = plt.subplots(1, 1, figsize=(10, 6))

sample_rate = 0.5  # 只显示每段 25% 的点，让图更稀疏
factor = 'O2'       # 你当前只画 O2 vs SPO2

for segment in segmented_df['segment'].unique():
    seg = segmented_df[segmented_df['segment'] == segment]

    # —— 1) 稀疏可视化：只抽样一部分点来画散点 ——
    plot_seg = seg.sample(frac=sample_rate, random_state=42) if len(seg) > 4 else seg
    sc = axes.scatter(plot_seg[factor], plot_seg['SPO2'], alpha=0.5, s=12, label=segment)

    # # —— 2) 线性拟合（SPO2 ~ O2）作为趋势斜线（用全量 seg 拟合，稳定） ——
    # if len(seg) > 2:
    #     x = seg[factor].values
    #     y = seg['SPO2'].values
    #     coef = np.polyfit(x, y, 1)       # y = a*x + b
    #     fit = np.poly1d(coef)
    #     # 为了平滑，按 x 排序后连线
    #     xs = np.linspace(x.min(), x.max(), 100)
    #     axes.plot(xs, fit(xs), linestyle='--', linewidth=2, color=sc.get_facecolors()[0],
    #               label=f'{segment} fit (slope={coef[0]:.2f})')

    # —— 3) 置信椭圆（2σ，约 95% 覆盖）表示该类别范围 ——
    if len(seg) > 3:
        draw_confidence_ellipse(seg[factor], seg['SPO2'], axes, n_std=2.0,
                                color=sc.get_facecolors()[0])

axes.set_xlabel(factor)
axes.set_ylabel('SPO2 (%)')
axes.legend(ncol=2, fontsize=9)
axes.grid(True, alpha=0.3)
plt.savefig('Figure_6.png', dpi=300, bbox_inches='tight')
plt.tight_layout()
plt.show()