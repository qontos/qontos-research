<div align="center">
  <a href="https://github.com/qontos">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/qontos/.github/main/assets/qontos-logo-white.png">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/qontos/.github/main/assets/qontos-logo.png">
      <img src="https://raw.githubusercontent.com/qontos/.github/main/assets/qontos-logo.png" alt="QONTOS" width="260">
    </picture>
  </a>

  <h3>QONTOS Research</h3>
  <p><strong>Whitepapers, roadmap, figures, and technical publications for the QONTOS program.</strong></p>
  <p>The public research surface for the software platform available today and the hybrid superconducting-photonic hardware program in development.</p>

  <p>
    <img src="https://img.shields.io/badge/Visibility-Public-0f766e?style=flat-square" alt="Visibility: Public">
    <img src="https://img.shields.io/badge/Track-Research-0b3b8f?style=flat-square" alt="Track: Research">
    <img src="https://img.shields.io/badge/Status-Active_Research-166534?style=flat-square" alt="Status: Active Research">
  </p>

  <p>
    <a href="#overview">Overview</a> &middot;
    <a href="#research-surface">Research Surface</a> &middot;
    <a href="#document-index">Document Index</a> &middot;
    <a href="#canonical-architecture">Canonical Architecture</a> &middot;
    <a href="#citation">Citation</a>
  </p>
</div>

---

## Overview

QONTOS Research is the public technical publication layer for the broader QONTOS platform. It collects the whitepaper, paper series, roadmap, and figures that explain how the software stack, modular hardware program, and long-range scaling assumptions fit together.

- **Open today**: SDK, simulators, examples, benchmarks, and public technical documentation
- **In development**: native modular superconducting hardware with photonic interconnects
- **Stretch roadmap**: 1,000,000 physical qubits and 10,000 logical qubits by 2030

## Research Surface

| Area | Focus |
| --- | --- |
| `whitepaper/` | Technical whitepaper for the QONTOS software stack and full-stack program |
| `papers/` | 10-paper research series covering architecture, devices, FTQC, interconnects, algorithms, and benchmarking |
| `roadmap/` | Gated multi-phase development path from platform maturity to large-scale modular hardware |
| `figures/` | Architecture, roadmap, and subsystem figures for publication and presentation use |
| `benchmarks/` | Public research context for the evidence and methodology layer |

## Document Index

### Technical Whitepaper

The [QONTOS Technical Whitepaper](whitepaper/QONTOS_Technical_Whitepaper.md) documents the implemented orchestration stack and the broader hybrid hardware research program.

- [Markdown](whitepaper/QONTOS_Technical_Whitepaper.md)
- [IEEE LaTeX](whitepaper/QONTOS_Technical_Whitepaper_IEEE.tex)

### Research Paper Series

| # | Paper | Topic | Status |
| --- | --- | --- | --- |
| 01 | [Scaled Architecture](papers/01_QONTOS_Scaled_Architecture_v2.md) | Chiplet-module-system-data-center hierarchy | Research |
| 02 | [Tantalum-Silicon Qubits](papers/02_Tantalum_Silicon_Qubits_v2.md) | Qubit platform and device physics | Research |
| 03 | [Error Correction at 100:1](papers/03_Error_Correction_100to1_v2.md) | QEC overhead reduction path | Research |
| 04 | [Photonic Interconnects](papers/04_Photonic_Interconnects_v2.md) | Inter-module communication | Research |
| 05 | [AI Decoding](papers/05_AI_Decoding_v2.md) | Neural decoder architecture | Research |
| 06 | [Software Stack](papers/06_Software_Stack_v2.md) | Orchestration, runtime, and control surfaces | Implemented + Research |
| 07 | [Cryogenic Infrastructure](papers/07_Cryogenic_Infrastructure_v2.md) | Thermal and facility engineering | Research |
| 08 | [Quantum Algorithms](papers/08_Quantum_Algorithms_v2.md) | Application benchmarks and workload classes | Research |
| 09 | [Benchmarking](papers/09_Benchmarking_v2.md) | Measurement methodology and evidence structure | Implemented + Research |
| 10 | [Roadmap 2030](papers/10_Roadmap_2030_v2.md) | Gated development plan | Research |

### Program Roadmap

The [5-phase roadmap](roadmap/ROADMAP_2030.md) outlines base, aggressive, and stretch development paths.

| Phase | Timeline | Base | Aggressive | Stretch |
| --- | --- | --- | --- | --- |
| Foundation | 2025-2026 | Platform + benchmarks | First hardware validation | Stretch device evidence |
| Sputnik | 2026-2027 | Small modular hardware | 10k-qubit module | Stretch module target |
| Pioneer | 2027-2028 | Distributed runtime | Multi-module demos | 100k physical qubit path |
| Horizon | 2028-2029 | Modular platform | 100k physical + 1k logical | 500k physical + 5k logical |
| Summit | 2029-2030 | Commercial platform | Large FT machine | 1M physical + 10k logical |

## Canonical Architecture

| Tier | Unit | Physical Qubits | Logical Qubits (100:1 stretch) |
| --- | --- | ---: | ---: |
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

| Repository | Role |
| --- | --- |
| [qontos](https://github.com/qontos/qontos) | Flagship SDK and public developer entry point |
| [qontos-sim](https://github.com/qontos/qontos-sim) | Simulators, digital twin, and tensor-network modeling |
| [qontos-examples](https://github.com/qontos/qontos-examples) | Tutorials, notebooks, and runnable workflows |
| [qontos-benchmarks](https://github.com/qontos/qontos-benchmarks) | Evidence and methodology for public claims |

## License

Apache License 2.0. See [LICENSE](LICENSE).

---

<p align="center">
  <sub>QONTOS · Hybrid superconducting-photonic quantum computing · Built by Zhyra Quantum Research Institute (ZQRI)</sub>
</p>
