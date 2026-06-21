> ## ⚠️ Status: superseded
> Original note III, kept for the record. The result **R_total = r_s** is correct; in the consolidated paper it is re-derived directly from the first law of black-hole mechanics and framed as an exact identity rather than new dynamics. See [`../ERRATA.md`](../ERRATA.md) and [`../consolidated/`](../consolidated/).

---

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20548070.svg)](https://doi.org/10.5281/zenodo.20548070)

# The Schwarzschild Radius as an Information-Geometry Invariant

**Total D3 Displacement over Complete Hawking Evaporation**

*Bharat Sharma — PhenexAI Research, Vancouver, BC, Canada*

> **Part of the D3 Research Series**
> | [Paper I — D3 Original](https://doi.org/10.5281/zenodo.20502577)
> | [Paper II — Kerr Extension](https://doi.org/10.5281/zenodo.20535347)
> | **Paper III — This work**

---

## The Central Result

$$R_{\text{total}} = \int_0^{M_0} D3(M)\, dN(M) = \frac{2GM_0}{c^2} = r_s(M_0) \quad \text{[exact]}$$

The total accumulated D3 information-geometry displacement over **complete Hawking evaporation** equals exactly the initial Schwarzschild radius. Five independent constants cancel — only G and c survive.

---

## The Five Cancellations

| Quantity | Cancels? |
|---|---|
| Mass M | ✓ cancels |
| Planck constant ℏ | ✓ cancels |
| Boltzmann constant k_B | ✓ cancels |
| ln(2) | ✓ cancels |
| π | ✓ cancels |
| **G and c** | **survive** |

The integrand reduces to a **universal constant:**

$$\frac{dR}{dM} = D3(M) \cdot \frac{dN}{dM} = \frac{2G}{c^2} = 1.485 \times 10^{-27} \text{ m/kg}$$

Mass-independent. Temperature-independent. Constant across all 26 decades of mass.

---

## Derivation in 6 Steps

| Step | Operation | Result |
|---|---|---|
| 1 | D3 at Hawking temperature | D3(M) = ℏln(2)/(4πMc) |
| 2 | Bekenstein entropy in bits | S(M) = 4πGM²/(ℏc·ln2) |
| 3 | Bits lost per unit mass | dN/dM = 8πGM/(ℏc·ln2) |
| 4 | Product D3 × dN/dM | M, ℏ, ln2, π all cancel |
| 5 | Result | dR/dM = 2G/c² (universal) |
| 6 | Integrate 0 → M₀ | R_total = 2GM₀/c² = r_s ✓ |

---

## Numerical Verification

Verified across **24 decades of mass** to five significant figures:

| Black Hole | M₀ | r_s(M₀) [m] | R_total [m] | Ratio |
|---|---|---|---|---|
| Primordial | 10¹¹ kg | 1.49 × 10⁻¹⁶ | 1.49 × 10⁻¹⁶ | 1.00000 |
| Stellar | 1 M☉ | 2.95 × 10³ | 2.95 × 10³ | 1.00001 |
| Stellar | 10 M☉ | 2.95 × 10⁴ | 2.95 × 10⁴ | 1.00001 |
| Supermassive | 4×10⁶ M☉ | 1.18 × 10¹⁰ | 1.18 × 10¹⁰ | 1.00001 |
| Planck mass | 2.18 × 10⁻⁸ kg | 3.23 × 10⁻³⁵ | 3.23 × 10⁻³⁵ | 1.00000 |

*Deviation from unity is numerical integration error, not analytical error.*

---

## Physical Interpretation

The Schwarzschild radius has traditionally been understood as a **geometric boundary** — the point of no return for infalling matter.

This result provides a second, independent interpretation:

> **r_s(M₀) is the exact total information-geometry displacement accumulated by Landauer erasure over complete Hawking evaporation.**

These two meanings are physically distinct but numerically identical. The geometric boundary and the information-thermodynamic cost are the same quantity.

### Connection to the Information Paradox

If information were truly destroyed during evaporation, R_total could in principle differ from r_s. Our result shows they are equal — the geometric accounting is exact and complete.

### Geometric Equipartition

Every kilogram of mass lost contributes exactly **2G/c²** of geometric displacement — regardless of the black hole's temperature, size, or age.

---

## Repository Structure

```
d3-research/
└── rs-invariant/
    ├── D3_Invariant_Paper3_Sharma_2026.pdf   # Submitted manuscript
    ├── figures/
    │   ├── fig1_universal_rate.png            # dR/dM = 2G/c² across 26 decades
    │   ├── fig2_rtotal_vs_rs.png              # R_total = r_s across 24 decades
    │   ├── fig3_derivation_flow.png           # Five cancellations diagram
    │   └── fig4_physical_interpretation.png   # Cumulative displacement vs shrinking horizon
    └── code/
        └── verify_invariant.py                # Numerical verification
```

---

## Reproduce the Results

```bash
git clone https://github.com/bsharma173860-oss/d3-research.git
cd d3-research/rs-invariant/code
pip install numpy matplotlib
python verify_invariant.py
# Output: R_total/r_s = 1.00001 for all masses
```

---

## Relation to Prior Work

- **Sharma (2026) Paper I** — D3 formula established the per-bit horizon-radius shift. This paper integrates it over complete evaporation.
- **Sharma (2026) Paper II** — Kerr extension. This paper is the Schwarzschild global result; Kerr global extension is future work.
- **Bekenstein (1973)** — Bekenstein entropy provides the dN/dM term. D3 and Bekenstein entropy combine with exact cancellations to give r_s.
- **Cortés & Liddle (2024)** — Established Hawking evaporation saturates the Landauer bound locally. This result is the global version: total geometric cost over complete evaporation equals r_s.
- **Page (1993)** — Page time marks when half the information is radiated. Our result is time-independent — a statement about total displacement, not its rate.

---

## Citation

```bibtex
@article{sharma2026invariant,
  title   = {The Schwarzschild Radius as an Information-Geometry Invariant:
             Total D3 Displacement over Complete Hawking Evaporation},
  author  = {Sharma, Bharat},
  journal = {Zenodo},
  year    = {2026},
  doi     = {10.5281/zenodo.20548070},
  url     = {https://doi.org/10.5281/zenodo.20548070},
  note    = {PhenexAI Research, Vancouver}
}
```

*DOI will be updated upon Zenodo publication.*

---

## License

Code: MIT License
Paper: © 2026 Bharat Sharma. All rights reserved pending journal submission.

---

## References

[1] B. Sharma, "Geometric Cost of Information Erasure," Zenodo (2026). DOI: 10.5281/zenodo.20502577
[2] B. Sharma, "Kerr Extension of the D3 Formula," Zenodo (2026). DOI: 10.5281/zenodo.20535347
[3] J. D. Bekenstein, Phys. Rev. D 7, 2333 (1973)
[4] S. W. Hawking, Commun. Math. Phys. 43, 199 (1975)
[5] S. W. Hawking, Phys. Rev. D 14, 2460 (1976)
[6] D. N. Page, Phys. Rev. Lett. 71, 3743 (1993)
[7] M. Cortés, A. R. Liddle, EPL 149, 59001 (2025)
[8] R. Landauer, IBM J. Res. Develop. 5, 183 (1961)
