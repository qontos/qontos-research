# Toward Quantum Error Correction at 100:1 Effective Overhead

**Technical Research Paper v2.1**

**Author:** Qontos Research Wing

**Affiliation:** Zhyra Quantum Research Institute (ZQRI), Abu Dhabi, UAE

**Correspondence:** research@zhyra.xyz

---

## Abstract

This paper evaluates a QONTOS path toward low-overhead fault tolerance for modular quantum systems. It compares three overhead regimes - conservative, aggressive, and stretch - and examines the device, decoder, and architecture conditions required for each. The focus is on whether a hybrid code strategy combining practical surface-code ideas with more efficient LDPC-inspired approaches could reduce the physical cost of logical qubits enough to make large modular systems economically and operationally plausible.

**Claim status:** feasibility-envelope paper with a stretch target of 100:1 effective overhead

**Keywords:** quantum error correction, LDPC, surface code, decoder latency, fault-tolerant computing

---

## 1. Introduction

Error-correction overhead is one of the central variables controlling whether large-scale quantum computing is merely scientifically interesting or actually buildable. For QONTOS, overhead is not a standalone coding-theory curiosity. It is the variable that couples:

- architecture scale
- facility size
- power budget
- capex
- algorithm viability

### 1.1 Claim Status Summary

| Claim | Status |
|---|---|
| 1000:1 is a conservative large-scale planning baseline | Derived from literature |
| 300:1 is an aggressive QONTOS target | QONTOS target |
| 100:1 is the QONTOS stretch target | Stretch target |

### 1.2 Why This Matters

For 10,000 logical qubits:

- at 1000:1 overhead: 10,000,000 physical qubits
- at 300:1 overhead: 3,000,000 physical qubits
- at 100:1 overhead: 1,000,000 physical qubits

This is why the QEC story and the architecture story must stay synchronized.

---

## 2. Overhead Scenarios

![Code Structure Tradeoffs](figures_final/03_code_structures.png){ width=100% }

*Figure 1: Surface-code baselines, hybrid-code paths, and stretch targets should be kept conceptually distinct.*

### 2.1 Conservative, Aggressive, and Stretch Cases

| Overhead regime | Meaning | Status |
|---|---|---|
| 1000:1 | conservative planning baseline | Derived from literature |
| 300:1 | aggressive engineering target | QONTOS target |
| 100:1 | stretch architecture enabler | Stretch target |

### 2.2 Hybrid Code Framing

QONTOS is evaluating a hybrid direction:

- surface-code-like strategies where they remain operationally practical
- LDPC-inspired or more efficient coding strategies where connectivity and decoder assumptions permit
- architecture-aware code selection for modular hardware

This is best described as a design exploration that can mature into a production code stack as the program advances.

### 2.3 Architecture Mapping

Using the canonical stretch architecture:

| Layer | Physical qubits | Logical qubits at 100:1 |
|---|---:|---:|
| Chiplet | 2,000 | 20 |
| Module | 10,000 | 100 |
| System | 100,000 | 1,000 |
| Data center | 1,000,000 | 10,000 |

The paper set must keep these counts aligned everywhere.

---

## 3. Decoder and Connectivity Requirements

### 3.1 What 100:1 Would Require

The stretch 100:1 case is not only a code question. It likely also requires:

- lower physical error rates than conservative baselines
- manageable 6-way or similar connectivity
- decoder latency near or below the correction-cycle budget
- tolerance to correlated noise and leakage
- modular operation without excessive communication penalties

### 3.2 Scenario Table

| Variable | Base | Aggressive | Stretch |
|---|---:|---:|---:|
| Effective overhead | 1000:1 | 300:1 | 100:1 |
| Decoder latency | 10 us | 1 us | 500 ns |
| Decoder accuracy | 95% | 99% | 99.99% |
| Physical error | 1e-3 to 1e-4 | around 1e-4 | around 1e-5 |
| Connectivity burden | low to moderate | moderate | high but controlled |

### 3.3 Decoder Performance Interpretation

The decoder table is intended as a scenario ladder for QONTOS:

- `Base`: classical feasibility
- `Aggressive`: engineering target for modular logical qubits
- `Stretch`: required for the 100:1 architecture case

---

## 4. Implementation Strategy

![Overhead Envelope](figures_final/03_error_correction.png){ width=100% }

*Figure 2: Effective overhead should be communicated as a planning envelope with explicit validation gates.*

### 4.1 Syndrome Extraction

At large scale, the decoder and control path is a systems problem:

- syndrome extraction rate
- classical transport bandwidth
- local and global correction timing
- interaction with modular communication

Any low-overhead code strategy that ignores these operational costs is incomplete.

### 4.2 AI-Assisted Decoding

QONTOS can describe AI-assisted decoding as one of the key enablers of the aggressive and stretch cases within the broader QEC program.

Recommended wording:

`QONTOS evaluates AI-assisted decoding as a potential route to reducing practical decoding latency and improving the viability of lower-overhead code families in modular settings.`

---

## 5. Fault-Tolerance Envelope

### 5.1 Threshold Framing

It is reasonable to discuss threshold and margin conceptually, and this paper treats them as one part of a broader architecture picture.

Better framing:

- physical error rate and threshold margin are necessary but not sufficient
- realistic performance also depends on leakage, correlated noise, finite-size effects, and decoder behavior

### 5.2 Logical Error Framing

The previous draft overstated logical performance through simplified asymptotic expressions. The revised paper should say:

`Simplified asymptotic scaling suggests that sufficiently low physical error and sufficient code distance could drive strong logical suppression. However, the practical logical error rate in a modular architecture must be estimated through finite-size analysis, realistic noise models, and decoder-in-the-loop simulation.`

### 5.3 Risks and Failure Modes

Major failure modes include:

- overhead remains far above 300:1
- decoder latency dominates correction cycle time
- correlated noise invalidates simplified suppression assumptions
- modular communication overhead destroys the logical cost advantage

---

## 6. Validation Gates

The low-overhead claim should only be promoted as a serious QONTOS program result once the following are satisfied:

1. a derivation exists for base, aggressive, and stretch overhead cases
2. decoder-in-the-loop simulation supports those cases
3. modular architecture penalties are included
4. first logical-qubit experiments align with the modeled trajectory

### 6.1 Phase-Aligned Gates

| Phase | QEC gate |
|---|---|
| FOUNDATION | conservative baseline and decoder methodology established |
| SPUTNIK | first logical-qubit evidence and correction-cycle model |
| PIONEER | modular logical-qubit demonstrations |
| HORIZON | aggressive overhead case becomes defensible |
| SUMMIT | stretch 100:1 case only if prior gates all pass |

---

## 7. Conclusion

The value of the QONTOS error-correction thesis is real, and it is strongest when communicated precisely. The most technically defensible position today is:

- low-overhead fault tolerance is central to the architecture
- 300:1 is a meaningful aggressive target
- 100:1 remains a stretch target whose feasibility depends on device, decoder, and modular-systems performance improving together

That framing keeps the ambition while making the production plan more technically honest.

---

## References

[1] Representative literature on surface codes, LDPC approaches, and low-overhead fault tolerance.

[2] Representative literature on decoder latency, finite-size effects, and modular fault tolerance.

---

*Document Version: 2.1*  
*Classification: Technical Research Paper*  
*Claim posture: Feasibility envelope for aggressive and stretch QEC targets*
