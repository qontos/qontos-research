# QONTOS Research

Public whitepapers, roadmap, technical papers, and figures from the QONTOS quantum computing program.

## Overview

QONTOS is a full-stack modular quantum computing company. This repository contains the public research artifacts that define the long-range architecture, hardware assumptions, and program milestones.

- **Open today**: Software platform, simulators, benchmarks, examples
- **In development**: Native modular superconducting quantum hardware
- **Stretch roadmap**: 1,000,000 physical qubits and 10,000 logical qubits by 2030

## Documents

### Technical Whitepaper

The [QONTOS Technical Whitepaper](whitepaper/QONTOS_Technical_Whitepaper.md) documents the implemented orchestration platform and the modular research program.

- [Markdown](whitepaper/QONTOS_Technical_Whitepaper.md)
- [IEEE LaTeX](whitepaper/QONTOS_Technical_Whitepaper_IEEE.tex)

### Research Paper Series (v2)

| # | Paper | Topic | Status |
|---|-------|-------|--------|
| 01 | [Scaled Architecture](papers/01_QONTOS_Scaled_Architecture_v2.md) | Chiplet-module-system-datacenter hierarchy | Research |
| 02 | [Tantalum-Silicon Qubits](papers/02_Tantalum_Silicon_Qubits_v2.md) | Qubit platform and device physics | Research |
| 03 | [Error Correction at 100:1](papers/03_Error_Correction_100to1_v2.md) | QEC overhead reduction path | Research |
| 04 | [Photonic Interconnects](papers/04_Photonic_Interconnects_v2.md) | Inter-module communication | Research |
| 05 | [AI Decoding](papers/05_AI_Decoding_v2.md) | Neural decoder architecture | Research |
| 06 | [Software Stack](papers/06_Software_Stack_v2.md) | Orchestration and runtime | Implemented + Research |
| 07 | [Cryogenic Infrastructure](papers/07_Cryogenic_Infrastructure_v2.md) | Thermal and facility engineering | Research |
| 08 | [Quantum Algorithms](papers/08_Quantum_Algorithms_v2.md) | Application benchmarks | Research |
| 09 | [Benchmarking](papers/09_Benchmarking_v2.md) | Measurement methodology | Implemented + Research |
| 10 | [Roadmap 2030](papers/10_Roadmap_2030_v2.md) | Gated development plan | Research |

### Program Roadmap

The [5-Phase Development Roadmap](roadmap/ROADMAP_2030.md) outlines the gated program with base, aggressive, and stretch scenarios.

| Phase | Timeline | Base | Aggressive | Stretch |
|-------|----------|------|------------|---------|
| Foundation | 2025–2026 | Platform + benchmarks | First HW validation | Stretch device evidence |
| Sputnik | 2026–2027 | Small modular HW | 10k-qubit module | Stretch module target |
| Pioneer | 2027–2028 | Distributed runtime | Multi-module demos | 100k qubit path |
| Horizon | 2028–2029 | Modular platform | 100k phys. + 1k logical | 500k phys. + 5k logical |
| Summit | 2029–2030 | Commercial platform | Large FT machine | 1M phys. + 10k logical |

## Canonical Architecture

| Tier | Unit | Physical Qubits | Logical Qubits (100:1 stretch) |
|------|------|----------------:|-------------------------------:|
| Chiplet | 1 | 2,000 | 20 |
| Module | 5 chiplets | 10,000 | 100 |
| System | 10 modules | 100,000 | 1,000 |
| Data Center | 10 systems | 1,000,000 | 10,000 |

## Citation

```bibtex
@techreport{qontos2026,
  title = {QONTOS: Quantum Orchestrated Network for Transformative Optimization Systems},
  author = {QONTOS Quantum Technologies},
  institution = {Zhyra Quantum Research Institute},
  year = {2026},
  url = {https://github.com/qontos/qontos-research}
}
```

## Related Repositories

- [qontos](https://github.com/qontos/qontos) — Flagship SDK
- [qontos-sim](https://github.com/qontos/qontos-sim) — Simulators and digital twin
- [qontos-examples](https://github.com/qontos/qontos-examples) — Tutorials and examples
- [qontos-benchmarks](https://github.com/qontos/qontos-benchmarks) — Benchmark evidence

## License

Apache License 2.0. See [LICENSE](LICENSE).
