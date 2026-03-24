#!/usr/bin/env python3
"""Regenerate ALL 15 QONTOS figures with proper alignment, spacing, and font sizes."""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe

OUT = os.path.dirname(os.path.abspath(__file__))

# Brand palette
NAVY = '#0A1628'
BLUE = '#1E88E5'
TEAL = '#00BCD4'
ORANGE = '#FF6F00'
GREEN = '#4CAF50'
RED = '#E53935'
LGRAY = '#F5F5F5'
MGRAY = '#9E9E9E'
DGRAY = '#616161'

def _setup():
    plt.rcParams.update({
        'font.family': 'sans-serif',
        'font.sans-serif': ['Arial', 'DejaVu Sans', 'Helvetica Neue'],
        'figure.facecolor': 'white',
        'axes.facecolor': 'white',
        'axes.edgecolor': MGRAY,
        'axes.grid': True,
        'grid.alpha': 0.25,
        'grid.color': MGRAY,
        'axes.titlesize': 13,
        'axes.labelsize': 11,
        'xtick.labelsize': 9,
        'ytick.labelsize': 9,
    })

_setup()

def _save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=300, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    sz = os.path.getsize(path) // 1024
    print(f"  [OK] {name}  ({sz} KB)")


# =====================================================================
# PAPER 00: Executive Summary
# =====================================================================
def fig_00():
    fig, ax = plt.subplots(figsize=(16, 8.5))
    ax.set_xlim(0, 16); ax.set_ylim(0, 9); ax.axis('off')
    ax.text(8, 8.6, 'QONTOS: Full-Stack Modular Quantum Computing Platform',
            fontsize=17, fontweight='bold', ha='center', color=NAVY)

    cols = [
        (2.8, 'OPEN TODAY', GREEN,
         ['SDK & Orchestration', 'Simulators & Digital Twin',
          'Benchmark Framework', 'Research & Whitepapers', 'Examples & Tutorials']),
        (8.0, 'IN DEVELOPMENT', ORANGE,
         ['Native Modular Hardware', 'Pulse & Control Stack',
          'Photonic Interconnects', 'Cryogenic Infrastructure', 'FTQC & Decoder Stack']),
        (13.2, 'STRETCH 2030', RED,
         ['1,000,000 Physical Qubits', '10,000 Logical Qubits',
          '100:1 Effective Overhead', 'FeMoco-Class Chemistry', 'Quantum Advantage']),
    ]
    for xc, title, color, items in cols:
        hdr = FancyBboxPatch((xc-2.3, 7.3), 4.6, 0.8, boxstyle="round,pad=0.15",
                              facecolor=color, edgecolor=color, lw=2, alpha=0.18)
        ax.add_patch(hdr)
        ax.text(xc, 7.7, title, ha='center', va='center', fontsize=13, fontweight='bold', color=color)
        for i, item in enumerate(items):
            y = 6.4 - i * 0.85
            bx = FancyBboxPatch((xc-2.1, y-0.28), 4.2, 0.56, boxstyle="round,pad=0.1",
                                 facecolor=LGRAY, edgecolor=color, lw=1.2, alpha=0.6)
            ax.add_patch(bx)
            ax.text(xc, y, item, ha='center', va='center', fontsize=10, color=NAVY)

    for x in [5.3, 10.5]:
        ax.annotate('', xy=(x+0.5, 5.2), xytext=(x-0.5, 5.2),
                    arrowprops=dict(arrowstyle='->', color=MGRAY, lw=2.5, mutation_scale=20))

    ax.text(8, 2.5, 'Canonical Architecture Hierarchy', fontsize=12,
            fontweight='bold', ha='center', color=NAVY)
    arch = [('Chiplet\n2,000 qubits', 3.0, 2.0, GREEN),
            ('Module\n10,000 qubits', 6.2, 2.4, TEAL),
            ('System\n100,000 qubits', 9.6, 2.8, BLUE),
            ('Data Center\n1,000,000 qubits', 13.2, 3.2, NAVY)]
    ya = 1.3
    for label, x, w, c in arch:
        bx = FancyBboxPatch((x-w/2, ya-0.35), w, 0.7, boxstyle="round,pad=0.08",
                             facecolor=c, edgecolor=c, lw=1.5, alpha=0.13)
        ax.add_patch(bx)
        FancyBboxPatch((x-w/2, ya-0.35), w, 0.7, boxstyle="round,pad=0.08",
                        facecolor='none', edgecolor=c, lw=1.5)
        ax.add_patch(FancyBboxPatch((x-w/2, ya-0.35), w, 0.7, boxstyle="round,pad=0.08",
                                     facecolor='none', edgecolor=c, lw=1.5))
        ax.text(x, ya, label, ha='center', va='center', fontsize=8.5, fontweight='bold', color=NAVY)
    for x1, x2 in [(4.0, 5.0), (7.4, 8.2), (11.0, 11.6)]:
        ax.annotate('', xy=(x2, ya), xytext=(x1, ya),
                    arrowprops=dict(arrowstyle='->', color=MGRAY, lw=1.5))

    ax.text(8, 0.3, 'Claim Labels:  Demonstrated  |  Simulated  |  Derived from literature  |  QONTOS target  |  Stretch target',
            ha='center', fontsize=9.5, color=DGRAY,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=LGRAY, edgecolor=MGRAY))
    _save(fig, '00_executive_summary.png')


# =====================================================================
# PAPER 01: Architecture Hierarchy
# =====================================================================
def fig_01_arch():
    fig, ax = plt.subplots(figsize=(12, 7.5))
    ax.set_xlim(0, 12); ax.set_ylim(0, 8); ax.axis('off')
    ax.text(6, 7.6, 'QONTOS Four-Tier Modular Architecture',
            fontsize=16, fontweight='bold', ha='center', color=NAVY)
    ax.text(2.5, 7.1, 'COMPOSITION', fontsize=9, ha='center', color=MGRAY, fontweight='bold')
    ax.text(6, 7.1, 'PHYSICAL QUBITS', fontsize=9, ha='center', color=MGRAY, fontweight='bold')
    ax.text(9.5, 7.1, 'LOGICAL QUBITS', fontsize=9, ha='center', color=MGRAY, fontweight='bold')

    tiers = [
        ('Tier 4: Data Center', '10 Systems', '1,000,000', '10,000', NAVY, 11.0, 0.8),
        ('Tier 3: System', '10 Modules', '100,000', '1,000', BLUE, 9.6, 1.8),
        ('Tier 2: Module', '5 Chiplets', '10,000', '100', TEAL, 8.2, 2.8),
        ('Tier 1: Chiplet', 'Base Unit', '2,000', '20', GREEN, 6.8, 3.8),
    ]
    for name, comp, phys, log, color, width, xoff in tiers:
        y = tiers.index((name, comp, phys, log, color, width, xoff))
        yp = 0.6 + y * 1.5
        x0 = 6 - width/2
        bx = FancyBboxPatch((x0, yp), width, 1.15, boxstyle="round,pad=0.12",
                             facecolor=color, edgecolor=color, lw=2, alpha=0.12)
        ax.add_patch(bx)
        ax.add_patch(FancyBboxPatch((x0, yp), width, 1.15, boxstyle="round,pad=0.12",
                                     facecolor='none', edgecolor=color, lw=2))
        ax.text(x0+0.3, yp+0.75, name, fontsize=11, fontweight='bold', color=NAVY, va='center')
        ax.text(x0+0.3, yp+0.35, comp, fontsize=9, color=DGRAY, va='center')
        ax.text(6, yp+0.75, phys, fontsize=14, fontweight='bold', color=color, ha='center', va='center')
        ax.text(6, yp+0.35, 'physical qubits', fontsize=8, color=MGRAY, ha='center', va='center')
        ax.text(x0+width-0.3, yp+0.75, log, fontsize=14, fontweight='bold', color=color, ha='right', va='center')
        ax.text(x0+width-0.3, yp+0.35, 'logical qubits', fontsize=8, color=MGRAY, ha='right', va='center')

    # Multiplier arrows between tiers
    for i, mult in enumerate(['x5', 'x10', 'x10']):
        y_mid = 0.6 + i * 1.5 + 1.15 + 0.1
        ax.text(6, y_mid + 0.08, mult, fontsize=8, ha='center', va='bottom', color=MGRAY)
        ax.annotate('', xy=(6, y_mid + 0.28), xytext=(6, y_mid - 0.03),
                    arrowprops=dict(arrowstyle='->', color=MGRAY, lw=1.2))

    ax.text(6, 0.15, 'Logical qubit counts assume stretch-case 100:1 overhead (physical:logical)',
            ha='center', fontsize=9, color=DGRAY, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=LGRAY, edgecolor=MGRAY))
    _save(fig, '01_complete_architecture.png')


# =====================================================================
# PAPER 01: Scaling Timeline
# =====================================================================
def fig_01_scaling():
    fig, ax = plt.subplots(figsize=(11, 6.5))
    phases = ['Foundation\n2025-26', 'Sputnik\n2026-27', 'Pioneer\n2027-28',
              'Horizon\n2028-29', 'Summit\n2029-30']
    x = np.arange(len(phases))

    base =       [100, 2500, 20000, 50000, 100000]
    aggressive = [100, 10000, 100000, 200000, 500000]
    stretch =    [100, 10000, 100000, 500000, 1000000]

    ax.fill_between(x, base, stretch, alpha=0.08, color=BLUE)
    ax.plot(x, stretch, 'o-', color=ORANGE, lw=2.5, ms=8, label='Stretch', zorder=5)
    ax.plot(x, aggressive, 's-', color=BLUE, lw=2.5, ms=7, label='Aggressive', zorder=5)
    ax.plot(x, base, 'D-', color=GREEN, lw=2.5, ms=6, label='Base', zorder=5)

    for vals, color, dy in [(stretch, ORANGE, 1.4), (aggressive, BLUE, 0.7), (base, GREEN, 0.5)]:
        for i, v in enumerate(vals):
            ax.text(i, v * (1 + dy * 0.3), f'{v:,.0f}', fontsize=8, ha='center',
                    color=color, fontweight='bold')

    ax.set_yscale('log')
    ax.set_xticks(x); ax.set_xticklabels(phases, fontsize=10)
    ax.set_ylabel('Physical Qubits', fontsize=12, fontweight='bold')
    ax.set_title('QONTOS Scaling Roadmap: Base / Aggressive / Stretch Scenarios',
                 fontsize=13, fontweight='bold', color=NAVY, pad=12)
    ax.set_ylim(50, 3000000)
    ax.legend(fontsize=10, loc='upper left', framealpha=0.9)

    for i in range(1, len(phases)):
        ax.axvline(x=i-0.5, color=MGRAY, ls=':', lw=1, alpha=0.4)
    ax.text(0.02, 0.02, 'Validation gates between each phase', transform=ax.transAxes,
            fontsize=8, color=MGRAY, style='italic')
    _save(fig, '01_scaling_timeline.png')


# =====================================================================
# PAPER 02: Coherence Progress
# =====================================================================
def fig_02_coherence():
    fig, ax = plt.subplots(figsize=(11, 5.5))
    data = [
        ('Pre-Ta era (Nb/Al)\n~2020', 75, MGRAY, 'Conventional transmon baseline', 'solid'),
        ('Place et al. 2021\nTa on sapphire', 300, BLUE, 'Nat. Commun. 12, 1779 (2021)', 'solid'),
        ('Wang et al. 2022\nTa with dry etch', 500, BLUE, 'npj Quantum Inf. 8, 3 (2022)', 'solid'),
        ('Bland et al. 2025\nTa on HR-Si', 1680, BLUE, 'Nature 647, 343-348 (2025)', 'solid'),
        ('QONTOS Target\nStretch goal', 2000, ORANGE, 'Internal roadmap target', 'dashed'),
    ]
    labels = [d[0] for d in data]
    values = [d[1] for d in data]
    colors = [d[2] for d in data]
    y = np.arange(len(data))

    bars = ax.barh(y, values, height=0.55, color=colors, alpha=0.75, edgecolor=NAVY, lw=1.2)
    # Dashed edge for target
    bars[-1].set_edgecolor(ORANGE)
    bars[-1].set_linestyle('--')
    bars[-1].set_linewidth(2.5)
    bars[-1].set_alpha(0.35)

    for i, (val, ref) in enumerate(zip(values, [d[3] for d in data])):
        ax.text(val + 30, i + 0.12, f'{val:,} us', fontsize=10, fontweight='bold',
                color=NAVY, va='center')
        ax.text(val + 30, i - 0.15, ref, fontsize=7.5, color=MGRAY, va='center', style='italic')

    ax.axvline(x=1000, color=RED, ls='--', lw=1.5, alpha=0.6)
    ax.text(1010, len(data)-0.5, '1 ms\nFT regime', fontsize=8, color=RED, va='top')

    ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlabel('Coherence Time T1 (us)', fontsize=11, fontweight='bold')
    ax.set_title('Tantalum-on-Silicon Transmon Qubit: Coherence Progress',
                 fontsize=13, fontweight='bold', color=NAVY, pad=12)
    ax.set_xlim(0, 2500)
    ax.invert_yaxis()
    _save(fig, '02_qubit_physics.png')


# =====================================================================
# PAPER 02: Operations Budget
# =====================================================================
def fig_02_ops():
    fig, ax = plt.subplots(figsize=(11, 6.5))
    labels = ['Pre-Ta\n(Nb/Al, ~2020)', 'Place et al.\n2021', 'Wang et al.\n2022',
              'Bland et al.\n2025', 'QONTOS\nTarget']
    t1_us = [75, 300, 500, 1680, 2000]
    gate_ns = 25

    raw = [t * 1000 / gate_ns for t in t1_us]
    qec_d7 = [r / (7 * 7 + 6 * 6 + 7 * 7) * 7 for r in raw]  # rough: overhead ~ d^2 per logical gate
    qec_d15 = [r / (15*15 + 14*14 + 15*15) * 15 for r in raw]

    x = np.arange(len(labels))
    w = 0.25
    b1 = ax.bar(x - w, raw, w, label=f'Raw gate slots (T1 / {gate_ns}ns)', color=BLUE, edgecolor=NAVY, lw=0.8)
    b2 = ax.bar(x, qec_d7, w, label='After QEC overhead (d=7)', color=TEAL, edgecolor=NAVY, lw=0.8)
    b3 = ax.bar(x + w, qec_d15, w, label='After QEC overhead (d=15)', color=ORANGE, edgecolor=NAVY, lw=0.8)

    for bars in [b1, b2, b3]:
        for bar in bars:
            h = bar.get_height()
            if h > 0:
                ax.text(bar.get_x() + bar.get_width()/2, h * 1.15,
                        f'{int(h):,}', ha='center', va='bottom', fontsize=7.5,
                        fontweight='bold', color=NAVY)

    ax.set_yscale('log')
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel('Number of Operations', fontsize=11, fontweight='bold')
    ax.set_title('Physical Qubit Operations Budget: Raw vs. Logical Depth',
                 fontsize=13, fontweight='bold', color=NAVY, pad=12)
    ax.legend(fontsize=9, loc='upper left', framealpha=0.9)
    ax.set_ylim(10, 500000)
    ax.text(0.5, -0.10, 'Raw gate slots != useful logical depth. Surface-code QEC at distance d '
            'requires ~d syndrome rounds per logical gate,\nreducing usable operations by the code distance. '
            f'Gate time = {gate_ns} ns (single-qubit). T1 values from published literature.',
            transform=ax.transAxes, fontsize=8, ha='center', color=MGRAY, style='italic')
    _save(fig, '02_materials_comparison.png')


# =====================================================================
# PAPER 03: Error Correction Log-Log Plot
# =====================================================================
def fig_03_error():
    fig, ax = plt.subplots(figsize=(11, 7))
    p_th = 0.01
    p = np.logspace(-4, -1.7, 300)
    dists = [3, 5, 7, 9, 11, 13, 15]
    cols = ['#E53935', '#FF6F00', '#FFB300', '#4CAF50', '#00BCD4', '#1E88E5', '#5E35B1']
    for d, c in zip(dists, cols):
        pL = 0.03 * (p / p_th) ** ((d+1)/2)
        mask = pL > 1e-18
        ax.plot(p[mask], pL[mask], color=c, lw=2, label=f'd = {d}')

    ax.axvline(x=p_th, color=RED, ls=':', lw=1.5, alpha=0.7)
    ax.text(p_th*1.2, 5e-2, 'Threshold\np = 1%', fontsize=9, color=RED, va='top')
    ax.axvline(x=1e-3, color=BLUE, ls='--', lw=1.5, alpha=0.6)
    ax.text(8e-4, 1e-14, 'Current best\n2Q fidelity', fontsize=8, color=BLUE, ha='right')
    ax.axhline(y=1e-8, color=ORANGE, ls='--', lw=1.5, alpha=0.6)
    ax.text(1.5e-4, 1.5e-8, 'QONTOS stretch target', fontsize=8, color=ORANGE)
    rect = plt.Rectangle((5e-4, 1e-12), 2.5e-3, 1e-6, facecolor=GREEN, alpha=0.06,
                          edgecolor=GREEN, lw=1, ls='--')
    ax.add_patch(rect)
    ax.text(1.2e-3, 5e-10, 'Useful operating\nregime', fontsize=8, color=GREEN, ha='center', style='italic')

    ax.set_xscale('log'); ax.set_yscale('log')
    ax.set_xlabel('Physical Error Rate (p)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Logical Error Rate (p_L)', fontsize=12, fontweight='bold')
    ax.set_title('Logical Error Rate vs. Physical Error Rate:\nSurface Code Distance Scaling',
                 fontsize=14, fontweight='bold', color=NAVY, pad=12)
    ax.set_xlim(1e-4, 2e-2); ax.set_ylim(1e-16, 1)
    ax.legend(title='Code Distance', loc='upper left', fontsize=9, framealpha=0.9)
    ax.text(0.98, 0.03, r'$p_L \approx 0.03 \times (p/p_{th})^{(d+1)/2}$' + '\n' +
            r'$p_{th} \approx 1\%$ (surface code)',
            transform=ax.transAxes, fontsize=9, ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=LGRAY, edgecolor=MGRAY))
    _save(fig, '03_error_correction.png')


# =====================================================================
# PAPER 03: Code Structures / Overhead Comparison
# =====================================================================
def fig_03_codes():
    fig, ax = plt.subplots(figsize=(11, 6))
    cats = ['Surface Code\n(d=15, conservative)', 'Surface Code\n(d=7, reduced)',
            'qLDPC [[144,12,12]]\n(theoretical)', 'QONTOS Hybrid\n(stretch target)']
    vals = [450, 100, 12, 100]
    cols = [BLUE, TEAL, GREEN, ORANGE]
    bars = ax.barh(cats, vals, color=cols, edgecolor=NAVY, lw=1.5, height=0.55)
    bars[3].set_linestyle('--'); bars[3].set_edgecolor(ORANGE); bars[3].set_linewidth(2.5)

    for bar, val in zip(bars, vals):
        lbl = f'{val}:1'
        if val == 100 and bar == bars[3]:
            lbl += '  (STRETCH TARGET)'
        ax.text(bar.get_width() + 12, bar.get_y() + bar.get_height()/2,
                lbl, va='center', fontsize=10, fontweight='bold', color=NAVY)

    for v, lbl, c, ls in [(1000, 'Conservative (1000:1)', RED, ':'),
                           (300, 'Aggressive (300:1)', ORANGE, '--'),
                           (100, 'Stretch (100:1)', GREEN, '--')]:
        ax.axvline(x=v, color=c, ls=ls, lw=1.5, alpha=0.5)
        ax.text(v+8, 3.6, lbl, fontsize=8, color=c, va='top')

    ax.set_xlabel('Physical : Logical Qubit Ratio', fontsize=12, fontweight='bold')
    ax.set_title('QEC Overhead Scenarios: Conservative / Aggressive / Stretch',
                 fontsize=13, fontweight='bold', color=NAVY, pad=12)
    ax.set_xlim(0, 1200)
    ax.text(0.5, -0.08, 'Note: qLDPC codes require 6+ connectivity. Surface code overheads include ancillas + routing.',
            transform=ax.transAxes, fontsize=8, ha='center', color=MGRAY, style='italic')
    _save(fig, '03_code_structures.png')


# =====================================================================
# PAPER 04: Transduction Link Budget  (FIXED: no overlapping labels)
# =====================================================================
def fig_04():
    fig, ax = plt.subplots(figsize=(13, 7))
    comps = ['Microwave\ncoupling', 'Electro-mech.\nconversion', 'Mech.-optical\nconversion',
             'Fiber\ntransmission', 'Optical\ndetection', 'Heralding\noverhead']
    stretch =    [0.5, 7.0, 3.0, 0.2, 1.0, 2.0]
    aggressive = [1.0, 10.0, 5.0, 0.5, 1.5, 3.0]
    base =       [2.0, 15.0, 8.0, 1.0, 2.0, 5.0]
    research =   [3.0, 20.0, 12.0, 2.0, 3.0, 8.0]

    x = np.arange(len(comps))
    w = 0.19
    ax.bar(x - 1.5*w, research, w, label='Research (<1%)', color=RED, alpha=0.8)
    ax.bar(x - 0.5*w, base, w, label='Base (1-10%)', color=ORANGE, alpha=0.8)
    ax.bar(x + 0.5*w, aggressive, w, label='Aggressive (10-20%)', color=TEAL, alpha=0.8)
    ax.bar(x + 1.5*w, stretch, w, label='Stretch (>20%)', color=GREEN, alpha=0.8)

    ax.set_ylabel('Signal Loss (dB)', fontsize=12, fontweight='bold')
    ax.set_title('End-to-End Photonic Link Budget:\nMicrowave-to-Optical Transduction',
                 fontsize=14, fontweight='bold', color=NAVY, pad=12)
    ax.set_xticks(x); ax.set_xticklabels(comps, fontsize=9.5)
    ax.legend(title='Scenario Band', fontsize=9, loc='upper right', framealpha=0.9)

    # Efficiency box
    totals = {'Stretch': sum(stretch), 'Aggressive': sum(aggressive),
              'Base': sum(base), 'Research': sum(research)}
    eff = "End-to-end efficiency:\n"
    for nm, db in totals.items():
        e = 10**(-db/10) * 100
        eff += f"  {nm}: -{db:.1f} dB = {e:.2f}%\n"
    ax.text(0.98, 0.98, eff.strip(), transform=ax.transAxes, fontsize=8.5,
            ha='right', va='top', bbox=dict(boxstyle='round,pad=0.4', facecolor=LGRAY, edgecolor=MGRAY))
    ax.text(0.5, -0.08, 'Literature baselines: Mirhosseini 2020, Delaney 2022, Lecocq 2021',
            transform=ax.transAxes, fontsize=8, ha='center', color=MGRAY, style='italic')
    _save(fig, '04_transduction.png')


# =====================================================================
# PAPER 05: Decoder Pipeline  (FIXED: larger figure, better spacing)
# =====================================================================
def fig_05():
    fig, ax = plt.subplots(figsize=(16, 7))
    ax.set_xlim(0, 16); ax.set_ylim(0, 7); ax.axis('off')
    ax.text(8, 6.6, 'QONTOS Decoder Pipeline: Three-Stage Architecture',
            fontsize=16, fontweight='bold', ha='center', color=NAVY)
    ax.text(8, 6.2, 'Target: < 1 us end-to-end decoding latency',
            fontsize=10, ha='center', color=MGRAY, style='italic')

    # Input box
    bx = FancyBboxPatch((0.4, 3.5), 2.0, 1.3, boxstyle="round,pad=0.15",
                         facecolor=LGRAY, edgecolor=NAVY, lw=1.5)
    ax.add_patch(bx)
    ax.text(1.4, 4.3, 'Syndrome', fontsize=10, fontweight='bold', ha='center', color=NAVY)
    ax.text(1.4, 3.9, 'Bits', fontsize=10, fontweight='bold', ha='center', color=NAVY)
    ax.text(1.4, 3.6, 'from QPU', fontsize=8, ha='center', color=MGRAY)

    stages = [
        (3.3, 'Stage 1: CFE', 'Classical Front-End', '~100 ns', 'Pre-processing', BLUE),
        (6.5, 'Stage 2: NAR', 'Neural Accelerated\nReasoner', '~200-500 ns', 'ML-based decoding', TEAL),
        (9.7, 'Stage 3: CD', 'Correction\nDispatcher', '~50 ns', 'Lookup & apply', GREEN),
    ]
    for x, title, sub, time, desc, c in stages:
        bx = FancyBboxPatch((x, 2.9), 2.5, 2.5, boxstyle="round,pad=0.2",
                             facecolor=c, edgecolor=c, lw=2.5, alpha=0.1)
        ax.add_patch(bx)
        ax.add_patch(FancyBboxPatch((x, 2.9), 2.5, 2.5, boxstyle="round,pad=0.2",
                                     facecolor='none', edgecolor=c, lw=2.5))
        ax.text(x+1.25, 5.0, title, ha='center', fontsize=11, fontweight='bold', color=NAVY)
        ax.text(x+1.25, 4.4, sub, ha='center', fontsize=9, color=c)
        ax.text(x+1.25, 3.7, desc, ha='center', fontsize=8.5, color=MGRAY)
        # Timing badge
        badge = FancyBboxPatch((x+0.4, 3.0), 1.7, 0.4, boxstyle="round,pad=0.08",
                                facecolor=c, edgecolor='none', alpha=0.15)
        ax.add_patch(badge)
        ax.text(x+1.25, 3.2, time, ha='center', fontsize=10, fontweight='bold', color=c)

    # Output box
    bx = FancyBboxPatch((12.8, 3.5), 2.5, 1.3, boxstyle="round,pad=0.15",
                         facecolor=LGRAY, edgecolor=NAVY, lw=1.5)
    ax.add_patch(bx)
    ax.text(14.05, 4.3, 'Pauli', fontsize=10, fontweight='bold', ha='center', color=NAVY)
    ax.text(14.05, 3.9, 'Corrections', fontsize=10, fontweight='bold', ha='center', color=NAVY)
    ax.text(14.05, 3.6, 'to QPU', fontsize=8, ha='center', color=MGRAY)

    # Arrows
    for x1, x2 in [(2.4, 3.3), (5.8, 6.5), (9.0, 9.7), (12.2, 12.8)]:
        ax.annotate('', xy=(x2, 4.15), xytext=(x1, 4.15),
                    arrowprops=dict(arrowstyle='->', color=NAVY, lw=2, mutation_scale=15))

    # Hardware targets
    ax.text(8, 1.8, 'Hardware Deployment Targets', fontsize=12, fontweight='bold', ha='center', color=NAVY)
    for x, lbl, c, st in [(4.0, 'FPGA\n(Near-term)', BLUE, 'Engineering target'),
                           (8.0, 'ASIC\n(Scale)', TEAL, 'Stretch target'),
                           (12.0, 'Integrated\n(Per-module)', ORANGE, 'Research direction')]:
        bx = FancyBboxPatch((x-1.4, 0.7), 2.8, 0.8, boxstyle="round,pad=0.1",
                             facecolor=c, edgecolor=c, lw=1.5, alpha=0.1)
        ax.add_patch(bx)
        ax.text(x, 1.2, lbl, ha='center', fontsize=9, fontweight='bold', color=c)
        ax.text(x, 0.8, st, ha='center', fontsize=7.5, color=MGRAY)

    ax.text(8, 0.15, 'Total target latency: < 1 us  |  QEC cycle budget: 1-10 us',
            ha='center', fontsize=10, color=NAVY, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=BLUE))
    _save(fig, '05_ai_decoding.png')


# =====================================================================
# PAPER 06: Software Stack  (FIXED: larger, cleaner layers)
# =====================================================================
def fig_06():
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14); ax.set_ylim(0, 10.5); ax.axis('off')
    ax.text(7, 10.2, 'QONTOS Software Architecture', fontsize=16, fontweight='bold', ha='center', color=NAVY)
    ax.text(7, 9.8, 'Green = Implemented today  |  Orange dashed = Target / In development',
            fontsize=10, ha='center', color=MGRAY)

    layers = [
        (8.8, 'User Applications', 'Chemistry, Optimization, Finance, ML', GREEN, 'solid', 'IMPLEMENTED'),
        (7.4, 'QONTOS SDK', 'QontosClient, CircuitIR, async API, models', GREEN, 'solid', 'IMPLEMENTED'),
        (6.0, 'Orchestration Pipeline', 'Ingest -> Partition -> Schedule -> Execute -> Aggregate -> Verify',
         GREEN, 'solid', 'IMPLEMENTED'),
        (3.2, 'Observability & Integrity', 'Tracing, Metrics, Prometheus, SHA-256 Proof Chain',
         GREEN, 'solid', 'IMPLEMENTED'),
        (1.8, 'Future Extensions', 'Digital Twin, Modular Runtime, FT Compiler, Native Hardware Control',
         ORANGE, 'dashed', 'TARGET'),
    ]
    for y, title, sub, color, ls, status in layers:
        lw = 2.5 if ls == 'dashed' else 2
        bx = FancyBboxPatch((0.5, y), 13, 1.1, boxstyle="round,pad=0.12",
                             facecolor=color, edgecolor=color, lw=lw, alpha=0.08, linestyle=ls)
        ax.add_patch(bx)
        ax.add_patch(FancyBboxPatch((0.5, y), 13, 1.1, boxstyle="round,pad=0.12",
                                     facecolor='none', edgecolor=color, lw=lw, linestyle=ls))
        ax.text(0.9, y+0.72, title, fontsize=12, fontweight='bold', color=NAVY)
        ax.text(0.9, y+0.3, sub, fontsize=9, color=MGRAY)
        ax.text(13.3, y+0.55, status, fontsize=9, color=color, fontweight='bold', ha='right')

    # Execution layer (special)
    ye = 4.5
    ax.add_patch(FancyBboxPatch((0.5, ye), 13, 1.2, boxstyle="round,pad=0.12",
                                 facecolor=LGRAY, edgecolor=MGRAY, lw=1, alpha=0.3))
    ax.text(0.9, ye+0.85, 'Execution Layer', fontsize=12, fontweight='bold', color=NAVY)
    execs = [('Local\nSimulator', 1.5, GREEN, 'solid'), ('IBM\nQuantum', 4.5, GREEN, 'solid'),
             ('Amazon\nBraket', 7.5, GREEN, 'solid'), ('Native QONTOS\nHardware', 10.5, ORANGE, 'dashed')]
    for lbl, x, c, ls in execs:
        lw = 2 if ls == 'dashed' else 1.5
        bx = FancyBboxPatch((x, ye+0.08), 2.3, 0.65, boxstyle="round,pad=0.08",
                             facecolor=c, edgecolor=c, lw=lw, alpha=0.1, linestyle=ls)
        ax.add_patch(bx)
        ax.add_patch(FancyBboxPatch((x, ye+0.08), 2.3, 0.65, boxstyle="round,pad=0.08",
                                     facecolor='none', edgecolor=c, lw=lw, linestyle=ls))
        ax.text(x+1.15, ye+0.4, lbl, ha='center', fontsize=9, fontweight='bold', color=NAVY)

    ax.text(7, 0.7, 'github.com/qontos/qontos', fontsize=11, ha='center', color=BLUE, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=BLUE))
    _save(fig, '06_software_stack.png')


# =====================================================================
# PAPER 07: Cryogenic  (FIXED: bigger, no overlaps)
# =====================================================================
def fig_07():
    fig, ax = plt.subplots(figsize=(14, 8))
    stages = [
        ('300 K  (Room temp)', 'Control electronics, classical compute', 'N/A', '#E53935'),
        ('50 K  (1st stage)', 'Coax cables, high-BW wiring', '~40 W', '#FF6F00'),
        ('4 K  (2nd stage)', 'HEMT amplifiers, DC wiring', '~1.5 W', '#FFB300'),
        ('800 mK  (Still)', 'Filtering, attenuation', '~100 mW', '#4CAF50'),
        ('100 mK  (Cold plate)', 'Attenuators, filters', '~1 mW', '#00BCD4'),
        ('15 mK  (MXC)', 'QPU modules, quantum plane', '10-25 mW', '#1E88E5'),
    ]
    widths = [10, 8.5, 7, 5.5, 4, 2.5]
    y_positions = list(range(len(stages) - 1, -1, -1))

    for i, ((label, comps, cool, color), w) in enumerate(zip(stages, widths)):
        y = y_positions[i]
        ax.barh(y, w, height=0.65, color=color, alpha=0.2, edgecolor=color, lw=2)
        ax.text(0.15, y + 0.08, label, fontsize=11, fontweight='bold', color=NAVY, va='center')
        ax.text(w + 0.3, y + 0.12, comps, fontsize=9, color=DGRAY, va='center')
        ax.text(w + 0.3, y - 0.15, f'Cooling capacity: {cool}', fontsize=8.5,
                color=color, fontweight='bold', va='center')

    ax.set_yticks([]); ax.set_xticks([]); ax.set_xlim(-0.5, 14)
    for spine in ax.spines.values(): spine.set_visible(False)
    ax.grid(False)
    ax.set_title('Cryogenic Infrastructure: Multi-Stage Thermal Budget',
                 fontsize=14, fontweight='bold', color=NAVY, pad=15)

    # Scaling box (positioned to not overlap)
    ax.text(11.5, 4.5,
            'Scaling challenge:\n'
            'At 10 modules per system,\n'
            'total 15 mK heat load\n'
            '= 100-250 mW\n\n'
            'Commercial DR capacity:\n'
            '10-25 mW per unit',
            fontsize=9, color=RED, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFEBEE', edgecolor=RED, lw=1))

    ax.text(11.5, 1.5,
            'QONTOS canonical:\n'
            '5 chiplets/module\n'
            '2,000 qubits at 15 mK\n'
            '2,000-3,000 control lines',
            fontsize=9, color=BLUE, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#E3F2FD', edgecolor=BLUE, lw=1))
    _save(fig, '07_cryogenic.png')


# =====================================================================
# PAPER 08: Algorithms Staircase  (FIXED: cleaner layout)
# =====================================================================
def fig_08():
    fig, ax = plt.subplots(figsize=(12, 7.5))
    benchmarks = [
        ('H2', 2, 1e3, GREEN, 'Near-term, classically verifiable'),
        ('LiH', 6, 1e5, GREEN, 'Small molecule validation'),
        ('Small catalyst\n(active space)', 30, 1e8, '#FFB300', 'Intermediate milestone'),
        ('P450 / Fe4S4\n(medium)', 100, 1e10, ORANGE, 'Application regime'),
        ('FeMoco\n(Reiher 2017)', 300, 1e14, RED, 'STRETCH: flagship'),
    ]
    for lbl, q, tg, c, ann in benchmarks:
        ax.scatter(q, tg, s=300, color=c, edgecolors=NAVY, lw=1.5, zorder=5)
        # Place label to the right, annotation below
        ax.text(q * 1.25, tg, lbl, fontsize=10, fontweight='bold', color=NAVY, va='center')
        ax.text(q * 1.25, tg * 0.15, ann, fontsize=8, color=MGRAY, style='italic', va='center')

    qs = [b[1] for b in benchmarks]; ts = [b[2] for b in benchmarks]
    ax.plot(qs, ts, color=MGRAY, lw=1, ls='--', alpha=0.4, zorder=1)

    ax.axhspan(1, 1e6, alpha=0.03, color=GREEN)
    ax.axhspan(1e6, 1e11, alpha=0.03, color=ORANGE)
    ax.axhspan(1e11, 1e16, alpha=0.03, color=RED)
    ax.text(1.3, 1e3, 'BASE', fontsize=9, color=GREEN, fontweight='bold')
    ax.text(1.3, 1e8, 'AGGRESSIVE', fontsize=9, color=ORANGE, fontweight='bold')
    ax.text(1.3, 1e13, 'STRETCH', fontsize=9, color=RED, fontweight='bold')

    ax.set_xscale('log'); ax.set_yscale('log')
    ax.set_xlabel('Logical Qubits Required', fontsize=12, fontweight='bold')
    ax.set_ylabel('T-gate Count (approximate)', fontsize=12, fontweight='bold')
    ax.set_title('Application Benchmark Staircase: Resource Requirements',
                 fontsize=14, fontweight='bold', color=NAVY, pad=12)
    ax.set_xlim(1, 1000); ax.set_ylim(1e2, 1e16)
    ax.text(0.98, 0.03, 'Resource estimates: Reiher et al. 2017, Lee et al. 2021, Beverland et al. 2022',
            transform=ax.transAxes, fontsize=8, ha='right', color=MGRAY, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=LGRAY, edgecolor=MGRAY))
    _save(fig, '08_quantum_algorithms.png')


# =====================================================================
# PAPER 09: Evidence Pyramid  (FIXED: no text bleeding)
# =====================================================================
def fig_09():
    fig, ax = plt.subplots(figsize=(13, 8.5))
    ax.set_xlim(0, 13); ax.set_ylim(0, 10); ax.axis('off')
    ax.text(6, 9.5, 'QONTOS Benchmark Framework: Evidence Pyramid',
            fontsize=16, fontweight='bold', ha='center', color=NAVY)

    layers = [
        ('L0: Device Metrics', 'T1, T2, gate fidelity, readout, yield',
         'Direct measurement  |  Demonstrated / Simulated', BLUE, 11.5),
        ('L1: Logical Metrics', 'Logical error rate, QEC cycle time, overhead',
         'QEC benchmarks  |  Simulated / Target', TEAL, 9.5),
        ('L2: System Metrics', 'Quantum Volume, CLOPS, inter-module fidelity',
         'System benchmarks  |  Simulated / Target', GREEN, 7.5),
        ('L3: Application Metrics', 'VQE accuracy, QAOA quality, chemistry ladder',
         'Application benchmarks  |  Target / Stretch', ORANGE, 5.5),
        ('L4: Release Gates', 'Pass/fail thresholds for public claims',
         'CI + evidence board  |  Gate decision', RED, 3.5),
    ]
    for i, (title, metrics, method, color, width) in enumerate(layers):
        y = 1.0 + i * 1.6
        xc = 6; h = 1.35
        nw = layers[i+1][4] if i < len(layers)-1 else width * 0.5
        pts = np.array([[xc-width/2, y], [xc+width/2, y],
                        [xc+nw/2, y+h], [xc-nw/2, y+h]])
        ax.add_patch(plt.Polygon(pts, facecolor=color, edgecolor=color, lw=2, alpha=0.1))
        ax.add_patch(plt.Polygon(pts, facecolor='none', edgecolor=color, lw=2))
        ax.text(xc, y+h*0.72, title, ha='center', fontsize=11, fontweight='bold', color=NAVY)
        ax.text(xc, y+h*0.42, metrics, ha='center', fontsize=8.5, color=DGRAY)
        ax.text(xc, y+h*0.15, method, ha='center', fontsize=7.5, color=color, style='italic')

    # Maturity sidebar
    ax.text(12.3, 8.8, 'Maturity', fontsize=11, fontweight='bold', ha='center', color=NAVY)
    ax.text(12.3, 8.5, 'Levels', fontsize=11, fontweight='bold', ha='center', color=NAVY)
    mat = [('M0', 'Concept', MGRAY), ('M1', 'Prototype', BLUE), ('M2', 'Validated', TEAL),
           ('M3', 'Reproducible', GREEN), ('M4', 'CI-gated', ORANGE), ('M5', 'Production', RED)]
    for j, (lv, desc, c) in enumerate(mat):
        ym = 7.8 - j * 0.7
        ax.text(11.8, ym, lv, fontsize=9, fontweight='bold', color=c)
        ax.text(12.3, ym, desc, fontsize=8.5, color=DGRAY)
    _save(fig, '09_benchmarking.png')


# =====================================================================
# PAPER 10: Roadmap  (FIXED: wider, better spacing)
# =====================================================================
def fig_10_roadmap():
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16); ax.set_ylim(0, 10); ax.axis('off')
    ax.text(8, 9.5, 'QONTOS Gated Development Roadmap Through 2030',
            fontsize=16, fontweight='bold', ha='center', color=NAVY)
    ax.text(8, 9.1, 'Each phase is contingent on passing explicit validation gates',
            fontsize=10, ha='center', color=MGRAY, style='italic')

    phases = [('FOUNDATION', '2025-26', 1.8), ('SPUTNIK', '2026-27', 4.6),
              ('PIONEER', '2027-28', 7.4), ('HORIZON', '2028-29', 10.2),
              ('SUMMIT', '2029-30', 13.0)]
    outcomes = {
        'FOUNDATION': ['Platform +\nbenchmarks', 'HW validation\npath', 'Stretch\nevidence'],
        'SPUTNIK': ['Small modular\nHW path', '10k-qubit\nmodule', 'Module\ntarget'],
        'PIONEER': ['Distributed\nruntime', 'Multi-module\ndemos', '100k qubit\npath'],
        'HORIZON': ['Modular\nplatform', '100k phys.\n100-1k log.', '500k phys.\n5k log.'],
        'SUMMIT': ['Commercial\nplatform', 'Large FT\nmachine', '1M phys.\n10k log.'],
    }
    scen = [('Base', GREEN, 7.0), ('Aggressive', ORANGE, 5.6), ('Stretch', RED, 4.2)]

    for name, years, x in phases:
        hdr = FancyBboxPatch((x-1.1, 8.0), 2.2, 0.7, boxstyle="round,pad=0.1",
                              facecolor=BLUE, edgecolor=NAVY, lw=1.5, alpha=0.12)
        ax.add_patch(hdr)
        ax.text(x, 8.45, name, ha='center', fontsize=10, fontweight='bold', color=NAVY)
        ax.text(x, 8.15, years, ha='center', fontsize=8, color=MGRAY)

        for sname, color, y in scen:
            idx = ['Base', 'Aggressive', 'Stretch'].index(sname)
            out = outcomes[name][idx]
            bx = FancyBboxPatch((x-1.0, y-0.45), 2.0, 1.0, boxstyle="round,pad=0.08",
                                 facecolor=color, edgecolor=color, lw=1.5, alpha=0.08)
            ax.add_patch(bx)
            ax.add_patch(FancyBboxPatch((x-1.0, y-0.45), 2.0, 1.0, boxstyle="round,pad=0.08",
                                         facecolor='none', edgecolor=color, lw=1.5))
            ax.text(x, y+0.05, out, ha='center', va='center', fontsize=8, color=NAVY)

        if name != 'SUMMIT':
            gx = x + 1.4
            diamond = plt.Polygon([(gx, 5.6), (gx+0.2, 5.4), (gx, 5.2), (gx-0.2, 5.4)],
                                  facecolor='#FFD600', edgecolor=NAVY, lw=1.5)
            ax.add_patch(diamond)
            ax.text(gx, 4.9, 'GATE', ha='center', fontsize=7, fontweight='bold', color=NAVY)

    for sname, color, y in scen:
        ax.text(0.4, y+0.05, sname, fontsize=10, fontweight='bold', color=color, va='center')

    ax.text(8, 3.0,
            'Fallback examples:  Transduction < 5% --> cap at 50k qubits  |  '
            'QEC overhead > 300:1 --> downgrade logical target  |  '
            'Chiplet yield miss --> smaller module topology',
            ha='center', fontsize=8.5, color=DGRAY,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF3E0', edgecolor=ORANGE, lw=1))

    gates = ['G1: Device coherence', 'G2: First logical qubit', 'G3: Multi-module QEC',
             'G4: Overhead < aggressive', 'G5: All subsystems stretch']
    ax.text(8, 2.2, 'Key Decision Points', fontsize=12, fontweight='bold', ha='center', color=NAVY)
    for i, g in enumerate(gates):
        col = i % 3; row = i // 3
        ax.text(2.5 + col * 4.5, 1.5 - row * 0.5, g, fontsize=8.5, color=NAVY,
                bbox=dict(boxstyle='round,pad=0.15', facecolor=LGRAY, edgecolor=MGRAY))
    _save(fig, '10_roadmap_2030.png')


# =====================================================================
# PAPER 10: Risk Matrix  (FIXED: no overlapping bubbles/labels)
# =====================================================================
def fig_10_risk():
    fig, ax = plt.subplots(figsize=(11, 7.5))
    risks = [
        ('Qubit coherence\nat scale', 3.5, 3.0, 'T', 45),
        ('QEC overhead\nstalls', 4.5, 3.0, 'T', 55),
        ('Transduction\nefficiency', 4.3, 3.8, 'T', 60),
        ('Cryogenic\nscaling', 3.0, 1.5, 'T', 40),
        ('Decoder\nlatency', 2.5, 2.5, 'T', 35),
        ('Chiplet yield', 3.0, 2.5, 'T', 40),
        ('Supply chain', 2.0, 1.3, 'P', 30),
        ('Talent\nacquisition', 2.0, 2.5, 'P', 35),
        ('Capital access', 4.5, 1.5, 'P', 50),
    ]
    for lbl, imp, prob, cat, sz in risks:
        c = BLUE if cat == 'T' else ORANGE
        ax.scatter(imp, prob, s=sz*18, color=c, alpha=0.25, edgecolors=c, lw=2, zorder=5)
        ax.text(imp, prob, lbl, ha='center', va='center', fontsize=8, fontweight='bold', color=NAVY, zorder=6)

    ax.set_xlabel('Impact', fontsize=12, fontweight='bold')
    ax.set_ylabel('Probability', fontsize=12, fontweight='bold')
    ax.set_title('QONTOS Program Risk Matrix', fontsize=14, fontweight='bold', color=NAVY, pad=12)
    ax.set_xlim(0.8, 5.2); ax.set_ylim(0.5, 4.5)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_xticklabels(['Low', 'Medium-\nLow', 'Medium', 'High', 'Critical'], fontsize=9)
    ax.set_yticks([1, 2, 3, 4])
    ax.set_yticklabels(['Low', 'Medium', 'High', 'Very High'], fontsize=9)
    ax.axhspan(2.8, 5, alpha=0.03, color=RED)
    ax.axvspan(3.5, 6, alpha=0.03, color=RED)

    from matplotlib.lines import Line2D
    legend = [Line2D([0],[0], marker='o', color='w', markerfacecolor=BLUE, markersize=12, alpha=0.5, label='Technical'),
              Line2D([0],[0], marker='o', color='w', markerfacecolor=ORANGE, markersize=12, alpha=0.5, label='Programmatic')]
    ax.legend(handles=legend, loc='lower right', fontsize=9, framealpha=0.9)
    ax.text(0.02, 0.02, 'Bubble size indicates relative program exposure',
            transform=ax.transAxes, fontsize=8, color=MGRAY, style='italic')
    _save(fig, '10_risk_matrix.png')


# =====================================================================
# MAIN
# =====================================================================
if __name__ == '__main__':
    print(f"Output: {OUT}\n\nRegenerating all 15 figures...\n")
    fig_00()
    fig_01_arch()
    fig_01_scaling()
    fig_02_coherence()
    fig_02_ops()
    fig_03_error()
    fig_03_codes()
    fig_04()
    fig_05()
    fig_06()
    fig_07()
    fig_08()
    fig_09()
    fig_10_roadmap()
    fig_10_risk()
    print(f"\nAll 15 figures regenerated successfully.")
