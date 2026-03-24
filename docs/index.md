# QONTOS Research — Documentation Index

Welcome to the QONTOS research documentation. This page serves as the landing page for all public research materials produced by the QONTOS quantum computing program.

Use the [Public Registry](https://github.com/qontos/.github/blob/main/docs/public-registry.md) for the shared map across the public SDK, simulator, examples, benchmark, and research repos.

## Research Materials

### Technical Whitepaper

The QONTOS Technical Whitepaper documents the implemented orchestration platform and the modular research program.

- [Markdown](../whitepaper/QONTOS_Technical_Whitepaper.md)
- [IEEE LaTeX](../whitepaper/QONTOS_Technical_Whitepaper_IEEE.tex)

### Research Paper Series (v2)

The 10-paper series covers the full QONTOS stack from architecture through devices, error correction, interconnects, software, and the 2030 roadmap.

| # | Paper | Topic |
|---|-------|-------|
| 01 | [Scaled Architecture](../papers/01_QONTOS_Scaled_Architecture_v2.md) | Chiplet-module-system-datacenter hierarchy |
| 02 | [Tantalum-Silicon Qubits](../papers/02_Tantalum_Silicon_Qubits_v2.md) | Qubit platform and device physics |
| 03 | [Error Correction at 100:1](../papers/03_Error_Correction_100to1_v2.md) | QEC overhead reduction path |
| 04 | [Photonic Interconnects](../papers/04_Photonic_Interconnects_v2.md) | Inter-module communication |
| 05 | [AI Decoding](../papers/05_AI_Decoding_v2.md) | Neural decoder architecture |
| 06 | [Software Stack](../papers/06_Software_Stack_v2.md) | Orchestration and runtime |
| 07 | [Cryogenic Infrastructure](../papers/07_Cryogenic_Infrastructure_v2.md) | Thermal and facility engineering |
| 08 | [Quantum Algorithms](../papers/08_Quantum_Algorithms_v2.md) | Application benchmarks |
| 09 | [Benchmarking](../papers/09_Benchmarking_v2.md) | Measurement methodology |
| 10 | [Roadmap 2030](../papers/10_Roadmap_2030_v2.md) | Gated development plan |

### Program Roadmap

The [5-Phase Development Roadmap](../roadmap/ROADMAP_2030.md) outlines the gated program with base, aggressive, and stretch scenarios from Foundation (2025) through Summit (2030).

### Figures

Architecture diagrams, system charts, and publication-ready figures are available in [`figures/`](../figures/).

## QONTOS Ecosystem

| Repository | Description |
| :--- | :--- |
| [qontos](https://github.com/qontos/qontos) | Flagship Python SDK for quantum circuit orchestration |
| [qontos-sim](https://github.com/qontos/qontos-sim) | Simulators, digital twin, and tensor-network engine |
| [qontos-benchmarks](https://github.com/qontos/qontos-benchmarks) | Benchmark framework and reproducible evidence |
| [qontos-examples](https://github.com/qontos/qontos-examples) | Tutorials, notebooks, and runnable examples |
| [qontos-research](https://github.com/qontos/qontos-research) | This repository — research papers and roadmap |

## Quick Links

- **What's open today:** Software platform, simulators, benchmarks, examples
- **What's in development:** Native modular superconducting quantum hardware
- **Stretch roadmap:** 1,000,000 physical qubits and 10,000 logical qubits by 2030

## Citation

If you reference QONTOS research, please cite using the [CITATION.cff](../CITATION.cff) file or the BibTeX entry in the [README](../README.md#citation).

## License

Apache License 2.0. See [LICENSE](../LICENSE).
