[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20549627.svg)](https://doi.org/10.5281/zenodo.20549627)

# Spin-Suppressed Evaporation Invariant

**Total D3 Displacement for Kerr Black Holes and Unification of the D3 Research Series**

*Bharat Sharma — PhenexAI Research, Vancouver, BC, Canada*

> **D3 Research Series**
> | [Paper I — D3 Original](https://doi.org/10.5281/zenodo.20502577)
> | [Paper II — Kerr Extension](https://doi.org/10.5281/zenodo.20535347)
> | [Paper III — Schwarzschild Invariant](https://doi.org/10.5281/zenodo.20548070)
> | **Paper IV — This work (Unification)**

---

## The Central Result

$$R_{\text{total}}(\text{Kerr}) = f(\chi) \cdot r_s(M_0) = f(\chi) \cdot \frac{2GM_0}{c^2} \quad \text{[exact]}$$

where:

$$f(\chi) = \frac{2\sqrt{1-\chi^2}}{1 + \sqrt{1-\chi^2}}$$

Five constants cancel (M, ℏ, k_B, ln2, π) — only G, c, and f(χ) survive.

---

## Unification of the D3 Series

| Level | Result | Paper |
|---|---|---|
| Per-bit, Schwarzschild | Δr_s = 2G·k_B·T·ln2/c⁴ | I |
| Per-bit, Kerr | D3_Kerr/D3_Schwarz = f(χ) | II |
| Global, χ=0 | R_total = r_s | III |
| **Global, χ>0** | **R_total = f(χ)·r_s** | **IV ← this work** |

Paper IV contains Papers II and III as exact special cases.

---

## Exact Limits

| Limit | χ | Result | Physical meaning |
|---|---|---|---|
| Schwarzschild | 0 | R_total = r_s | Paper III recovered exactly |
| Extremal | →1 | R_total → 0 | Zero Hawking temperature |

---

## Astrophysical Results

| Black Hole | Mass | χ | f(χ) | r_s [m] | R_total [m] |
|---|---|---|---|---|---|
| GW150914 remnant | 30 M☉ | 0.67 | 0.852 | 8.87 × 10⁴ | 7.56 × 10⁴ |
| GRS 1915+105 | 14 M☉ | 0.98 | 0.332 | 4.14 × 10⁴ | 1.37 × 10⁴ |
| Sgr A* | 4×10⁶ M☉ | 0.90 | 0.607 | 1.18 × 10¹⁰ | 7.17 × 10⁹ |
| Slow stellar | 10 M☉ | 0.10 | 0.997 | 2.95 × 10⁴ | 2.95 × 10⁴ |
| Schwarzschild | 1 M☉ | 0.00 | 1.000 | 2.95 × 10³ | 2.95 × 10³ |

---

## Derivation in 7 Steps

| Step | Operation | Result |
|---|---|---|
| 1 | D3_Kerr at Hawking temperature | = f(χ)·ℏln2/(4πMc) |
| 2 | Bekenstein bit-loss rate | dN/dM = 8πGM/(ℏc·ln2) |
| 3 | Product D3_Kerr × dN/dM | f(χ) factors out |
| 4 | M cancels | ✓ |
| 5 | ℏ cancels | ✓ |
| 6 | ln2 cancels | ✓ |
| 7 | π cancels | dR/dM = f(χ)·2G/c² |
| Integrate | 0 → M₀ | R_total = f(χ)·2GM₀/c² ✓ |

---

## Repository Structure

```
d3-research/
└── kerr-invariant/
    ├── D3_Kerr_Invariant_Paper4_Sharma_2026.pdf  # Submitted manuscript
    ├── figures/
    │   ├── fig1_rtotal_vs_chi.png                 # R_total/r_s = f(chi) for all masses
    │   ├── fig2_unification_diagram.png           # Papers 2,3,4 unified
    │   ├── fig3_displacement_rate.png             # dR/dM = f(chi)*2G/c² for 4 spins
    │   └── fig4_astrophysical_cases.png           # R_total vs r_s for real black holes
    └── code/
        └── verify_kerr_invariant.py               # Numerical verification
```

---

## Reproduce the Results

```bash
git clone https://github.com/bsharma173860-oss/d3-research.git
cd d3-research/kerr-invariant/code
pip install numpy matplotlib
python verify_kerr_invariant.py
# Output: chi=0.00: R/rs=1.00001, f(chi)=1.00000
#         chi=0.50: R/rs=1.00001, f(chi)=0.92820
#         chi=0.90: R/rs=1.00001, f(chi)=0.60714
#         chi=0.99: R/rs=1.00001, f(chi)=0.24726
```

---

## Physical Interpretation

Spinning black holes are **"geometrically cheaper"** to evaporate than non-rotating ones of the same mass. The total information-geometry cost of complete evaporation is f(χ)·r_s — strictly less than r_s for any χ > 0.

This is consistent with the lower Hawking temperature of Kerr black holes: they radiate less energetically at each mass step.

---

## Citation

```bibtex
@article{sharma2026kerrInvariant,
  title   = {Spin-Suppressed Evaporation Invariant: Total D3 Displacement
             for Kerr Black Holes and Unification of the D3 Research Series},
  author  = {Sharma, Bharat},
  journal = {Zenodo},
  year    = {2026},
  doi     = {10.5281/zenodo.20549627},
  url     = {https://doi.org/10.5281/zenodo.20549627},
  note    = {PhenexAI Research, Vancouver}
}
```

---

## License

Code: MIT License
Paper: © 2026 Bharat Sharma. All rights reserved pending journal submission.

---

## References

[1] B. Sharma, Paper II — Kerr Extension. Zenodo (2026). DOI: 10.5281/zenodo.20535347
[2] B. Sharma, Paper III — Schwarzschild Invariant. Zenodo (2026). DOI: 10.5281/zenodo.20548070
[3] B. Sharma, Paper I — D3 Original. Zenodo (2026). DOI: 10.5281/zenodo.20502577
[4] S. W. Hawking, Commun. Math. Phys. 43, 199 (1975)
[5] J. D. Bekenstein, Phys. Rev. D 7, 2333 (1973)
[6] D. N. Page, Phys. Rev. Lett. 71, 3743 (1993)
[7] M. Cortés, A. R. Liddle, EPL 149, 59001 (2025)
