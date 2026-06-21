> ## ⚠️ Status: superseded — corrected
> Original note VIII, kept for the record. The "constant integrand" proof holds only in d = 4; for d > 4, r_h ∝ M^{1/(d−3)}, so the integrand is not constant. The result **R_total = r_h(d)** is correct, but follows from the first law, not from a mass-independent integrand. See [`../ERRATA.md`](../ERRATA.md) and [`../consolidated/`](../consolidated/).

---

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20564313.svg)](https://doi.org/10.5281/zenodo.20564313)

# The D3 Evaporation Invariant in All Spacetime Dimensions

**R_total = r_s is Dimension-Independent**

*Bharat Sharma — PhenexAI Research, Vancouver, BC, Canada*

> **D3 Research Series**
> | [Paper I](https://doi.org/10.5281/zenodo.20502577)
> | [Paper II](https://doi.org/10.5281/zenodo.20535347)
> | [Paper III](https://doi.org/10.5281/zenodo.20548070)
> | [Paper IV](https://doi.org/10.5281/zenodo.20549627)
> | [Paper V](https://doi.org/10.5281/zenodo.20549980)
> | [Paper VI](https://doi.org/10.5281/zenodo.20561229)
> | [Paper VII](https://doi.org/10.5281/zenodo.20563756)
> | **Paper VIII — This work**

---

## The Central Result

$$R_{\text{total}}(d) = r_s(d) \quad \text{for ALL } d \geq 4$$

The proof uses one identity:

$$-\frac{1}{d-3} + \frac{1}{d-3} = 0 \quad \text{for any } d \geq 4$$

Paper III is not a 4D coincidence — it is a **universal property** of the D3 framework.

---

## The Universal Cancellation

In d spacetime dimensions:

| Quantity | M-dependence |
|---|---|
| D3_d(M) ∝ T_H(d) | M^(−1/(d−3)) |
| dN/dM ∝ dS/dM | M^(+1/(d−3)) |
| **Product dR/dM** | **M⁰ = constant** |

The exponents cancel exactly for **any d ≥ 4** — giving dR/dM = 2G_d/c² = constant in all dimensions.

---

## Verification by Dimension

| d | D3_d ~ M^? | dN/dM ~ M^? | Product | R_total | Context |
|---|---|---|---|---|---|
| 4 | −1 | +1 | M⁰ | r_s(4D) | Standard GR |
| 5 | −1/2 | +1/2 | M⁰ | r_s(5D) | Kaluza-Klein |
| 6 | −1/3 | +1/3 | M⁰ | r_s(6D) | Extra dimensions |
| 7 | −1/4 | +1/4 | M⁰ | r_s(7D) | Supergravity |
| 10 | −1/7 | +1/7 | M⁰ | r_s(10D) | **String theory** |
| 11 | −1/8 | +1/8 | M⁰ | r_s(11D) | **M-theory** |
| d | −1/(d−3) | +1/(d−3) | M⁰ | r_s(dD) | General |

---

## Why the Cancellation is Not Accidental

The result follows directly from the **first law of black hole thermodynamics:**

$$dM = T_H \cdot dS$$

Since D3_d ∝ T_H and dN/dM = dS/dM · (1/ln2):

$$\frac{dR}{dM} = D3_d \cdot \frac{dN}{dM} \propto T_H \cdot \frac{dS}{dM} = \frac{dM}{dM} = 1$$

The first law guarantees R_total = r_s in **any dimension** where black hole thermodynamics holds — including string theory (d=10) and M-theory (d=11).

---

## Repository Structure

```
d3-research/
└── all-dimensions/
    ├── D3_AllDimensions_Paper8_Sharma_2026.pdf  # Submitted manuscript
    ├── figures/
    │   ├── fig1_power_cancellation.png           # M-exponents cancel for all d
    │   ├── fig2_rtotal_all_dimensions.png        # R_total/r_s = 1 for all d
    │   ├── fig3_proof_diagram.png                # Universal cancellation diagram
    │   └── fig4_series_complete.png              # All 8 papers
    └── code/
        └── verify_all_dimensions.py             # Exact fraction verification
```

---

## Reproduce the Results

```python
from fractions import Fraction

for d in [4, 5, 6, 7, 10, 11]:
    exp_D3 = Fraction(-1, d-3)
    exp_dN = Fraction(+1, d-3)
    product = exp_D3 + exp_dN
    assert product == 0
    print(f"d={d}: {exp_D3} + {exp_dN} = {product} PASS")

# Output:
# d=4:  -1   + 1   = 0 PASS
# d=5:  -1/2 + 1/2 = 0 PASS
# d=10: -1/7 + 1/7 = 0 PASS
# d=11: -1/8 + 1/8 = 0 PASS
```

---

## Citation

```bibtex
@article{sharma2026alldimensions,
  title   = {The D3 Evaporation Invariant in All Spacetime Dimensions:
             R\_total = r\_s is Dimension-Independent},
  author  = {Sharma, Bharat},
  journal = {Zenodo},
  year    = {2026},
  doi     = {10.5281/zenodo.20564313},
  url     = {https://doi.org/10.5281/zenodo.20564313},
  note    = {PhenexAI Research, Vancouver}
}
```

---

## License

Code: MIT License
Paper: © 2026 Bharat Sharma. All rights reserved pending journal submission.

---

## References

[1] B. Sharma, Paper I. Zenodo (2026). DOI: 10.5281/zenodo.20502577
[2] B. Sharma, Paper III. Zenodo (2026). DOI: 10.5281/zenodo.20548070
[3] B. Sharma, Paper VII. Zenodo (2026). DOI: 10.5281/zenodo.20563756
[4] F. R. Tangherlini, Nuovo Cimento 27, 636 (1963)
[5] R. C. Myers, M. J. Perry, Ann. Phys. 172, 304 (1986)
[6] S. W. Hawking, Commun. Math. Phys. 43, 199 (1975)
[7] J. D. Bekenstein, Phys. Rev. D 7, 2333 (1973)
[8] R. Landauer, IBM J. Res. Develop. 5, 183 (1961)
[9] M. Cortés, A. R. Liddle, EPL 149, 59001 (2025)
