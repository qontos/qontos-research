# QONTOS 5-Phase Development Roadmap to 2030

This document outlines the gated development program for the QONTOS modular quantum computing platform. Each phase includes base, aggressive, and stretch scenarios.

---

## Phase Overview

| Phase | Timeline | Base | Aggressive | Stretch |
|-------|----------|------|------------|---------|
| **Foundation** | 2025–2026 | Platform + benchmarks | First HW validation | Stretch device evidence |
| **Sputnik** | 2026–2027 | Small modular HW | 10k-qubit module | Stretch module target |
| **Pioneer** | 2027–2028 | Distributed runtime | Multi-module demos | 100k qubit path |
| **Horizon** | 2028–2029 | Modular platform | 100k phys. + 1k logical | 500k phys. + 5k logical |
| **Summit** | 2029–2030 | Commercial platform | Large FT machine | 1M phys. + 10k logical |

## Canonical Architecture Targets

| Tier | Unit | Physical Qubits | Logical Qubits (100:1 stretch) |
|------|------|----------------:|-------------------------------:|
| Chiplet | 1 | 2,000 | 20 |
| Module | 5 chiplets | 10,000 | 100 |
| System | 10 modules | 100,000 | 1,000 |
| Data Center | 10 systems | 1,000,000 | 10,000 |

## Phase 1: Foundation (2025–2026)

**Objective:** Establish the open software platform and begin hardware research.

- **Base:** SDK, simulators, benchmarks, and examples publicly released
- **Aggressive:** First tantalum-silicon qubit prototypes fabricated and characterized
- **Stretch:** Preliminary device evidence supporting T1/T2 coherence targets

## Phase 2: Sputnik (2026–2027)

**Objective:** Demonstrate first modular quantum hardware.

- **Base:** Small-scale modular hardware demonstration
- **Aggressive:** 10,000-qubit single module operational
- **Stretch:** Module-level targets exceeded; chiplet yield validated

## Phase 3: Pioneer (2027–2028)

**Objective:** Multi-module distributed quantum computing.

- **Base:** Distributed runtime across multiple modules
- **Aggressive:** Multi-module demonstrations with photonic interconnects
- **Stretch:** Path to 100,000 physical qubits validated

## Phase 4: Horizon (2028–2029)

**Objective:** Large-scale modular quantum platform.

- **Base:** Modular platform with integrated error correction
- **Aggressive:** 100,000 physical qubits + 1,000 logical qubits
- **Stretch:** 500,000 physical qubits + 5,000 logical qubits

## Phase 5: Summit (2029–2030)

**Objective:** Commercial fault-tolerant quantum computing.

- **Base:** Commercial platform with demonstrated quantum advantage
- **Aggressive:** Large fault-tolerant quantum machine
- **Stretch:** 1,000,000 physical qubits + 10,000 logical qubits

---

For the full research paper on the roadmap, see [Paper 10: Roadmap 2030](../papers/10_Roadmap_2030_v2.md).

For the complete research paper series, see the [qontos-research README](../README.md).
