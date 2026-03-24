#!/usr/bin/env python3
"""Generate publication-grade figures for QONTOS Papers 03 and 04."""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import LogLocator, LogFormatterSciNotation

OUT = os.path.dirname(os.path.abspath(__file__))

# QONTOS Brand Palette
NAVY = '#0A1628'
BLUE = '#1E88E5'
TEAL = '#00BCD4'
ORANGE = '#FF6F00'
GREEN = '#4CAF50'
RED = '#E53935'
LIGHT_GRAY = '#F5F5F5'
MED_GRAY = '#9E9E9E'

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Arial', 'DejaVu Sans'],
    'axes.titlesize': 14,
    'axes.labelsize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.edgecolor': MED_GRAY,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.color': MED_GRAY,
})


def figure_03_error_correction():
    """Logical error rate vs physical error rate for surface code distances."""
    fig, ax = plt.subplots(figsize=(10, 7))

    p_th = 0.01  # 1% threshold
    p_phys = np.logspace(-4, -1.7, 300)  # 10^-4 to ~2%

    distances = [3, 5, 7, 9, 11, 13, 15]
    colors_d = ['#E53935', '#FF6F00', '#FFB300', '#4CAF50', '#00BCD4', '#1E88E5', '#5E35B1']

    for d, color in zip(distances, colors_d):
        p_L = 0.03 * (p_phys / p_th) ** ((d + 1) / 2)
        # Clip for display
        mask = p_L > 1e-18
        ax.plot(p_phys[mask], p_L[mask], color=color, linewidth=2, label=f'd = {d}')

    # Threshold line
    ax.axvline(x=p_th, color=RED, linestyle=':', linewidth=1.5, alpha=0.7)
    ax.text(p_th * 1.15, 1e-2, 'Threshold\np = 1%', fontsize=8, color=RED, va='top')

    # Current best regime
    ax.axvline(x=1e-3, color=BLUE, linestyle='--', linewidth=1.5, alpha=0.6)
    ax.text(1e-3 * 0.8, 1e-14, 'Current best\n2Q fidelity\nregime', fontsize=8,
            color=BLUE, ha='right', va='center')

    # QONTOS stretch target
    ax.axhline(y=1e-8, color=ORANGE, linestyle='--', linewidth=1.5, alpha=0.6)
    ax.text(2e-4, 2e-8, 'QONTOS stretch target (p_L = 10^{-8})', fontsize=8,
            color=ORANGE, va='bottom')

    # Highlight the sweet spot
    rect = plt.Rectangle((5e-4, 1e-12), 3e-3 - 5e-4, 1e-6 - 1e-12,
                          facecolor=GREEN, alpha=0.08, edgecolor=GREEN, linewidth=1, linestyle='--')
    ax.add_patch(rect)
    ax.text(1.2e-3, 3e-10, 'Useful operating\nregime', fontsize=8, color=GREEN,
            ha='center', style='italic')

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Physical Error Rate (p)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Logical Error Rate (p_L)', fontsize=12, fontweight='bold')
    ax.set_title('Logical Error Rate vs. Physical Error Rate:\nSurface Code Distance Scaling',
                 fontsize=14, fontweight='bold', color=NAVY, pad=15)
    ax.set_xlim(1e-4, 2e-2)
    ax.set_ylim(1e-16, 1)
    ax.legend(title='Code Distance', loc='upper left', framealpha=0.9)

    # Formula annotation
    ax.text(0.98, 0.02, r'$p_L \approx 0.03 \times (p / p_{th})^{(d+1)/2}$'
            '\n' r'$p_{th} \approx 1\%$ (surface code)',
            transform=ax.transAxes, fontsize=9, ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=LIGHT_GRAY, edgecolor=MED_GRAY))

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, '03_error_correction.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] 03_error_correction.png")


def figure_03_code_structures():
    """QEC overhead scenarios comparison."""
    fig, ax = plt.subplots(figsize=(10, 6.5))

    categories = [
        'Surface Code\n(d=15, conservative)',
        'Surface Code\n(d=7, reduced)',
        'qLDPC [[144,12,12]]\n(theoretical)',
        'QONTOS Hybrid\n(stretch target)'
    ]
    overheads = [450, 100, 12, 100]
    colors = [BLUE, TEAL, GREEN, ORANGE]
    edge_styles = ['solid', 'solid', 'solid', 'dashed']

    bars = ax.barh(categories, overheads, color=colors, edgecolor=[NAVY]*3 + [ORANGE],
                   linewidth=[1.5]*3 + [2.5], height=0.6)

    # Make the stretch target bar have dashed edge
    bars[3].set_linestyle('--')

    # Add value labels
    for bar, val, cat in zip(bars, overheads, categories):
        label = f'{val}:1'
        if 'stretch' in cat.lower():
            label += ' (STRETCH TARGET)'
        ax.text(bar.get_width() + 8, bar.get_y() + bar.get_height()/2,
                label, va='center', fontsize=10, fontweight='bold', color=NAVY)

    # Scenario reference lines
    scenarios = [
        (1000, 'Conservative\n(1000:1)', RED, ':'),
        (300, 'Aggressive\n(300:1)', ORANGE, '--'),
        (100, 'Stretch\n(100:1)', GREEN, '--'),
    ]
    for val, label, color, ls in scenarios:
        ax.axvline(x=val, color=color, linestyle=ls, linewidth=1.5, alpha=0.5)
        ax.text(val + 5, 3.7, label, fontsize=8, color=color, va='top')

    ax.set_xlabel('Physical : Logical Qubit Ratio', fontsize=12, fontweight='bold')
    ax.set_title('QEC Overhead Scenarios: Conservative / Aggressive / Stretch',
                 fontsize=14, fontweight='bold', color=NAVY, pad=15)
    ax.set_xlim(0, 1200)

    # Add notes
    notes = ("Note: qLDPC codes require 6+ connectivity (not available on all architectures).\n"
             "Surface code overheads include ancillas + routing. Hybrid combines qLDPC data + surface distillation.")
    ax.text(0.5, -0.12, notes, transform=ax.transAxes, fontsize=8,
            ha='center', color=MED_GRAY, style='italic')

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, '03_code_structures.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] 03_code_structures.png")


def figure_04_transduction():
    """End-to-end photonic link budget."""
    fig, ax = plt.subplots(figsize=(11, 7))

    # Link budget components (in dB loss)
    components = [
        'Microwave\ncoupling',
        'Electro-mech.\nconversion',
        'Mech.-optical\nconversion',
        'Fiber\ntransmission',
        'Optical\ndetection',
        'Heralding\noverhead'
    ]

    # Loss values for each scenario (in dB, negative = loss)
    stretch = [-0.5, -7.0, -3.0, -0.2, -1.0, -2.0]
    aggressive = [-1.0, -10.0, -5.0, -0.5, -1.5, -3.0]
    base = [-2.0, -15.0, -8.0, -1.0, -2.0, -5.0]
    research = [-3.0, -20.0, -12.0, -2.0, -3.0, -8.0]

    x = np.arange(len(components))
    width = 0.2

    bars1 = ax.bar(x - 1.5*width, [-v for v in research], width, label='Research (<1%)',
                   color=RED, alpha=0.8)
    bars2 = ax.bar(x - 0.5*width, [-v for v in base], width, label='Base (1-10%)',
                   color=ORANGE, alpha=0.8)
    bars3 = ax.bar(x + 0.5*width, [-v for v in aggressive], width, label='Aggressive (10-20%)',
                   color=TEAL, alpha=0.8)
    bars4 = ax.bar(x + 1.5*width, [-v for v in stretch], width, label='Stretch (>20%)',
                   color=GREEN, alpha=0.8)

    ax.set_ylabel('Signal Loss (dB)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Link Budget Component', fontsize=12, fontweight='bold')
    ax.set_title('End-to-End Photonic Link Budget:\nMicrowave-to-Optical Transduction',
                 fontsize=14, fontweight='bold', color=NAVY, pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(components, fontsize=9)
    ax.legend(title='Scenario Band', loc='upper left', framealpha=0.9)

    # Total efficiency annotations
    totals = {
        'Stretch': sum(stretch),
        'Aggressive': sum(aggressive),
        'Base': sum(base),
        'Research': sum(research)
    }
    eff_text = "Total end-to-end efficiency:\n"
    for name, db in totals.items():
        eff = 10 ** (db / 10) * 100
        eff_text += f"  {name}: {db:.1f} dB = {eff:.2f}%\n"

    ax.text(0.98, 0.98, eff_text.strip(), transform=ax.transAxes, fontsize=9,
            ha='right', va='top',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=LIGHT_GRAY, edgecolor=MED_GRAY))

    # Literature markers
    ax.text(0.02, 0.02,
            'Literature baselines: Mirhosseini 2020 (~10^-6 eff.), '
            'Delaney 2022 (~10^-4 eff.), Lecocq 2021 (~10^-3 eff.)',
            transform=ax.transAxes, fontsize=8, color=MED_GRAY, style='italic')

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, '04_transduction.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] 04_transduction.png")


if __name__ == '__main__':
    print(f"Output: {OUT}\n")
    figure_03_error_correction()
    figure_03_code_structures()
    figure_04_transduction()
    print("\nDone - Papers 03-04 figures generated.")
