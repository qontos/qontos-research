# Tantalum-on-Silicon Superconducting Qubits: Device Assumptions for a Modular Fault-Tolerant Path

**Technical Research Paper v2.1**

**Author:** Qontos Research Wing

**Affiliation:** Zhyra Quantum Research Institute (ZQRI), Abu Dhabi, UAE

**Correspondence:** research@zhyra.xyz

---

## Abstract

This paper examines the tantalum-on-silicon superconducting qubit platform as a candidate device basis for the QONTOS modular architecture. It evaluates the device assumptions required for the aggressive and stretch architecture scenarios, including millisecond-class coherence, very high two-qubit fidelity, scalable chiplet fabrication, and manageable cryogenic and control integration. The paper uses literature-reported millisecond-class coherence as a strong starting point and maps that progress into the practical questions of logical depth, packaging, calibration, and fabrication yield.

**Claim status:** literature-informed device feasibility paper with aggressive and stretch targets

**Keywords:** superconducting qubits, transmon, tantalum, coherence, device roadmap, chiplet fabrication

---

## 1. Introduction

The QONTOS architecture depends on a superconducting qubit platform that can simultaneously support:

- high coherence
- high gate fidelity
- scalable fabrication
- modular packaging
- practical calibration and control

Tantalum-on-silicon is attractive because literature reports suggest significant progress over earlier material stacks. However, raw coherence values alone do not establish a viable path to fault-tolerant computation. This paper therefore focuses on what device-level performance would actually be needed for the larger architecture to remain credible.

### 1.1 Claim Status Summary

| Claim | Status |
|---|---|
| Millisecond-class tantalum coherence exists in the literature | Derived from literature |
| QONTOS can build its stretch architecture on 2 ms devices | QONTOS target / stretch assumption |
| 99.999% two-qubit fidelity at scale is available | Stretch target |
| Million-qubit fabrication is economically viable | Stretch target |

---

## 2. Device Performance Requirements

![Materials Comparison](figures_final/02_materials_comparison.png){ width=100% }

*Figure 1: Device-platform comparison is presented as a feasibility envelope spanning current literature performance and stretch program targets.*

### 2.1 Scenario-Based Targets

| Metric | Base | Aggressive | Stretch |
|---|---:|---:|---:|
| T1 | 300 us | 1 ms | 2 ms |
| T2 | 300 us | 1 ms | 1.5-2 ms |
| 1Q fidelity | 99.9% | 99.99% | 99.999% |
| 2Q fidelity | 99.9% | 99.99% | 99.999% |
| 2Q gate time | 50 ns | 35 ns | 25 ns |
| Readout fidelity | 99.5% | 99.9% | 99.99% |

### 2.2 Literature Baseline

The strongest role of tantalum in the current QONTOS paper set is as a literature-supported direction and a serious device-development candidate for the modular architecture.

Representative literature-relevant points:

- millisecond-class coherence has been reported for high-quality tantalum devices
- materials quality and oxide behavior appear favorable relative to older stacks
- device integration at scale remains far less mature than isolated coherence headlines

---

## 3. Coherence, Gate Time, and Logical Depth

### 3.1 Raw Operations Are Not Logical Depth

The most important correction in this paper is conceptual:

Raw coherence time does not equal executable logical algorithm depth.

For example:

```text
Raw physical gate opportunities = T1 / gate_time

If T1 = 2 ms and 2Q gate time = 25 ns:
raw physical gate opportunities = 2,000,000 ns / 25 ns = 80,000
```

That number is not the same thing as:

- logical gate depth
- full algorithm depth
- fault-tolerant executable workload length

In practice, logical depth depends on:

- repeated error-correction cycles
- decoder latency
- leakage handling
- calibration stability
- state preparation and measurement overhead
- idling and synchronization across modules

### 3.2 Implication for QONTOS

The relevant device question is therefore not:

`How many raw gates fit inside T1?`

It is:

`Does this device regime reduce the burden on fault tolerance enough for the system-level architecture to remain plausible?`

That is the right role for the tantalum platform in the QONTOS story.

### 3.3 Workload-Oriented Device Requirements

| Workload class | Device implication |
|---|---|
| Early logical-qubit experiments | aggressive case may be sufficient |
| Modular fault-tolerance demonstrations | requires aggressive to stretch device regime |
| FeMoco-class flagship workloads | requires stretch device regime plus strong QEC and interconnect assumptions |

---

## 4. Device Architecture and Control

![Device Feasibility Stack](figures_final/02_qubit_physics.png){ width=100% }

*Figure 2: Raw coherence matters, but scalable device feasibility depends on fidelity, packaging, and yield together.*

### 4.1 Double-Transmon Coupler Targets

| Parameter | Aggressive | Stretch | Status |
|---|---:|---:|---|
| Tunable coupling window | +/- 50 MHz | +/- 50 MHz | QONTOS target |
| CZ gate fidelity | 99.99% | 99.999% | Target / stretch |
| CZ gate time | 35 ns | 25 ns | Target / stretch |
| ZZ suppression | <1 kHz | <0.1 kHz | Target / stretch |

### 4.2 What Must Be Validated

The coupler architecture must be evaluated not only for isolated gate performance, but for:

- frequency crowding
- calibration drift
- cross-talk at dense packing
- leakage under repeated operation
- compatibility with chiplet packaging

---

## 5. Fabrication and Packaging Strategy

### 5.1 Chiplet Assumptions

The current canonical stretch architecture assumes:

- 2,000 physical qubits per chiplet
- 5 chiplets per module
- 10,000 physical qubits per module

These are architecture constants, not demonstrated manufacturing outputs.

### 5.2 Fabrication Questions That Matter More Than Headlines

| Question | Why it matters |
|---|---|
| Can yield remain acceptable at chiplet scale? | stretch architecture fails if yield collapses |
| Can packaging preserve qubit performance? | good bare-die metrics do not guarantee module-level success |
| Can control density remain manageable? | wiring and control are often harder than the qubits themselves |
| Can calibration labor be reduced enough? | manual tuning does not scale to large chiplet fleets |

### 5.3 Partner Strategy

Named fabrication partners fit best as part of a partner strategy and target ecosystem for future scale-up.

Recommended phrasing:

`QONTOS is exploring a multi-partner fabrication strategy to reduce supply-chain concentration and improve scale flexibility.`

---

## 6. Thermal and Integration Constraints

### 6.1 Module Thermal Envelope

The current stretch planning envelope assumes roughly:

| Component | Total load |
|---|---:|
| Coaxial lines | 20 mW |
| Optical fibers | 0.01 mW |
| DC lines | 0.5 mW |
| Chip dissipation | 0.1 mW |
| Total | ~21 mW |
| Available budget | 25 mW |

This is a planning estimate tied to the cryogenic paper and the current architecture assumptions.

### 6.2 Packaging and Calibration Risks

The device story is not only about physics. It is equally about:

- packaging yield
- thermal interfaces
- connector density
- calibration automation
- module replacement and maintainability

If these remain unresolved, even excellent single-device metrics will not convert into a viable modular machine.

---

## 7. Device Roadmap by Scenario

| Year | Base | Aggressive | Stretch |
|---|---|---|---|
| 2025-2026 | literature benchmarking, design studies, calibration tooling | small internal validation targets | first evidence supporting millisecond-class stretch path |
| 2026-2027 | device-package integration | module-scale integration targets | 10,000 physical-qubit stretch module assumptions tested |
| 2027-2028 | robust modular hardware support | high-fidelity chiplet fleet | architecture-scale stretch device envelope tested |
| 2029-2030 | strong device basis for modular products | large modular fault-tolerance path | full stretch device assumptions required |

---

## 8. Validation Gates

The materials and device story becomes strongest for the stretch architecture once the following are satisfied:

1. coherence and fidelity are shown under realistic packaging conditions
2. chiplet-level control and calibration complexity are bounded
3. fabrication yield assumptions are grounded in a real partner process model
4. module thermal and control density assumptions survive systems review

---

## 9. Conclusion

Tantalum-on-silicon remains a promising candidate platform for the QONTOS modular architecture, especially because it offers a credible path toward stronger coherence and better device quality than older superconducting stacks. In this paper, raw coherence is treated as one important input to broader fault-tolerant algorithm readiness.

The technically defensible conclusion is:

- literature results make tantalum worth pursuing
- aggressive modular hardware scenarios may be plausible if packaging and control are solved
- the full million-qubit stretch architecture requires substantial additional validation beyond device-level headline metrics

---

## References

[1] Representative literature on tantalum transmons and millisecond-class coherence.

[2] Representative literature on superconducting gate fidelity, packaging, and calibration limits.

---

*Document Version: 2.1*  
*Classification: Technical Research Paper*  
*Claim posture: Device-feasibility analysis, not demonstrated stretch performance*
