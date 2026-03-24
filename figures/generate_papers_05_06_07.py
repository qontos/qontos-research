#!/usr/bin/env python3
"""Generate publication-grade figures for QONTOS Papers 05, 06, and 07."""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = os.path.dirname(os.path.abspath(__file__))

NAVY = '#0A1628'
BLUE = '#1E88E5'
TEAL = '#00BCD4'
ORANGE = '#FF6F00'
GREEN = '#4CAF50'
RED = '#E53935'
LIGHT_GRAY = '#F5F5F5'
MED_GRAY = '#9E9E9E'
WHITE = '#FFFFFF'

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Arial', 'DejaVu Sans'],
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.edgecolor': MED_GRAY,
})


def figure_05_ai_decoding():
    """Three-stage decoder pipeline architecture."""
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Title
    ax.text(7, 5.7, 'QONTOS Decoder Pipeline: Three-Stage Architecture',
            fontsize=15, fontweight='bold', ha='center', color=NAVY)
    ax.text(7, 5.35, 'Target: < 1 us end-to-end decoding latency',
            fontsize=10, ha='center', color=MED_GRAY, style='italic')

    # Input
    inp = FancyBboxPatch((0.3, 3.2), 1.8, 1.2, boxstyle="round,pad=0.15",
                         facecolor=LIGHT_GRAY, edgecolor=NAVY, linewidth=1.5)
    ax.add_patch(inp)
    ax.text(1.2, 3.95, 'Syndrome\nBits', ha='center', va='center', fontsize=9, fontweight='bold', color=NAVY)
    ax.text(1.2, 3.4, 'from QPU', ha='center', va='center', fontsize=7, color=MED_GRAY)

    # Stage boxes
    stages = [
        (2.8, 'Stage 1:\nCFE', 'Classical\nFront-End', '~100 ns', 'Pre-processing,\nsyndrome parsing', BLUE),
        (5.6, 'Stage 2:\nNAR', 'Neural Accelerated\nReasoner', '~200-500 ns', 'ML-based\ndecoding', TEAL),
        (8.4, 'Stage 3:\nCD', 'Correction\nDispatcher', '~50 ns', 'Lookup &\napplication', GREEN),
    ]

    for x, title, subtitle, timing, desc, color in stages:
        box = FancyBboxPatch((x, 2.5), 2.2, 2.2, boxstyle="round,pad=0.2",
                             facecolor=color, edgecolor=NAVY, linewidth=2, alpha=0.15)
        ax.add_patch(box)
        border = FancyBboxPatch((x, 2.5), 2.2, 2.2, boxstyle="round,pad=0.2",
                                facecolor='none', edgecolor=color, linewidth=2.5)
        ax.add_patch(border)
        ax.text(x + 1.1, 4.3, title, ha='center', va='center', fontsize=10,
                fontweight='bold', color=NAVY)
        ax.text(x + 1.1, 3.7, subtitle, ha='center', va='center', fontsize=8, color=color)
        ax.text(x + 1.1, 3.15, desc, ha='center', va='center', fontsize=7.5, color=MED_GRAY)
        # Timing badge
        badge = FancyBboxPatch((x + 0.35, 2.55), 1.5, 0.35, boxstyle="round,pad=0.1",
                               facecolor=color, edgecolor='none', alpha=0.2)
        ax.add_patch(badge)
        ax.text(x + 1.1, 2.72, timing, ha='center', va='center', fontsize=9,
                fontweight='bold', color=color)

    # Output
    out = FancyBboxPatch((11.2, 3.2), 2.2, 1.2, boxstyle="round,pad=0.15",
                         facecolor=LIGHT_GRAY, edgecolor=NAVY, linewidth=1.5)
    ax.add_patch(out)
    ax.text(12.3, 3.95, 'Pauli\nCorrections', ha='center', va='center', fontsize=9, fontweight='bold', color=NAVY)
    ax.text(12.3, 3.4, 'to QPU', ha='center', va='center', fontsize=7, color=MED_GRAY)

    # Arrows
    arrow_style = dict(arrowstyle='->', color=NAVY, linewidth=2, mutation_scale=15)
    for x1, x2 in [(2.1, 2.8), (5.0, 5.6), (7.8, 8.4), (10.6, 11.2)]:
        ax.annotate('', xy=(x2, 3.8), xytext=(x1, 3.8), arrowprops=arrow_style)

    # Data flow labels
    flow_labels = [
        (2.45, 'Raw\nsyndromes'),
        (5.3, 'Feature\nvectors'),
        (8.1, 'Correction\ntable'),
        (10.9, 'Pauli\nframes'),
    ]
    for x, label in flow_labels:
        ax.text(x, 4.55, label, ha='center', va='bottom', fontsize=6.5,
                color=MED_GRAY, style='italic')

    # Hardware targets
    hw_y = 1.5
    ax.text(7, hw_y + 0.5, 'Hardware Deployment Targets', fontsize=11,
            fontweight='bold', ha='center', color=NAVY)
    for x, label, color, status in [
        (3.5, 'FPGA\n(Near-term)', BLUE, 'Engineering target'),
        (7, 'ASIC\n(Scale)', TEAL, 'Stretch target'),
        (10.5, 'Integrated\n(Per-module)', ORANGE, 'Research direction'),
    ]:
        box = FancyBboxPatch((x - 1.2, hw_y - 0.6), 2.4, 0.9, boxstyle="round,pad=0.1",
                             facecolor=color, edgecolor=color, linewidth=1.5, alpha=0.12)
        ax.add_patch(box)
        ax.text(x, hw_y - 0.05, label, ha='center', va='center', fontsize=8,
                fontweight='bold', color=color)
        ax.text(x, hw_y - 0.5, status, ha='center', va='center', fontsize=7, color=MED_GRAY)

    # Total latency
    ax.text(7, 0.3, 'Total target latency: < 1 us  |  QEC cycle budget: 1-10 us',
            ha='center', fontsize=9, color=NAVY, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=BLUE, linewidth=1))

    fig.savefig(os.path.join(OUT, '05_ai_decoding.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] 05_ai_decoding.png")


def figure_06_software_stack():
    """QONTOS software architecture: current + future."""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(6, 9.7, 'QONTOS Software Architecture', fontsize=15,
            fontweight='bold', ha='center', color=NAVY)
    ax.text(6, 9.35, 'Green = Implemented today  |  Orange dashed = Target / In development',
            fontsize=9, ha='center', color=MED_GRAY)

    layers = [
        (8.2, 'User Applications', 'Chemistry, Optimization, Finance, ML',
         GREEN, 'solid', 0.08, 'IMPLEMENTED'),
        (7.0, 'QONTOS SDK', 'QontosClient, CircuitIR, async API, models',
         GREEN, 'solid', 0.12, 'IMPLEMENTED'),
        (5.6, 'Orchestration Pipeline',
         'Ingest  ->  Partition  ->  Schedule  ->  Execute  ->  Aggregate  ->  Verify',
         GREEN, 'solid', 0.12, 'IMPLEMENTED'),
        (4.2, 'Execution Layer', '', None, None, 0, ''),
        (2.8, 'Observability & Integrity',
         'Tracing, Metrics, Prometheus, SHA-256 Proof Chain',
         GREEN, 'solid', 0.1, 'IMPLEMENTED'),
        (1.4, 'Future Extensions',
         'Digital Twin, Modular Runtime, FT Compiler, Native Hardware Control',
         ORANGE, 'dashed', 0.08, 'TARGET'),
    ]

    for y, title, subtitle, color, style, alpha, status in layers:
        if color is None:
            continue
        ls = style if style else 'solid'
        lw = 2.5 if style == 'dashed' else 2
        box = FancyBboxPatch((0.5, y), 11, 0.9, boxstyle="round,pad=0.12",
                             facecolor=color if color else LIGHT_GRAY,
                             edgecolor=color if color else MED_GRAY,
                             linewidth=lw, alpha=alpha, linestyle=ls)
        ax.add_patch(box)
        border = FancyBboxPatch((0.5, y), 11, 0.9, boxstyle="round,pad=0.12",
                                facecolor='none', edgecolor=color,
                                linewidth=lw, linestyle=ls)
        ax.add_patch(border)
        ax.text(0.8, y + 0.6, title, fontsize=11, fontweight='bold', color=NAVY, va='center')
        ax.text(0.8, y + 0.25, subtitle, fontsize=8.5, color=MED_GRAY, va='center')
        ax.text(11.3, y + 0.45, status, fontsize=8, color=color, fontweight='bold',
                va='center', ha='right')

    # Execution layer (special - mixed)
    y_exec = 4.2
    box_bg = FancyBboxPatch((0.5, y_exec), 11, 0.9, boxstyle="round,pad=0.12",
                            facecolor=LIGHT_GRAY, edgecolor=MED_GRAY, linewidth=1, alpha=0.3)
    ax.add_patch(box_bg)
    ax.text(0.8, y_exec + 0.6, 'Execution Layer', fontsize=11, fontweight='bold',
            color=NAVY, va='center')

    # Sub-boxes for executors
    executors = [
        (1.2, 'Local\nSimulator', GREEN, 'solid'),
        (3.5, 'IBM\nQuantum', GREEN, 'solid'),
        (5.8, 'Amazon\nBraket', GREEN, 'solid'),
        (8.1, 'Native QONTOS\nHardware', ORANGE, 'dashed'),
    ]
    for x, label, color, ls in executors:
        lw = 2 if ls == 'dashed' else 1.5
        sub = FancyBboxPatch((x, y_exec + 0.08), 2.0, 0.55, boxstyle="round,pad=0.08",
                             facecolor=color, edgecolor=color, linewidth=lw,
                             alpha=0.12, linestyle=ls)
        ax.add_patch(sub)
        sub_border = FancyBboxPatch((x, y_exec + 0.08), 2.0, 0.55, boxstyle="round,pad=0.08",
                                    facecolor='none', edgecolor=color, linewidth=lw, linestyle=ls)
        ax.add_patch(sub_border)
        ax.text(x + 1.0, y_exec + 0.35, label, ha='center', va='center',
                fontsize=8, fontweight='bold', color=NAVY)

    # GitHub link
    ax.text(6, 0.6, 'github.com/qontos/qontos', fontsize=10, ha='center',
            color=BLUE, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=BLUE))

    fig.savefig(os.path.join(OUT, '06_software_stack.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] 06_software_stack.png")


def figure_07_cryogenic():
    """Multi-stage thermal budget for dilution refrigerator."""
    fig, ax = plt.subplots(figsize=(12, 7))

    stages = [
        ('300 K\n(Room temp)', 300, 'Control electronics\nClassical compute', 'N/A', '#E53935'),
        ('50 K\n(1st stage)', 50, 'Coax cables\nHigh-BW wiring', '~40 W', '#FF6F00'),
        ('4 K\n(2nd stage)', 4, 'HEMT amplifiers\nDC wiring', '~1.5 W', '#FFB300'),
        ('800 mK\n(Still)', 0.8, 'Filtering\nAttenuation', '~100 mW', '#4CAF50'),
        ('100 mK\n(Cold plate)', 0.1, 'Attenuators\nFilters', '~1 mW', '#00BCD4'),
        ('15 mK\n(MXC)', 0.015, 'QPU modules\nQuantum plane', '10-25 mW', '#1E88E5'),
    ]

    y_positions = np.arange(len(stages))
    temps = [s[1] for s in stages]
    colors = [s[4] for s in stages]

    # Horizontal bars (log-proportional width)
    log_temps = [np.log10(max(t, 0.01)) for t in temps]
    max_log = max(log_temps)
    bar_widths = [(lt - min(log_temps) + 0.5) / (max_log - min(log_temps) + 0.5) * 8
                  for lt in log_temps]

    for i, (stage_label, temp, components, cooling, color) in enumerate(stages):
        y = len(stages) - 1 - i
        w = bar_widths[i]
        bar = ax.barh(y, w, height=0.7, color=color, alpha=0.25, edgecolor=color, linewidth=2)
        ax.text(0.15, y, stage_label, va='center', fontsize=10, fontweight='bold', color=NAVY)
        ax.text(w + 0.2, y + 0.12, components, va='center', fontsize=8.5, color=MED_GRAY)
        ax.text(w + 0.2, y - 0.18, f'Cooling: {cooling}', va='center', fontsize=8,
                color=color, fontweight='bold')

    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_xlim(-0.5, 13)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set_facecolor('white')
    ax.grid(False)

    ax.set_title('Cryogenic Infrastructure: Multi-Stage Thermal Budget',
                 fontsize=14, fontweight='bold', color=NAVY, pad=15)

    # Scaling challenge annotation
    scaling_text = ("Scaling challenge: At 10 modules per system,\n"
                    "total 15 mK heat load = 100-250 mW\n"
                    "Current commercial DR capacity: 10-25 mW per unit")
    ax.text(9, 4.5, scaling_text, fontsize=9, color=RED,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFEBEE', edgecolor=RED, linewidth=1),
            ha='center', va='center')

    # Module count annotation
    module_text = ("QONTOS canonical: 5 chiplets/module\n"
                   "Each chiplet: 2,000 qubits at 15 mK\n"
                   "Per-module control lines: 2,000-3,000")
    ax.text(9, 2.0, module_text, fontsize=9, color=BLUE,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#E3F2FD', edgecolor=BLUE, linewidth=1),
            ha='center', va='center')

    # Temperature gradient arrow
    ax.annotate('', xy=(11.5, 5.2), xytext=(11.5, -0.2),
                arrowprops=dict(arrowstyle='->', color=MED_GRAY, linewidth=2))
    ax.text(11.8, 2.5, 'Cooling\nstages', fontsize=8, color=MED_GRAY,
            ha='left', va='center', rotation=0)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, '07_cryogenic.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] 07_cryogenic.png")


if __name__ == '__main__':
    print(f"Output: {OUT}\n")
    figure_05_ai_decoding()
    figure_06_software_stack()
    figure_07_cryogenic()
    print("\nDone - Papers 05-06-07 figures generated.")
