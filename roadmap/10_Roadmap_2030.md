# Roadmap to Large-Scale Modular Quantum Computing: Base, Aggressive, and Stretch Scenarios Through 2030

**Technical Research Paper v2.1**

**Author:** Qontos Research Wing

**Affiliation:** Zhyra Quantum Research Institute (ZQRI), Abu Dhabi, UAE

---

## Abstract

This paper presents a gated development roadmap for QONTOS through 2030. It replaces a single-path million-qubit storyline with three scenarios: `Base`, `Aggressive`, and `Stretch`. The stretch scenario retains the long-term aim of **1,000,000 physical qubits** and **10,000 logical qubits**, and the roadmap ties that ambition to explicit subsystem breakthroughs in device performance, error correction, interconnects, cryogenics, and software control. The purpose of the roadmap is to define a disciplined sequence of gates, fallback outcomes, and decision points.

**Claim status:** program roadmap and scenario planning document

---

## 1. Roadmap Philosophy

The previous roadmap framing was too singular. A technically feasible program needs:

- base outcome
- aggressive outcome
- stretch outcome
- validation gates
- no-go conditions
- fallback paths

### 1.1 Scenario Summary

| Scenario | By 2030 likely outcome |
|---|---|
| Base | strong software, digital twin, modular hardware integration, early logical qubits |
| Aggressive | large modular machine with meaningful logical-qubit and distributed FTQC demonstrations |
| Stretch | 1,000,000 physical qubits and 10,000 logical qubits |

### 1.2 What This Roadmap Establishes

This roadmap establishes:

- that the stretch scenario is gated by explicit subsystem milestones
- that the stretch budget is a planning envelope for the full program
- that subsystem breakthroughs will advance on different but coordinated timelines

---

## 2. Five Program Phases

![Gated Roadmap](figures_final/10_roadmap_2030.png){ width=100% }

*Figure 1: The roadmap is presented as a gated program with fallback outcomes across base, aggressive, and stretch scenarios.*

### 2.1 FOUNDATION (2025-2026)

**Primary objective**

- establish the software, benchmark, device, and digital-twin foundation

**Base outcome**

- strong software-first orchestration platform
- current benchmark harness and replayability
- improved architecture and assumptions discipline

**Aggressive outcome**

- first hardware-linked validation path
- stronger device and packaging evidence

**Stretch relevance**

- first evidence that stretch device and QEC assumptions are not obviously impossible

**Validation gates**

- canonical architecture constants fixed
- benchmark methodology paper in place
- first device assumptions table grounded in literature
- current platform and simulation artifacts reproducible

**No-go conditions**

- no coherent benchmark program
- no plausible device story
- no current platform credibility

**Fallback if gate fails**

- remain a software-first orchestration and digital-twin platform while hardware path matures

### 2.2 SPUTNIK (2026-2027)

**Primary objective**

- move from architecture thesis to first scaled modular hardware assumptions

**Base outcome**

- small modular hardware integration path
- digital-twin and software stack mature together

**Aggressive outcome**

- 10,000 physical-qubit class module assumptions become defensible
- first 100 logical-qubit program target becomes credible

**Stretch relevance**

- first evidence toward the 10,000 physical-qubit module target

**Validation gates**

- packaging and thermal budgets reviewed
- first logical-qubit milestone path defined
- inter-module entanglement experiment plan credible

**No-go conditions**

- module thermal/control assumptions fail
- device packaging does not preserve performance

**Fallback if gate fails**

- reduce module size and extend timeline while preserving modular software roadmap

### 2.3 PIONEER (2027-2028)

**Primary objective**

- validate multi-module behavior and distributed execution

**Base outcome**

- mature distributed runtime and modular benchmark program

**Aggressive outcome**

- large multi-module demonstrations
- 100-1,000 logical-qubit path becomes plausible

**Stretch relevance**

- first credible path to 100,000 physical qubits and modular FTQC subroutines

**Validation gates**

- distributed runtime and digital twin aligned
- inter-module communication passes minimum thresholds
- decoder path supports the targeted correction-cycle budget

**No-go conditions**

- communication overhead dominates
- decoder latency or reliability collapses at modular scale

**Fallback if gate fails**

- focus on lower-scale modular advantage and software commercialization

### 2.4 HORIZON (2028-2029)

**Primary objective**

- translate modular maturity into large-scale logical performance

**Base outcome**

- strong modular system platform with useful workload demonstrations

**Aggressive outcome**

- 100,000 physical-qubit and 100-1,000 logical-qubit class system becomes feasible

**Stretch relevance**

- 500,000 physical qubits and 5,000 logical qubits become conditionally plausible

**Validation gates**

- effective overhead moves materially below conservative baselines
- photonic and cryogenic assumptions survive systems validation
- benchmark ladder shows meaningful upward progression

**No-go conditions**

- effective overhead remains near 1000:1
- photonic path remains too weak for modular scaling

**Fallback if gate fails**

- keep aggressive system target, retire or defer the stretch case

### 2.5 SUMMIT (2029-2030)

**Primary objective**

- determine whether the stretch architecture is truly reachable

**Base outcome**

- commercially meaningful modular platform with validated logical resources

**Aggressive outcome**

- large fault-tolerant modular machine with strong flagship benchmark progress

**Stretch outcome**

- 1,000,000 physical qubits
- 10,000 logical qubits
- flagship chemistry or comparable application advantage

**Validation gates**

- device assumptions support stretch performance
- effective overhead near stretch case
- interconnect assumptions near stretch case
- benchmark and replay evidence support the claim set

**No-go conditions**

- one or more critical subsystems remain at base or conservative performance

**Fallback if gate fails**

- ship the strongest aggressive architecture achievable and continue stretch R&D beyond 2030

---

## 3. Scenario Tables

### 3.1 Architecture Outcome by 2030

| Metric | Base | Aggressive | Stretch |
|---|---:|---:|---:|
| Physical qubits | 10,000-20,000 | 100,000 | 1,000,000 |
| Logical qubits | 1-20 | 100-1,000 | 10,000 |
| Effective overhead | 1000:1 | 300:1 | 100:1 |
| Interconnect regime | limited modular | meaningful modular | large-scale modular |

### 3.2 Investment Envelope

| Scenario | Indicative interpretation |
|---|---|
| Base | software-led and hardware-integrating program |
| Aggressive | full modular research and scale-up program |
| Stretch | approximately the previously cited $530-780M class envelope, contingent on subsystem success |

The stretch investment number is an estimated planning envelope for the program.

---

## 4. Risks and Dependencies

### 4.1 Major technical dependencies

- millisecond-class device regime
- low-enough effective overhead
- practical decoder latency
- adequate transduction and Bell-pair performance
- cryogenic and control scalability

### 4.2 Major program dependencies

- fabrication partners
- packaging and supply chain
- sustained capital access
- team build-out across software, hardware, cryogenics, and QEC

### 4.3 Major communication risk

The communication standard for this roadmap is to present the stretch scenario as a staged, technically gated production program.

---

## 5. Recommended External Framing

The most technically credible public statement is:

`QONTOS is pursuing a modular quantum roadmap with base, aggressive, and stretch scenarios through 2030. The stretch scenario targets 1 million physical qubits and 10,000 logical qubits, contingent on major advances in qubits, error correction, interconnects, cryogenics, and control systems.`

Use stretch-case phrasing whenever communicating the largest architecture and application goals.

---

## 6. Conclusion

This roadmap is strongest when it is used as a disciplined program map rather than a single-path promise. The stretch scenario remains valuable because it defines a bold north star. But the base and aggressive scenarios are equally important because they preserve technical credibility and create real decision points.

The roadmap is therefore feasible only if it remains gated, scenario-based, and tightly linked to benchmark evidence.

---

## References

[1] Internal QONTOS architecture constants, assumptions register, and claim-status guidance.

[2] Representative literature on modular quantum systems, error correction, and large-scale superconducting roadmaps.

---

*Document Version: 2.1*  
*Classification: Technical Research Paper*  
*Claim posture: Scenario-based roadmap with explicit gates and fallback paths*
