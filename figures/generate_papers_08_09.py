#!/usr/bin/env python3
"""Generate publication-grade figures for QONTOS Papers 08 and 09."""

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
    'axes.grid': True,
    'grid.alpha': 0.3,
})


def figure_08_quantum_algorithms():
    """Application benchmark staircase: resource requirements."""
    fig, ax = plt.subplots(figsize=(11, 7))

    benchmarks = [
        ('H$_2$', 2, 1e3, GREEN, 'Near-term\nclassically verifiable'),
        ('LiH', 6, 1e5, GREEN, 'Small molecule\nvalidation'),
        ('Small catalyst\n(active space)', 30, 1e8, '#FFB300', 'Intermediate\nmilestone'),
        ('P450 / Fe$_4$S$_4$\n(medium catalyst)', 100, 1e10, ORANGE, 'Application\nregime'),
        ('FeMoco\n(Reiher 2017)', 300, 1e14, RED, 'STRETCH:\nflagship application'),
    ]

    for label, qubits, tgates, color, annotation in benchmarks:
        ax.scatter(qubits, tgates, s=250, color=color, edgecolors=NAVY, linewidth=1.5, zorder=5)
        ax.text(qubits * 1.15, tgates * 1.5, label, fontsize=9, fontweight='bold',
                color=NAVY, va='bottom')
        ax.text(qubits * 1.15, tgates * 0.4, annotation, fontsize=7.5,
                color=MED_GRAY, style='italic', va='top')

    # Connect with line
    qubits_list = [b[1] for b in benchmarks]
    tgates_list = [b[2] for b in benchmarks]
    ax.plot(qubits_list, tgates_list, color=MED_GRAY, linewidth=1, linestyle='--', alpha=0.5, zorder=1)

    # Scenario bands (horizontal)
    ax.axhspan(1, 1e6, alpha=0.04, color=GREEN)
    ax.axhspan(1e6, 1e11, alpha=0.04, color=ORANGE)
    ax.axhspan(1e11, 1e16, alpha=0.04, color=RED)

    ax.text(1.5, 3e2, 'BASE scenario range', fontsize=8, color=GREEN, fontweight='bold')
    ax.text(1.5, 3e8, 'AGGRESSIVE scenario range', fontsize=8, color=ORANGE, fontweight='bold')
    ax.text(1.5, 3e13, 'STRETCH scenario range', fontsize=8, color=RED, fontweight='bold')

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Logical Qubits Required', fontsize=12, fontweight='bold')
    ax.set_ylabel('T-gate Count (approximate)', fontsize=12, fontweight='bold')
    ax.set_title('Application Benchmark Staircase: Resource Requirements',
                 fontsize=14, fontweight='bold', color=NAVY, pad=15)
    ax.set_xlim(1, 1000)
    ax.set_ylim(1e2, 1e16)

    # Citation box
    cite = ("Resource estimates from:\n"
            "Reiher et al. 2017 (PNAS), Lee et al. 2021 (PRX Quantum),\n"
            "Beverland et al. 2022 (arXiv:2211.07629)")
    ax.text(0.98, 0.02, cite, transform=ax.transAxes, fontsize=7.5,
            ha='right', va='bottom', color=MED_GRAY, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=LIGHT_GRAY, edgecolor=MED_GRAY))

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, '08_quantum_algorithms.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] 08_quantum_algorithms.png")


def figure_09_benchmarking():
    """Benchmark framework: evidence pyramid."""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(6, 9.5, 'QONTOS Benchmark Framework: Evidence Pyramid',
            fontsize=15, fontweight='bold', ha='center', color=NAVY)

    # Pyramid layers (bottom to top)
    layers = [
        (0, 'L0: Device Metrics', 'T1, T2, gate fidelity, readout fidelity, yield',
         'Direct measurement', 'Demonstrated / Simulated', BLUE, 10),
        (1, 'L1: Logical Metrics', 'Logical error rate, QEC cycle time, overhead ratio',
         'QEC benchmarks', 'Simulated / Target', TEAL, 8.2),
        (2, 'L2: System Metrics', 'Quantum Volume, CLOPS, inter-module fidelity, Bell pair rate',
         'System benchmarks', 'Simulated / Target', GREEN, 6.4),
        (3, 'L3: Application Metrics', 'VQE accuracy, QAOA quality, chemistry benchmark ladder',
         'Application benchmarks', 'Target / Stretch', ORANGE, 4.6),
        (4, 'L4: Release Gates', 'Pass/fail thresholds for public claims and roadmap promotion',
         'CI + evidence board', 'Gate decision', RED, 2.8),
    ]

    for i, (idx, title, metrics, method, claim, color, width) in enumerate(layers):
        y = 1.0 + i * 1.55
        x_center = 6
        x_left = x_center - width / 2
        h = 1.3

        # Trapezoid approximation using polygon
        next_width = layers[i + 1][6] if i < len(layers) - 1 else width * 0.6
        pts = np.array([
            [x_center - width/2, y],
            [x_center + width/2, y],
            [x_center + next_width/2, y + h],
            [x_center - next_width/2, y + h],
        ])
        polygon = plt.Polygon(pts, facecolor=color, edgecolor=NAVY, linewidth=1.5, alpha=0.15)
        ax.add_patch(polygon)
        border = plt.Polygon(pts, facecolor='none', edgecolor=color, linewidth=2)
        ax.add_patch(border)

        # Text
        ax.text(x_center, y + h * 0.7, title, ha='center', va='center',
                fontsize=10, fontweight='bold', color=NAVY)
        ax.text(x_center, y + h * 0.38, metrics, ha='center', va='center',
                fontsize=8, color=MED_GRAY)
        ax.text(x_center, y + h * 0.12, f'Method: {method}  |  Claim: {claim}',
                ha='center', va='center', fontsize=7, color=color, style='italic')

    # Maturity levels sidebar
    ax.text(11.5, 8.5, 'Maturity\nLevels', fontsize=10, fontweight='bold',
            ha='center', color=NAVY)
    maturity = [
        ('M0', 'Concept', MED_GRAY),
        ('M1', 'Prototype', BLUE),
        ('M2', 'Validated', TEAL),
        ('M3', 'Reproducible', GREEN),
        ('M4', 'CI-gated', ORANGE),
        ('M5', 'Production', RED),
    ]
    for j, (level, desc, color) in enumerate(maturity):
        y_m = 7.5 - j * 0.65
        ax.text(11.0, y_m, level, fontsize=9, fontweight='bold', color=color)
        ax.text(11.5, y_m, desc, fontsize=8, color=MED_GRAY)

    fig.savefig(os.path.join(OUT, '09_benchmarking.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] 09_benchmarking.png")


if __name__ == '__main__':
    print(f"Output: {OUT}\n")
    figure_08_quantum_algorithms()
    figure_09_benchmarking()
    print("\nDone - Papers 08-09 figures generated.")
