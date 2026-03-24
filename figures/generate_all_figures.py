#!/usr/bin/env python3
"""
QONTOS Research Papers — Publication-Grade Figure Generator
Generates all 4 figures for Papers 01 and 02 at 300 DPI.
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# Output directory
OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)

# ─── QONTOS Brand Palette ───
NAVY      = '#0A1628'
BLUE      = '#1E88E5'
TEAL      = '#00BCD4'
ORANGE    = '#FF6F00'
GREEN     = '#4CAF50'
RED       = '#E53935'
LIGHT_GRAY= '#F5F5F5'
MED_GRAY  = '#9E9E9E'
WHITE     = '#FFFFFF'

# ─── Global rcParams ───
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Helvetica', 'Arial', 'DejaVu Sans'],
    'axes.facecolor': WHITE,
    'figure.facecolor': WHITE,
    'text.color': NAVY,
    'axes.labelcolor': NAVY,
    'xtick.color': NAVY,
    'ytick.color': NAVY,
    'axes.edgecolor': MED_GRAY,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'grid.color': '#E0E0E0',
    'grid.linewidth': 0.5,
    'grid.alpha': 0.7,
})


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 1: 01_complete_architecture.png
# ═══════════════════════════════════════════════════════════════════════════════
def figure_01_architecture():
    fig, ax = plt.subplots(figsize=(14, 8.5))
    ax.set_xlim(0, 14)
    ax.set_ylim(-0.2, 8.8)
    ax.axis('off')

    # Title
    ax.text(7, 8.45, 'QONTOS Four-Tier Modular Architecture',
            fontsize=19, fontweight='bold', ha='center', va='top', color=NAVY)
    ax.plot([2.5, 11.5], [8.12, 8.12], color=TEAL, lw=1.5, alpha=0.6)

    # Tier data (top-to-bottom: largest first)
    tiers = [
        {'name': 'Tier 4: Data Center', 'mult': '10 Systems',
         'phys': '1,000,000', 'logical': '10,000', 'color': NAVY},
        {'name': 'Tier 3: System', 'mult': '10 Modules',
         'phys': '100,000', 'logical': '1,000', 'color': BLUE},
        {'name': 'Tier 2: Module', 'mult': '5 Chiplets',
         'phys': '10,000', 'logical': '100', 'color': TEAL},
        {'name': 'Tier 1: Chiplet', 'mult': 'Base Unit',
         'phys': '2,000', 'logical': '20', 'color': GREEN},
    ]

    y_positions = [1.2, 2.9, 4.6, 6.3]
    widths      = [12.4, 10.0, 7.6, 5.2]
    height      = 1.25

    for tier, y, w in zip(tiers, y_positions, widths):
        x = 7 - w / 2
        rect = FancyBboxPatch(
            (x, y), w, height,
            boxstyle="round,pad=0.08",
            facecolor=tier['color'], edgecolor='white',
            linewidth=2.5, alpha=0.93, zorder=3)
        ax.add_patch(rect)

        # Tier name + composition
        ax.text(x + 0.45, y + height/2 + 0.18, tier['name'],
                fontsize=12.5, fontweight='bold', ha='left', va='center', color='white', zorder=4)
        ax.text(x + 0.45, y + height/2 - 0.18, tier['mult'],
                fontsize=9.5, ha='left', va='center', color='white', alpha=0.78, zorder=4)

        # Physical qubits (center)
        ax.text(7, y + height/2 + 0.18, tier['phys'],
                fontsize=16, fontweight='bold', ha='center', va='center', color='white', zorder=4)
        ax.text(7, y + height/2 - 0.22, 'physical qubits',
                fontsize=8.5, ha='center', va='center', color='white', alpha=0.75, zorder=4)

        # Logical qubits (right)
        ax.text(x + w - 0.45, y + height/2 + 0.18, tier['logical'],
                fontsize=16, fontweight='bold', ha='right', va='center', color='white', zorder=4)
        ax.text(x + w - 0.45, y + height/2 - 0.22, 'logical qubits',
                fontsize=8.5, ha='right', va='center', color='white', alpha=0.75, zorder=4)

    # Connecting arrows with multiplier labels
    mults = ['\u00d710', '\u00d710', '\u00d75']
    for i in range(3):
        y_start = y_positions[i] + height
        y_end   = y_positions[i + 1]
        mid_y   = (y_start + y_end) / 2
        ax.annotate('', xy=(7, y_end - 0.02), xytext=(7, y_start + 0.02),
                    arrowprops=dict(arrowstyle='-|>', color=MED_GRAY,
                                    lw=1.8, mutation_scale=14), zorder=2)
        ax.text(7.55, mid_y, mults[i], fontsize=10, fontweight='bold',
                ha='left', va='center', color=MED_GRAY, fontstyle='italic')

    # Column headers
    for x_pos, label in [(3.2, 'COMPOSITION'), (7, 'PHYSICAL QUBITS'), (10.8, 'LOGICAL QUBITS')]:
        ax.text(x_pos, 7.82, label, fontsize=8.5, fontweight='bold',
                ha='center', va='center', color=MED_GRAY,
                fontstyle='italic')

    # Footnote box
    note = 'Logical qubit counts assume stretch-case 100:1 overhead  (physical \u2192 logical)'
    ax.text(7, 0.45, note, fontsize=9.5, ha='center', va='center', color=NAVY,
            fontstyle='italic',
            bbox=dict(boxstyle='round,pad=0.35', facecolor=LIGHT_GRAY,
                      edgecolor=MED_GRAY, alpha=0.6, linewidth=0.8))

    fig.savefig(os.path.join(OUT, '01_complete_architecture.png'),
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print("  [OK] 01_complete_architecture.png")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 2: 01_scaling_timeline.png
# ═══════════════════════════════════════════════════════════════════════════════
def figure_02_scaling():
    fig, ax = plt.subplots(figsize=(13, 7))

    phases = ['Foundation\n2025-26', 'Sputnik\n2026-27', 'Pioneer\n2027-28',
              'Horizon\n2028-29', 'Summit\n2029-30']
    x = np.arange(len(phases))

    base       = [100, 2_500,  20_000,   50_000,   100_000]
    aggressive = [100, 10_000, 100_000,  200_000,   500_000]
    stretch    = [100, 10_000, 100_000,  500_000, 1_000_000]

    # Shaded bands
    ax.fill_between(x, base, aggressive, alpha=0.10, color=BLUE, zorder=1)
    ax.fill_between(x, aggressive, stretch, alpha=0.08, color=ORANGE, zorder=1)

    # Lines
    ax.plot(x, stretch, 'o-', color=ORANGE, lw=2.8, markersize=9,
            label='Stretch', zorder=5, markeredgecolor='white', markeredgewidth=1.5)
    ax.plot(x, aggressive, 's-', color=BLUE, lw=2.8, markersize=9,
            label='Aggressive', zorder=5, markeredgecolor='white', markeredgewidth=1.5)
    ax.plot(x, base, 'D-', color=GREEN, lw=2.8, markersize=8,
            label='Base', zorder=5, markeredgecolor='white', markeredgewidth=1.5)

    # Data labels
    for xi, b, a, s in zip(x, base, aggressive, stretch):
        offset_y = 1.25  # multiplicative in log space
        ax.text(xi, s * 1.35, f'{s:,}', fontsize=8, ha='center', va='bottom',
                color=ORANGE, fontweight='bold')
        if a != s:
            ax.text(xi + 0.12, a * 0.68, f'{a:,}', fontsize=8, ha='left', va='top',
                    color=BLUE, fontweight='bold')
        if b != a:
            ax.text(xi, b * 0.62, f'{b:,}', fontsize=8, ha='center', va='top',
                    color=GREEN, fontweight='bold')

    # Validation gates
    for xi in x[1:]:
        ax.axvline(xi - 0.5, color=MED_GRAY, ls='--', lw=0.8, alpha=0.5, zorder=0)
    ax.text(0.5, 60, 'Validation\nGate', fontsize=7, ha='center', va='top',
            color=MED_GRAY, fontstyle='italic')

    ax.set_yscale('log')
    ax.set_xticks(x)
    ax.set_xticklabels(phases, fontsize=11, fontweight='bold')
    ax.set_ylabel('Physical Qubits', fontsize=13, fontweight='bold')
    ax.set_title('QONTOS Scaling Roadmap: Base / Aggressive / Stretch Scenarios',
                 fontsize=16, fontweight='bold', pad=18, color=NAVY)

    ax.set_ylim(50, 3_000_000)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(
        lambda val, pos: f'{int(val):,}' if val >= 1 else str(val)))
    ax.grid(axis='y', alpha=0.35, zorder=0)
    ax.grid(axis='x', alpha=0.0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    leg = ax.legend(fontsize=11, loc='upper left', frameon=True,
                    fancybox=True, framealpha=0.9, edgecolor=MED_GRAY)
    leg.get_frame().set_linewidth(0.6)

    fig.savefig(os.path.join(OUT, '01_scaling_timeline.png'),
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print("  [OK] 01_scaling_timeline.png")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 3: 02_qubit_physics.png
# ═══════════════════════════════════════════════════════════════════════════════
def figure_03_coherence():
    fig, ax = plt.subplots(figsize=(12, 6.5))

    entries = [
        {'label': 'Pre-Ta era (Nb/Al)\n~2020',           'T1': 75,   'color': BLUE,  'citation': 'Conventional Nb/Al transmon baseline'},
        {'label': 'Place et al. 2021\nTa on sapphire',   'T1': 300,  'color': BLUE,  'citation': 'Nat. Commun. 12, 1779 (2021)'},
        {'label': 'Wang et al. 2022\nTa with dry etch',  'T1': 500,  'color': BLUE,  'citation': 'npj Quantum Inf. 8, 3 (2022)'},
        {'label': 'Bland et al. 2025\nTa on HR-Si',      'T1': 1680, 'color': BLUE,  'citation': 'Preprint, arXiv:2501.xxxxx (2025)'},
        {'label': 'QONTOS Target\nStretch goal',         'T1': 2000, 'color': ORANGE, 'citation': 'QONTOS internal roadmap'},
    ]

    y_pos = np.arange(len(entries))
    bar_heights = [e['T1'] for e in entries]
    colors = [e['color'] for e in entries]

    bars = ax.barh(y_pos, bar_heights, height=0.62, color=colors, alpha=0.88,
                   edgecolor='white', linewidth=1.5, zorder=3)

    # Dashed border for QONTOS target
    bars[-1].set_edgecolor(ORANGE)
    bars[-1].set_linestyle('--')
    bars[-1].set_linewidth(2.2)
    bars[-1].set_alpha(0.35)

    # Overlay a dashed-edge rectangle for the target bar
    ax.barh(y_pos[-1], bar_heights[-1], height=0.62, color='none',
            edgecolor=ORANGE, linewidth=2.5, linestyle='--', zorder=4)

    # Labels
    ax.set_yticks(y_pos)
    ax.set_yticklabels([e['label'] for e in entries], fontsize=10.5, fontweight='bold')

    # Value annotations
    for i, e in enumerate(entries):
        suffix = ' \u03bcs' if e['T1'] < 2000 else ' \u03bcs (TARGET)'
        ax.text(e['T1'] + 25, i + 0.0, f"{e['T1']:,}{suffix}",
                fontsize=10.5, fontweight='bold', va='center', color=e['color'])
        # Citation below bar
        ax.text(e['T1'] + 25, i - 0.25, e['citation'],
                fontsize=7.5, va='center', color=MED_GRAY, fontstyle='italic')

    # 1 ms threshold line
    ax.axvline(1000, color=RED, ls='-', lw=1.8, alpha=0.7, zorder=2)
    ax.text(1010, len(entries) - 0.2, '1 ms', fontsize=9.5, fontweight='bold',
            color=RED, va='bottom', ha='left')
    ax.text(1010, len(entries) - 0.55, 'Fault-tolerance\nthreshold regime',
            fontsize=8, color=RED, alpha=0.8, va='bottom', ha='left', fontstyle='italic')

    ax.set_xlabel('Coherence Time T\u2081 (\u03bcs)', fontsize=13, fontweight='bold')
    ax.set_title('Tantalum-on-Silicon Transmon Qubit: Coherence Progress',
                 fontsize=16, fontweight='bold', pad=16, color=NAVY)
    ax.set_xlim(0, 2650)
    ax.grid(axis='x', alpha=0.3, zorder=0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.invert_yaxis()

    fig.savefig(os.path.join(OUT, '02_qubit_physics.png'),
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print("  [OK] 02_qubit_physics.png")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 4: 02_materials_comparison.png
# ═══════════════════════════════════════════════════════════════════════════════
def figure_04_operations_budget():
    fig, ax = plt.subplots(figsize=(13, 7))

    # Data: qubit platform, T1 (us), gate time (ns), raw slots, QEC d=7, QEC d=15
    gate_time_ns = 25  # Single-qubit gate time
    platforms = [
        'Pre-Ta\n(Nb/Al, ~2020)',
        'Place et al.\n2021',
        'Wang et al.\n2022',
        'Bland et al.\n2025',
        'QONTOS\nTarget',
    ]
    T1_values = [75, 300, 500, 1680, 2000]  # microseconds
    raw_slots = [t1 * 1000 / gate_time_ns for t1 in T1_values]  # T1/gate_time

    # QEC overhead estimates (distance d surface code)
    # Logical cycle ~ d * gate_time, so logical ops ~ T1 / (d * gate_time)
    # For d=7:  logical_ops = T1 / (7 * gate_time)
    # For d=15: logical_ops = T1 / (15 * gate_time)
    d7_ops  = [t1 * 1000 / (7 * gate_time_ns)  for t1 in T1_values]
    d15_ops = [t1 * 1000 / (15 * gate_time_ns) for t1 in T1_values]

    x = np.arange(len(platforms))
    width = 0.25

    bars1 = ax.bar(x - width, raw_slots, width, label=f'Raw gate slots (T\u2081 / {gate_time_ns}ns)',
                   color=BLUE, alpha=0.88, edgecolor='white', linewidth=1.2, zorder=3)
    bars2 = ax.bar(x,         d7_ops, width, label='After QEC overhead (d = 7)',
                   color=TEAL, alpha=0.88, edgecolor='white', linewidth=1.2, zorder=3)
    bars3 = ax.bar(x + width, d15_ops, width, label='After QEC overhead (d = 15)',
                   color=ORANGE, alpha=0.88, edgecolor='white', linewidth=1.2, zorder=3)

    # Value labels on bars
    def label_bar(bars, color, fontsize=8):
        for bar in bars:
            h = bar.get_height()
            if h > 0:
                lbl = f'{int(h):,}'
                ax.text(bar.get_x() + bar.get_width()/2, h * 1.05, lbl,
                        fontsize=fontsize, fontweight='bold', ha='center', va='bottom',
                        color=color, rotation=0)

    label_bar(bars1, BLUE, 8)
    label_bar(bars2, TEAL, 8)
    label_bar(bars3, ORANGE, 8)

    # Annotate the reduction
    # Arrow from raw to d=15 for Bland
    idx = 3  # Bland
    ax.annotate('',
                xy=(x[idx] + width, d15_ops[idx] + 800),
                xytext=(x[idx] - width, raw_slots[idx] * 0.7),
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.5, connectionstyle='arc3,rad=-0.2'))
    ax.text(x[idx] + 0.55, raw_slots[idx] * 0.35,
            f'\u223c{int(raw_slots[idx] / d15_ops[idx])}\u00d7 reduction\nfrom raw to d=15',
            fontsize=8.5, color=RED, fontweight='bold', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='white', edgecolor=RED, alpha=0.85, lw=0.8))

    ax.set_xticks(x)
    ax.set_xticklabels(platforms, fontsize=10.5, fontweight='bold')
    ax.set_ylabel('Number of Operations', fontsize=13, fontweight='bold')
    ax.set_title('Physical Qubit Operations Budget: Raw vs. Logical Depth',
                 fontsize=16, fontweight='bold', pad=18, color=NAVY)

    ax.set_yscale('log')
    ax.set_ylim(100, 200_000)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(
        lambda val, pos: f'{int(val):,}' if val >= 1 else str(val)))
    ax.grid(axis='y', alpha=0.3, zorder=0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    leg = ax.legend(fontsize=10.5, loc='upper left', frameon=True,
                    fancybox=True, framealpha=0.92, edgecolor=MED_GRAY)
    leg.get_frame().set_linewidth(0.6)

    # Explanatory note
    note = ('Raw gate slots \u2260 useful logical depth.  '
            'Surface-code QEC at distance d requires ~d syndrome rounds per logical gate,\n'
            'reducing usable operations by the code distance.  '
            'Gate time = 25 ns (single-qubit).  T\u2081 values from published literature.')
    ax.text(0.5, -0.14, note, fontsize=8.5, ha='center', va='top',
            transform=ax.transAxes, color=MED_GRAY, fontstyle='italic')

    fig.savefig(os.path.join(OUT, '02_materials_comparison.png'),
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print("  [OK] 02_materials_comparison.png")


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print(f"Output directory: {OUT}\n")
    print("Generating figures ...")
    figure_01_architecture()
    figure_02_scaling()
    figure_03_coherence()
    figure_04_operations_budget()
    print("\nAll figures generated. Verifying files ...")
    expected = [
        '01_complete_architecture.png',
        '01_scaling_timeline.png',
        '02_qubit_physics.png',
        '02_materials_comparison.png',
    ]
    for f in expected:
        path = os.path.join(OUT, f)
        if os.path.isfile(path):
            size_kb = os.path.getsize(path) / 1024
            print(f"  \u2713 {f}  ({size_kb:.0f} KB)")
        else:
            print(f"  \u2717 {f}  MISSING!")
    print("\nDone.")
