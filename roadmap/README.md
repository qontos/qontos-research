# QONTOS Roadmap

## Overview

The QONTOS roadmap defines a five-phase program from 2025 to 2030, progressing from software platform launch and first qubit prototypes to a million-qubit fault-tolerant quantum computer. Each phase includes Base, Aggressive, and Stretch scenarios to account for technical and programmatic uncertainty.

The latest roadmap paper is available as [`10_Roadmap_2030.md`](10_Roadmap_2030.md).

---

## Phase 1 -- Foundation (2025-2026)

**Objective**: Launch the QONTOS software platform and demonstrate first tantalum-silicon qubit prototypes.

| Scenario | Physical Qubits | Logical Qubits | Key Milestones |
|----------|----------------|----------------|----------------|
| **Base** | 50 | 0 | Software platform v1.0, single-qubit characterization complete |
| **Aggressive** | 100 | 0 | Two-qubit gate fidelity > 99.5%, multi-qubit module prototype |
| **Stretch** | 200 | 1 | First logical qubit demonstration, cloud API beta |

**Deliverables**:
- QONTOS software stack v1.0 (circuit compiler, simulator, cloud API)
- Tantalum-silicon transmon qubit fabrication pipeline
- Single-qubit T1 > 200 us, T2 > 150 us demonstrated
- Two-qubit gate fidelity baseline established

---

## Phase 2 -- Sputnik (2026-2027)

**Objective**: Achieve a 1,000-qubit module and demonstrate real-time error correction.

| Scenario | Physical Qubits | Logical Qubits | Key Milestones |
|----------|----------------|----------------|----------------|
| **Base** | 500 | 2-5 | Surface code distance-3 demonstrations |
| **Aggressive** | 1,000 | 5-10 | Real-time AI decoding, distance-5 logical qubits |
| **Stretch** | 2,000 | 10-20 | Multi-module prototype, photonic link proof-of-concept |

**Deliverables**:
- 1,000-qubit single-module processor
- Real-time error correction with AI-driven decoding
- Surface code distance-5 logical qubit operation
- Cryogenic control electronics integration

---

## Phase 3 -- Pioneer (2027-2028)

**Objective**: Scale to 10,000 physical qubits with photonic interconnect integration.

| Scenario | Physical Qubits | Logical Qubits | Key Milestones |
|----------|----------------|----------------|----------------|
| **Base** | 5,000 | 20-50 | Multi-module system online, photonic links operational |
| **Aggressive** | 10,000 | 50-100 | Distributed error correction across modules |
| **Stretch** | 20,000 | 100-200 | First quantum advantage benchmarks, distance-7+ codes |

**Deliverables**:
- Multi-module quantum processor with photonic interconnects
- Distributed surface code error correction
- QONTOS software stack v2.0 with multi-module orchestration
- Quantum advantage demonstrations on targeted applications

---

## Phase 4 -- Horizon (2028-2029)

**Objective**: Reach 100,000 physical qubits and 1,000 logical qubits with quantum advantage benchmarks.

| Scenario | Physical Qubits | Logical Qubits | Key Milestones |
|----------|----------------|----------------|----------------|
| **Base** | 50,000 | 500 | Large-scale fault-tolerant operation demonstrated |
| **Aggressive** | 100,000 | 1,000 | Quantum advantage on commercially relevant problems |
| **Stretch** | 200,000 | 2,000 | Algorithmic breakthroughs leveraging logical qubit counts |

**Deliverables**:
- 100,000-qubit multi-module system
- 1,000 logical qubits with error rates below application thresholds
- Full cryogenic infrastructure for large-scale operation
- Commercial quantum computing services pilot

---

## Phase 5 -- Summit (2029-2030)

**Objective**: Achieve 1,000,000 physical qubits and 10,000 logical qubits with full fault tolerance.

| Scenario | Physical Qubits | Logical Qubits | Key Milestones |
|----------|----------------|----------------|----------------|
| **Base** | 500,000 | 5,000 | Production-grade fault-tolerant quantum computer |
| **Aggressive** | 1,000,000 | 10,000 | Full roadmap targets achieved, broad application portfolio |
| **Stretch** | 1,000,000+ | 10,000+ | Beyond-roadmap scaling, next-generation architectures |

**Deliverables**:
- Million-qubit fault-tolerant quantum computer
- 10,000 logical qubits operating below fault-tolerance thresholds
- Full-stack production deployment (hardware + software + cloud)
- Quantum computing as a service at commercial scale

---

## Scenario Definitions

| Scenario | Definition |
|----------|------------|
| **Base** | Conservative projections assuming typical R&D timelines and known technical risks |
| **Aggressive** | Optimistic projections assuming favorable technical outcomes and accelerated development |
| **Stretch** | Best-case projections assuming breakthroughs in key areas and maximum resource allocation |

## Risk Factors

Key risks tracked across all phases:

- **Qubit coherence**: Achieving and maintaining target T1/T2 times at scale
- **Fabrication yield**: Wafer-scale production with sufficient qubit yield
- **Interconnect fidelity**: Photonic link error rates meeting error correction thresholds
- **Decoder latency**: AI decoding speed keeping pace with error correction cycles
- **Cryogenic scaling**: Thermal management and wiring density at million-qubit scale
- **Supply chain**: Access to specialized materials (tantalum, dilution refrigerator components)

## Related Documents

- [Whitepaper](../whitepaper/) -- Full architectural vision
- [Paper 10 -- Roadmap 2030](../papers/) -- Detailed roadmap analysis
- [Benchmarks](../benchmarks/) -- Performance tracking against milestones
