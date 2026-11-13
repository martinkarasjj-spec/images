import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

d = json.load(open('series_data.json'))

C = {k: tuple(v/255 for v in val['color']) for k, val in d.items()}

fig, ax1 = plt.subplots(figsize=(16, 8.5), dpi=150)
fig.subplots_adjust(left=0.06, right=0.76, top=0.90, bottom=0.10)

axes = [ax1]
for i in range(4):
    axes.append(ax1.twinx())
ax2, ax3, ax4, ax5 = axes[1], axes[2], axes[3], axes[4]

offs = [0, 55, 110, 165, 220]
for ax, off in zip(axes, offs):
    ax.spines['right'].set_position(('outward', off))
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(False)

def plot_on(ax, key, label, linestyle, marker, ms):
    xs, ys = d[key]['xs'], d[key]['ys']
    ax.plot(xs, ys, color=C[key], linestyle=linestyle, marker=marker,
            markersize=ms, linewidth=2.2, markerfacecolor=C[key], label=label)
    ax.set_ylabel(label, color=C[key], fontsize=11)
    ax.tick_params(axis='y', colors=C[key])
    ax.spines['right'].set_color(C[key])

plot_on(ax1, 'implicit', '4. Strategic FDI Governance Discourse: Explicit + Implicit', '-', 's', 4)
plot_on(ax2, 'explicit', '3. Strategic FDI Governance Discourse: Explicit', '--', 'o', 4)
plot_on(ax3, 'ratio', '5. Strategic FDI Governance Discourse: Ratio', '-', '', 0)
plot_on(ax4, 'treaty', '1. Average Treaty Strength', '--', 's', 4)
plot_on(ax5, 'screening', '2. Number of Countries with Investment Screening Mechanism', '-', 'o', 4)

ax1.set_ylim(0, 40)
ax2.set_ylim(0, 12)
ax3.set_ylim(0.02, 0.06)
ax4.set_ylim(6.0, 3.0)
ax5.set_ylim(10, 45)

ax1.set_xlim(1991.5, 2025.5)
ax1.set_xticks(range(1992, 2026, 2))
ax1.set_xlabel('Year', fontsize=12)
ax1.grid(True, axis='x', linestyle=':', alpha=0.4)
ax1.spines['left'].set_color(C['implicit'])
ax1.tick_params(axis='y', colors=C['implicit'])
ax1.set_ylabel('4. Strategic FDI Governance Discourse: Explicit + Implicit', color=C['implicit'], fontsize=11)

h1, l1 = ax1.get_legend_handles_labels()
handles, labels = h1, l1
for ax in axes[1:]:
    hh, ll = ax.get_legend_handles_labels()
    handles += hh
    labels += ll
ax1.legend(handles, labels, loc='upper left', fontsize=9, framealpha=0.9)

ax1.set_title('Strategic FDI governance in the literature, 1992–2025\n(five series, shared year axis, one y-axis per series)',
              fontsize=13)

fig.savefig('combined_multiaxis.png', dpi=150, bbox_inches='tight')
print('saved combined_multiaxis.png')
