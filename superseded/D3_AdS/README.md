[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20567233.svg)](https://doi.org/10.5281/zenodo.20567233)

# Information-Geometry of AdS-Schwarzschild Black Holes

**An Exact AdS Correction to the D3 Evaporation Invariant and its Holographic CFT Interpretation**

*Bharat Sharma — PhenexAI Research, Vancouver, BC, Canada*

> **D3 Research Series**
> | [Paper I](https://doi.org/10.5281/zenodo.20502577)
> | [Paper II](https://doi.org/10.5281/zenodo.20535347)
> | [Paper III](https://doi.org/10.5281/zenodo.20548070)
> | [Paper IV](https://doi.org/10.5281/zenodo.20549627)
> | [Paper V](https://doi.org/10.5281/zenodo.20549980)
> | [Paper VI](https://doi.org/10.5281/zenodo.20561229)
> | [Paper VII](https://doi.org/10.5281/zenodo.20563756)
> | [Paper VIII](https://doi.org/10.5281/zenodo.20564313)
> | **Paper IX — This work**

---

## The Central Result

$$R_{\text{total}}(\text{AdS}) = r_s + \frac{r_s^3}{L^2} = r_s\left(1 + \left(\frac{r_s}{L}\right)^2\right)$$

$$\phi(x) = 1 + x^2, \quad x = r_s/L$$

At L→∞: Paper III recovered exactly. At r_s=L (Hawking-Page): **R_total = 2r_s exactly.**

---

## Holographic Decomposition

The two terms have distinct CFT meanings:

| Term | Expression | CFT meaning |
|---|---|---|
| Vacuum | r_s | Zero-temperature contribution |
| Thermal | r_s³/L² | ∝ T³_CFT — Stefan-Boltzmann (3D CFT) |

**At the Hawking-Page transition (r_s = L):**
$$\text{Vacuum term} = \text{Thermal term} = r_s$$

This is a sharp CFT prediction: **at deconfinement, thermal information cost = vacuum information cost exactly.**

---

## φ as a Holographic Observable

$$\phi = \frac{R_{\text{total}}}{r_s^{\text{vacuum}}} = 1 + \left(\frac{T_{\text{CFT}}}{T_{\text{HP}}}\right)^2 \pi^2$$

| Phase | T_CFT | φ | Physical meaning |
|---|---|---|---|
| Confined | < T_HP | ~1 | Thermal cost negligible |
| **Deconfinement** | **= T_HP** | **= 2** | **Equal contributions** |
| Plasma | >> T_HP | ~T² | Thermal cost dominates |

---

## Exact Integer Values

| x = r_s/L | φ(x) | R_total/r_s | Context |
|---|---|---|---|
| 0 | 1 | 1 (exact) | Flat space — Paper III |
| 1 | 2 | 2 (exact) | Hawking-Page transition |
| √2 | 3 | 3 (exact) | r_s = √2·L |
| 2 | 5 | 5 (exact) | r_s = 2L |
| √(n−1) | n | n (exact) | General integer pattern |

---

## Connection to Free Energy

The Hawking-Page free energy ΔF ∝ r_s²(r_s²−L²)/(GL²) vanishes at r_s=L — exactly where our correction term r_s³/L² equals r_s (φ=2). The D3 result is consistent with the thermodynamic phase structure.

---

## Repository Structure

```
d3-research/
└── ads-correction/
    ├── D3_AdS_Paper9_Sharma_2026.pdf         # Submitted manuscript
    ├── figures/
    │   ├── fig1_phi_correction.png            # φ(x) = 1+x² with integer values
    │   ├── fig2_numerical_verification.png    # Numerical vs analytical R_total/r_s
    │   ├── fig3_cft_phases.png                # Three CFT phases diagram
    │   └── fig4_series_diagram.png            # D3 series Papers 1-9
    └── code/
        └── verify_ads_correction.py          # Numerical verification
```

---

## Reproduce the Results

```bash
git clone https://github.com/bsharma173860-oss/d3-research.git
cd d3-research/ads-correction/code
pip install numpy matplotlib
python verify_ads_correction.py
# Output:
# x=0.001: ratio=1.0000
# x=0.100: ratio=1.0000
# x=0.500: ratio=1.0000
# x=1.000: ratio=1.0000
# x=2.000: ratio=1.0000
```

---

## Citation

```bibtex
@article{sharma2026ads,
  title   = {Information-Geometry of AdS-Schwarzschild Black Holes:
             An Exact AdS Correction to the D3 Evaporation Invariant
             and its Holographic CFT Interpretation},
  author  = {Sharma, Bharat},
  journal = {Zenodo},
  year    = {2026},
  doi     = {10.5281/zenodo.20567233},
  url     = {https://doi.org/10.5281/zenodo.20567233},
  note    = {PhenexAI Research, Vancouver}
}
```

---

## License

Code: MIT License
Paper: © 2026 Bharat Sharma. All rights reserved pending journal submission.

---

## References

[1] B. Sharma, Paper III. Zenodo (2026). DOI: 10.5281/zenodo.20548070
[2] B. Sharma, Paper VIII. Zenodo (2026). DOI: 10.5281/zenodo.20564313
[3] B. Sharma, Paper I. Zenodo (2026). DOI: 10.5281/zenodo.20502577
[4] J. M. Maldacena, Int. J. Theor. Phys. 38, 1113 (1999)
[5] S. W. Hawking, D. N. Page, Commun. Math. Phys. 87, 577 (1983)
[6] E. Witten, Adv. Theor. Math. Phys. 2, 505 (1998)
[7] J. D. Bekenstein, Phys. Rev. D 7, 2333 (1973)
[8] R. Landauer, IBM J. Res. Develop. 5, 183 (1961)
[9] M. Cortés, A. R. Liddle, EPL 149, 59001 (2025)
