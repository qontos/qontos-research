#!/usr/bin/env python3
"""Generate publication-grade figures for QONTOS Papers 00 (Executive Summary) and 10 (Roadmap)."""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = os.path.dirname(os.path.abspath(__file__))

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
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.edgecolor': MED_GRAY,
})


def figure_00_executive_summary():
    """Full-stack modular quantum computing platform overview."""
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    ax.text(7, 7.6, 'QONTOS: Full-Stack Modular Quantum Computing Platform',
            fontsize=16, fontweight='bold', ha='center', color=NAVY)

    # Three columns
    columns = [
        (2.3, 'OPEN TODAY', GREEN, [
            'SDK & Orchestration',
            'Simulators & Digital Twin',
            'Benchmark Framework',
            'Research & Whitepapers',
            'Examples & Tutorials',
        ]),
        (7, 'IN DEVELOPMENT', ORANGE, [
            'Native Modular Hardware',
            'Pulse & Control Stack',
            'Photonic Interconnects',
            'Cryogenic Infrastructure',
            'FTQC & Decoder Stack',
        ]),
        (11.7, 'STRETCH 2030', RED, [
            '1,000,000 Physical Qubits',
            '10,000 Logical Qubits',
            '100:1 Effective Overhead',
            'FeMoco-Class Chemistry',
            'Quantum Advantage',
        ]),
    ]

    for x_center, title, color, items in columns:
        # Header
        header_box = FancyBboxPatch((x_center - 2, 6.5), 4, 0.7,
                                    boxstyle="round,pad=0.15",
                                    facecolor=color, edgecolor=color,
                                    linewidth=2, alpha=0.2)
        ax.add_patch(header_box)
        ax.text(x_center, 6.85, title, ha='center', va='center',
                fontsize=12, fontweight='bold', color=color)

        # Items
        for i, item in enumerate(items):
            y = 5.8 - i * 0.75
            item_box = FancyBboxPatch((x_center - 1.8, y - 0.25), 3.6, 0.55,
                                      boxstyle="round,pad=0.1",
                                      facecolor=LIGHT_GRAY, edgecolor=color,
                                      linewidth=1.2, alpha=0.5)
            ax.add_patch(item_box)
            ax.text(x_center, y, item, ha='center', va='center',
                    fontsize=9, color=NAVY)

    # Arrows between columns
    for x in [4.5, 9.2]:
        ax.annotate('', xy=(x + 0.4, 5.0), xytext=(x - 0.4, 5.0),
                    arrowprops=dict(arrowstyle='->', color=MED_GRAY,
                                    linewidth=2.5, mutation_scale=20))

    # Architecture mini-diagram at bottom
    y_arch = 1.2
    ax.text(7, 2.1, 'Canonical Architecture Hierarchy', fontsize=11,
            fontweight='bold', ha='center', color=NAVY)

    arch = [
        ('Chiplet\n2,000 qubits', 2.5, 1.5, GREEN),
        ('Module\n10,000 qubits', 5.0, 2.0, TEAL),
        ('System\n100,000 qubits', 7.8, 2.5, BLUE),
        ('Data Center\n1,000,000 qubits', 10.8, 3.0, NAVY),
    ]
    for label, x, w, color in arch:
        box = FancyBboxPatch((x - w/2, y_arch - 0.3), w, 0.6,
                             boxstyle="round,pad=0.08",
                             facecolor=color, edgecolor=color,
                             linewidth=1.5, alpha=0.15)
        ax.add_patch(box)
        border = FancyBboxPatch((x - w/2, y_arch - 0.3), w, 0.6,
                                boxstyle="round,pad=0.08",
                                facecolor='none', edgecolor=color, linewidth=1.5)
        ax.add_patch(border)
        ax.text(x, y_arch, label, ha='center', va='center',
                fontsize=7.5, fontweight='bold', color=NAVY)

    # Arrows between arch boxes
    for x1, x2 in [(3.25, 4.0), (6.0, 6.55), (9.05, 9.3)]:
        ax.annotate('', xy=(x2, y_arch), xytext=(x1, y_arch),
                    arrowprops=dict(arrowstyle='->', color=MED_GRAY, linewidth=1.5))

    # Claim label legend
    ax.text(7, 0.3, 'Claim Labels:  Demonstrated  |  Simulated  |  '
            'Derived from literature  |  QONTOS target  |  Stretch target',
            ha='center', fontsize=8.5, color=MED_GRAY,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=LIGHT_GRAY, edgecolor=MED_GRAY))

    fig.savefig(os.path.join(OUT, '00_executive_summary.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] 00_executive_summary.png")


def figure_10_roadmap():
    """Gated development roadmap through 2030."""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')

    ax.text(7, 8.6, 'QONTOS Gated Development Roadmap Through 2030',
            fontsize=15, fontweight='bold', ha='center', color=NAVY)
    ax.text(7, 8.25, 'Each phase is contingent on passing explicit validation gates',
            fontsize=9, ha='center', color=MED_GRAY, style='italic')

    phases = [
        ('FOUNDATION', '2025-26', 1.5, 'T1 > 500 us\nat scale'),
        ('SPUTNIK', '2026-27', 4.0, 'First 100\nlogical qubits'),
        ('PIONEER', '2027-28', 6.5, 'Multi-module\ndistributed QEC'),
        ('HORIZON', '2028-29', 9.0, 'Overhead\n< 300:1'),
        ('SUMMIT', '2029-30', 11.5, 'All subsystems\nat stretch'),
    ]

    scenarios = [
        ('Base', GREEN, 6.5),
        ('Aggressive', ORANGE, 5.2),
        ('Stretch', RED, 3.9),
    ]

    # Phase columns
    for name, years, x, gate_text in phases:
        # Phase header
        header = FancyBboxPatch((x - 1.0, 7.2), 2.0, 0.7,
                                boxstyle="round,pad=0.1",
                                facecolor=BLUE, edgecolor=NAVY,
                                linewidth=1.5, alpha=0.15)
        ax.add_patch(header)
        ax.text(x, 7.65, name, ha='center', va='center',
                fontsize=10, fontweight='bold', color=NAVY)
        ax.text(x, 7.35, years, ha='center', va='center',
                fontsize=8, color=MED_GRAY)

        # Scenario bars
        base_outcomes = {
            'FOUNDATION': ['Platform +\nbenchmarks', 'HW validation\npath', 'Stretch\nevidence'],
            'SPUTNIK': ['Small modular\nHW path', '10k-qubit\nmodule', 'Module\ntarget'],
            'PIONEER': ['Distributed\nruntime', 'Multi-module\ndemos', '100k qubit\npath'],
            'HORIZON': ['Modular\nplatform', '100k phys.\n100-1k log.', '500k phys.\n5k log.'],
            'SUMMIT': ['Commercial\nplatform', 'Large FT\nmachine', '1M phys.\n10k log.'],
        }

        for scenario_name, color, y in scenarios:
            idx = ['Base', 'Aggressive', 'Stretch'].index(scenario_name)
            outcome = base_outcomes[name][idx]
            box = FancyBboxPatch((x - 0.9, y - 0.4), 1.8, 0.9,
                                 boxstyle="round,pad=0.08",
                                 facecolor=color, edgecolor=color,
                                 linewidth=1.5, alpha=0.1)
            ax.add_patch(box)
            border = FancyBboxPatch((x - 0.9, y - 0.4), 1.8, 0.9,
                                    boxstyle="round,pad=0.08",
                                    facecolor='none', edgecolor=color, linewidth=1.5)
            ax.add_patch(border)
            ax.text(x, y + 0.05, outcome, ha='center', va='center',
                    fontsize=7, color=NAVY)

        # Gate diamond between phases (except after last)
        if name != 'SUMMIT':
            gx = x + 1.25
            diamond = plt.Polygon([(gx, 5.2), (gx + 0.2, 5.0), (gx, 4.8), (gx - 0.2, 5.0)],
                                  facecolor='#FFD600', edgecolor=NAVY, linewidth=1.5)
            ax.add_patch(diamond)
            ax.text(gx, 4.5, 'GATE', ha='center', fontsize=6.5,
                    fontweight='bold', color=NAVY)

    # Scenario labels on left
    for scenario_name, color, y in scenarios:
        ax.text(0.3, y + 0.05, scenario_name, fontsize=10, fontweight='bold',
                color=color, va='center')

    # Fallback note at bottom
    fallback_text = ("Fallback examples:  "
                     "Transduction < 5% --> cap at 50k qubits  |  "
                     "QEC overhead > 300:1 --> downgrade logical target  |  "
                     "Chiplet yield miss --> smaller module topology")
    ax.text(7, 2.8, fallback_text, ha='center', fontsize=8, color=MED_GRAY,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF3E0', edgecolor=ORANGE, linewidth=1))

    # Key milestones
    ax.text(7, 2.0, 'Key Decision Points', fontsize=11, fontweight='bold',
            ha='center', color=NAVY)
    milestones = [
        'Gate 1: Device coherence at scale',
        'Gate 2: First logical qubit milestone',
        'Gate 3: Multi-module QEC demonstrated',
        'Gate 4: Overhead below aggressive threshold',
        'Gate 5: All subsystems pass stretch criteria',
    ]
    for i, m in enumerate(milestones):
        ax.text(2 + (i % 3) * 4, 1.3 - (i // 3) * 0.4, m,
                fontsize=8, color=NAVY,
                bbox=dict(boxstyle='round,pad=0.15', facecolor=LIGHT_GRAY, edgecolor=MED_GRAY))

    fig.savefig(os.path.join(OUT, '10_roadmap_2030.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] 10_roadmap_2030.png")


def figure_10_risk_matrix():
    """Program risk matrix (bubble chart)."""
    fig, ax = plt.subplots(figsize=(10, 7))

    risks = [
        ('Qubit coherence\nat scale', 2.5, 3.5, 'Technical', 45),
        ('QEC overhead\nstalls', 2.5, 4.5, 'Technical', 55),
        ('Transduction\nefficiency', 3.5, 4.5, 'Technical', 60),
        ('Cryogenic\nscaling', 1.5, 3.5, 'Technical', 40),
        ('Decoder\nlatency', 2.5, 2.5, 'Technical', 35),
        ('Chiplet\nyield', 2.5, 3.0, 'Technical', 40),
        ('Supply\nchain', 1.5, 2.5, 'Programmatic', 30),
        ('Talent\nacquisition', 2.5, 2.0, 'Programmatic', 35),
        ('Capital\naccess', 1.5, 4.5, 'Programmatic', 50),
    ]

    for label, prob, impact, category, size in risks:
        color = BLUE if category == 'Technical' else ORANGE
        ax.scatter(impact, prob, s=size * 15, color=color, alpha=0.3, edgecolors=color, linewidth=2)
        ax.text(impact, prob, label, ha='center', va='center', fontsize=7.5,
                fontweight='bold', color=NAVY)

    ax.set_xlabel('Impact', fontsize=12, fontweight='bold')
    ax.set_ylabel('Probability', fontsize=12, fontweight='bold')
    ax.set_title('QONTOS Program Risk Matrix',
                 fontsize=14, fontweight='bold', color=NAVY, pad=15)
    ax.set_xlim(0.5, 5)
    ax.set_ylim(0.5, 5)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_xticklabels(['Low', 'Medium-Low', 'Medium', 'High', 'Critical'])
    ax.set_yticks([1, 2, 3, 4])
    ax.set_yticklabels(['Low', 'Medium', 'High', 'Very High'])

    # Quadrant shading
    ax.axhspan(3, 5, xmin=0.5, alpha=0.03, color=RED)
    ax.axvspan(3, 5, ymin=0.5, alpha=0.03, color=RED)

    # Legend
    legend_elements = [
        plt.scatter([], [], s=150, color=BLUE, alpha=0.3, edgecolors=BLUE, linewidth=2, label='Technical'),
        plt.scatter([], [], s=150, color=ORANGE, alpha=0.3, edgecolors=ORANGE, linewidth=2, label='Programmatic'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9, framealpha=0.9)

    ax.text(0.02, 0.02, 'Bubble size indicates relative program exposure',
            transform=ax.transAxes, fontsize=8, color=MED_GRAY, style='italic')

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, '10_risk_matrix.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] 10_risk_matrix.png")


if __name__ == '__main__':
    print(f"Output: {OUT}\n")
    figure_00_executive_summary()
    figure_10_roadmap()
    figure_10_risk_matrix()
    print("\nDone - Papers 00 & 10 figures generated.")
