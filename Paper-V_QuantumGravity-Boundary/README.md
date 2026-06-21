> ## ⚠️ Status: superseded
> Original note V, kept for the record. Superseded by the consolidated treatment of the evaporation invariant. See [`../ERRATA.md`](../ERRATA.md) and [`../consolidated/`](../consolidated/).

---

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20549980.svg)](https://doi.org/10.5281/zenodo.20549980)

# A Quantum Gravity Boundary from the D3 Framework

**The Scale at Which Information Erasure Cost Exceeds the Schwarzschild Radius**

*Bharat Sharma — PhenexAI Research, Vancouver, BC, Canada*

> **D3 Research Series**
> | [Paper I — D3 Original](https://doi.org/10.5281/zenodo.20502577)
> | [Paper II — Kerr Extension](https://doi.org/10.5281/zenodo.20535347)
> | [Paper III — Schwarzschild Invariant](https://doi.org/10.5281/zenodo.20548070)
> | [Paper IV — Kerr Invariant](https://doi.org/10.5281/zenodo.20549627)
> | **Paper V — This work (Series Complete)**

---

## The Central Results

$$M_{QG} = m_P \sqrt{\frac{\ln 2}{8\pi}} = 0.166071\, m_P$$

$$\frac{D3(M)}{r_s(M)} = \left(\frac{M_{QG}}{M}\right)^2 \quad \text{[exact power law]}$$

$$M_{QG}(\chi) = M_{QG} \cdot \sqrt{f(\chi)} \quad \text{[Kerr extension]}$$

Below M_QG, each bit erased costs more geometry than the entire black hole — classical GR breaks down.

---

## The Quantum Gravity Boundary

| Quantity | Value |
|---|---|
| M_QG | 0.166071 m_P |
| r_QG | 0.332141 l_P |
| T_QG | 0.239589 T_P |

This is **not** the Planck mass — it is a specific sub-Planckian scale determined by ln2 and 8π, the information-theoretic and geometric constants of the D3 framework.

---

## The Exact Power Law

| M/M_QG | D3/r_s | Exact value | Regime |
|---|---|---|---|
| 0.001 | 1,000,000 | 10⁶ | Quantum gravity |
| 0.01 | 10,000 | 10⁴ | Quantum gravity |
| 0.1 | 100 | 10² | Quantum gravity |
| 0.5 | 4 | 4 | Quantum gravity |
| **1.0** | **1** | **1** | **Boundary** |
| 2.0 | 0.25 | 1/4 | Classical GR |
| 10 | 0.01 | 10⁻² | Classical GR |
| 1000 | 0.000001 | 10⁻⁶ | Classical GR |

Exact integers at rational mass fractions — verified to 10 significant figures.

---

## Kerr Extension

$$M_{QG}(\chi) = M_{QG} \cdot \sqrt{f(\chi)}$$

| χ | f(χ) | M_QG(χ)/m_P | r_QG(χ)/l_P |
|---|---|---|---|
| 0.00 | 1.000000 | 0.166071 | 0.332141 |
| 0.50 | 0.928203 | 0.159998 | 0.319996 |
| 0.67 | 0.852132 | 0.153224 | 0.306448 |
| 0.90 | 0.607136 | 0.129400 | 0.258801 |
| 0.99 | 0.247255 | 0.082578 | 0.165156 |
| 1.00 | 0.000000 | 0.000000 | 0.000000 |

At χ→1 (extremal): M_QG→0 — an extremal Kerr black hole has **no quantum gravity boundary**, consistent with zero Hawking temperature.

---

## Two Planck-Scale Identities from One Framework

| Paper | Identity | Condition |
|---|---|---|
| I | D3 = 2·ln(2)·l_P | T = T_P (Planck temperature) |
| V | D3 = r_s | M = M_QG = 0.166071 m_P |

Same formula. Two distinct Planck-scale results.

---

## Complete D3 Series — One Framework, Five Results

| Paper | Result |
|---|---|
| I | Δr_s = 2G·k_B·T·ln2/c⁴ + Planck coincidence |
| II | f(χ) = 2√(1−χ²)/(1+√(1−χ²)) |
| III | R_total = r_s |
| IV | R_total(Kerr) = f(χ)·r_s |
| V | M_QG = 0.166071 m_P, D3/r_s = (M_QG/M)² |

**All five results derived from D3 = 2Gk_BT·ln2/c⁴. All constants cancel in every proof.**

---

## Repository Structure

```
d3-research/
└── qg-boundary/
    ├── D3_QG_Boundary_Paper5_Sharma_2026.pdf  # Submitted manuscript
    ├── figures/
    │   ├── fig1_qg_boundary.png                # D3/r_s power law across 35 decades
    │   ├── fig2_power_law.png                  # Exact integers at rational fractions
    │   ├── fig3_kerr_extension.png             # M_QG(chi) shrinking with spin
    │   └── fig4_series_summary.png             # All 5 papers unified diagram
    └── code/
        └── verify_qg_boundary.py              # Numerical verification
```

---

## Reproduce the Results

```bash
git clone https://github.com/bsharma173860-oss/d3-research.git
cd d3-research/qg-boundary/code
pip install numpy matplotlib
python verify_qg_boundary.py
# Output:
# M_QG/m_P = 0.166071
# Power law verified
# Kerr extension verified
```

---

## Citation

```bibtex
@article{sharma2026qgboundary,
  title   = {A Quantum Gravity Boundary from the D3 Framework:
             The Scale at Which Information Erasure Cost Exceeds
             the Schwarzschild Radius},
  author  = {Sharma, Bharat},
  journal = {Zenodo},
  year    = {2026},
  doi     = {10.5281/zenodo.20549980},
  url     = {https://doi.org/10.5281/zenodo.20549980},
  note    = {PhenexAI Research, Vancouver}
}
```

---

## License

Code: MIT License
Paper: © 2026 Bharat Sharma. All rights reserved pending journal submission.

---

## References

[1] B. Sharma, Paper II. Zenodo (2026). DOI: 10.5281/zenodo.20535347
[2] B. Sharma, Paper III. Zenodo (2026). DOI: 10.5281/zenodo.20548070
[3] B. Sharma, Paper I. Zenodo (2026). DOI: 10.5281/zenodo.20502577
[4] B. Sharma, Paper IV. Zenodo (2026). DOI: 10.5281/zenodo.20549627
[5] S. W. Hawking, Commun. Math. Phys. 43, 199 (1975)
[6] J. D. Bekenstein, Phys. Rev. D 7, 2333 (1973)
[7] R. Landauer, IBM J. Res. Develop. 5, 183 (1961)
[8] M. Cortés, A. R. Liddle, EPL 149, 59001 (2025)
