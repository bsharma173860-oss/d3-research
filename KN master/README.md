[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20563756.svg)](https://doi.org/10.5281/zenodo.20563756)

# The Kerr-Newman Information-Geometry Master Formula

**Unification of Spin and Charge Suppression in the D3 Framework**

*Bharat Sharma — PhenexAI Research, Vancouver, BC, Canada*

> **D3 Research Series — Complete**
> | [Paper I](https://doi.org/10.5281/zenodo.20502577)
> | [Paper II](https://doi.org/10.5281/zenodo.20535347)
> | [Paper III](https://doi.org/10.5281/zenodo.20548070)
> | [Paper IV](https://doi.org/10.5281/zenodo.20549627)
> | [Paper V](https://doi.org/10.5281/zenodo.20549980)
> | [Paper VI](https://doi.org/10.5281/zenodo.20561229)
> | **Paper VII — Capstone**

---

## The Master Formula

$$\sigma = \sqrt{1 - \chi^2 - q^2}$$

$$h(\chi, q) = \frac{4\sigma}{2(1+\sigma) - q^2}$$

$$R_{\text{total}}(\text{KN}) = h(\chi, q) \cdot r_s(M_0) \quad \text{[exact, all masses]}$$

The Kerr-Newman metric is the **most general stationary black hole in 4D GR**. This is the most general result possible in the D3 framework. **The series is complete.**

---

## All Previous Results Are Exact Special Cases

| Condition | Result | Paper |
|---|---|---|
| χ=0, q=0 | h=1 → R_total = r_s | I, III |
| q=0 | h=f(χ) = 2√(1−χ²)/(1+√(1−χ²)) | II, IV |
| χ=0 | h=g(q) = 4√(1−q²)/(1+√(1−q²))² | VI |
| χ²+q²→1 | h→0 → R_total→0 | All |
| **general** | **h(χ,q) — this paper** | **VII** |

---

## The Key Identity

$$\sigma^2 + \chi^2 = 1 - q^2$$

This generalises the Paper 2 identity s²+χ²=1 to the charged case. It collapses the denominator:

$$(1+\sigma)^2 + \chi^2 = 2(1+\sigma) - q^2$$

Verified for **625 parameter combinations** to machine precision.

---

## Why h ≠ f·g

The natural conjecture h=f·g is **wrong** in general:

| (χ, q) | h(χ,q) | f(χ)·g(q) | Difference |
|---|---|---|---|
| (0.5, 0.5) | 0.893880 | 0.923419 | ≠ |
| (0.7, 0.3) | 0.808539 | 0.832773 | ≠ |

Spin and charge interact in the KN geometry — they are not independent. The correct formula contains an interaction term through q² in the denominator.

---

## Numerical Results

| χ | q | σ | h(χ,q) | R_total/r_s | Note |
|---|---|---|---|---|---|
| 0.0 | 0.0 | 1.000 | 1.000000 | 1.000000 | Schwarzschild |
| 0.5 | 0.0 | 0.866 | 0.928203 | 0.928203 | Kerr f(χ) |
| 0.0 | 0.5 | 0.866 | 0.994845 | 0.994845 | RN g(q) |
| 0.5 | 0.5 | 0.707 | 0.893880 | 0.893880 | KN — new |
| 0.7 | 0.3 | 0.648 | 0.808539 | 0.808539 | KN — new |
| 0.3 | 0.7 | 0.648 | 0.923792 | 0.923792 | KN — new |
| 0.9 | 0.0 | 0.436 | 0.607136 | 0.607136 | Kerr f(0.9) |
| 0.0 | 0.9 | 0.436 | 0.845658 | 0.845658 | RN g(0.9) |

---

## Repository Structure

```
d3-research/
└── kn-master/
    ├── D3_KN_Master_Paper7_Sharma_2026.pdf   # Submitted manuscript
    ├── figures/
    │   ├── fig1_h_parameter_space.png         # h(chi,q) over full spin-charge space
    │   ├── fig2_special_cases.png             # f(chi) and g(q) as slices of h
    │   ├── fig3_key_identity.png              # sigma^2+chi^2=1-q^2 verified
    │   └── fig4_series_complete.png           # All 7 papers unified diagram
    └── code/
        └── verify_kn_master.py               # Full verification of all results
```

---

## Reproduce the Results

```bash
git clone https://github.com/bsharma173860-oss/d3-research.git
cd d3-research/kn-master/code
pip install numpy matplotlib
python verify_kn_master.py
# Output:
# h(chi,0) = f(chi) verified
# h(0,q) = g(q) verified
# Key identity verified for 625 combinations
# R_total = h*rs verified
# All verified.
```

---

## Citation

```bibtex
@article{sharma2026knmaster,
  title   = {The Kerr-Newman Information-Geometry Master Formula:
             Unification of Spin and Charge Suppression
             in the D3 Framework},
  author  = {Sharma, Bharat},
  journal = {Zenodo},
  year    = {2026},
  doi     = {10.5281/zenodo.20563756},
  url     = {https://doi.org/10.5281/zenodo.20563756},
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
[2] B. Sharma, Paper IV. Zenodo (2026). DOI: 10.5281/zenodo.20549627
[3] B. Sharma, Paper I. Zenodo (2026). DOI: 10.5281/zenodo.20502577
[4] B. Sharma, Paper III. Zenodo (2026). DOI: 10.5281/zenodo.20548070
[5] B. Sharma, Paper V. Zenodo (2026). DOI: 10.5281/zenodo.20549980
[6] B. Sharma, Paper VI. Zenodo (2026). DOI: 10.5281/zenodo.20561229
[7] S. W. Hawking, Commun. Math. Phys. 43, 199 (1975)
[8] J. D. Bekenstein, Phys. Rev. D 7, 2333 (1973)
[9] E. T. Newman et al., J. Math. Phys. 6, 918 (1965)
[10] R. Landauer, IBM J. Res. Develop. 5, 183 (1961)
[11] M. Cortés, A. R. Liddle, EPL 149, 59001 (2025)
