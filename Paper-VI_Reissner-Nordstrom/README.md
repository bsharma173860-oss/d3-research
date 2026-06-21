> ## ⚠️ Status: superseded — corrected
> Original note VI, kept for the record. The charge-suppression factor **g(q)** was an artifact of using the Schwarzschild bit-count for a charged hole. Corrected statement: **R_total = r_h**, with g(q) a Hawking-temperature ratio. See [`../ERRATA.md`](../ERRATA.md) and [`../consolidated/`](../consolidated/).

---

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20561229.svg)](https://doi.org/10.5281/zenodo.20561229)

# Charge-Suppressed Information-Geometry in Reissner-Nordström Black Holes

**The D3 Charge-Suppression Factor and its Relation to the Kerr Spin-Suppression**

*Bharat Sharma — PhenexAI Research, Vancouver, BC, Canada*

> **D3 Research Series**
> | [Paper I — D3 Original](https://doi.org/10.5281/zenodo.20502577)
> | [Paper II — Kerr Extension](https://doi.org/10.5281/zenodo.20535347)
> | [Paper III — Schwarzschild Invariant](https://doi.org/10.5281/zenodo.20548070)
> | [Paper IV — Kerr Invariant](https://doi.org/10.5281/zenodo.20549627)
> | [Paper V — QG Boundary](https://doi.org/10.5281/zenodo.20549980)
> | **Paper VI — This work → Paper VII: Kerr-Newman**

---

## The Central Results

$$g(q) = \frac{4\sqrt{1-q^2}}{(1+\sqrt{1-q^2})^2}$$

$$R_{\text{total}}(\text{RN}) = g(q) \cdot r_s(M_0) \quad \text{[exact]}$$

$$g(q) = \frac{f(q)^2}{\sqrt{1-q^2}} \quad \text{[exact algebraic relation to Kerr]}$$

where q = Q/M is the dimensionless charge parameter (0 ≤ q < 1).

---

## Charge-Suppression Factor

| q | g(q) | R_total/r_s | Context |
|---|---|---|---|
| 0.00 | 1.000000 | 1.000000 | Schwarzschild (Paper III recovered) |
| 0.10 | 0.999994 | 0.999994 | Tiny charge |
| 0.30 | 0.999444 | 0.999444 | Small charge |
| 0.50 | 0.994845 | 0.994845 | Moderate charge |
| 0.70 | 0.972190 | 0.972190 | Significant charge |
| 0.90 | 0.845658 | 0.845658 | Large charge |
| 0.99 | 0.433375 | 0.433375 | Near-extremal |
| 1.00 | 0.000000 | 0.000000 | Extremal (T=0) |

---

## The Algebraic Pattern — Path to Paper VII

Both suppression factors share the same denominator structure **(1+s)ⁿ** with s = √(1−x²):

| Factor | Formula | Denominator power | Paper |
|---|---|---|---|
| Kerr f(χ) | 2s/(1+s)¹ | n = 1 | II |
| RN g(q) | 4s/(1+s)² | n = 2 | VI |
| Kerr-Newman h(χ,q) | ??? | n = ? | **VII** |

Exact relation: **g(q) = f(q)²/√(1−q²)**

This algebraic connection between charge and spin suppression is the key result pointing toward Paper VII.

---

## RN Quantum Gravity Boundary

$$M_{QG}(q) = M_{QG} \cdot \sqrt{g(q)}$$

| q | g(q) | M_QG(q)/m_P | r_QG(q)/l_P |
|---|---|---|---|
| 0.00 | 1.000000 | 0.166071 | 0.332141 |
| 0.50 | 0.994845 | 0.165643 | 0.331285 |
| 0.70 | 0.972190 | 0.163745 | 0.327490 |
| 0.90 | 0.845658 | 0.152718 | 0.305436 |
| 0.99 | 0.433375 | 0.109326 | 0.218652 |
| 1.00 | 0.000000 | 0.000000 | 0.000000 |

---

## Derivation in 4 Steps

| Step | Operation | Result |
|---|---|---|
| 1 | RN horizons r±= M(1±√(1−q²)) | s = √(1−q²) |
| 2 | T_RN/T_Schwarz | = 4s/(1+s)² = g(q) |
| 3 | D3_RN × dN/dM | g(q) factors out, M,ℏ,ln2,π cancel |
| 4 | Integrate 0→M₀ | R_total = g(q)·r_s ✓ |

---

## Repository Structure

```
d3-research/
└── rn-charge/
    ├── D3_RN_Paper6_Sharma_2026.pdf          # Submitted manuscript
    ├── figures/
    │   ├── fig1_gq_vs_fchi.png               # g(q) vs f(chi) comparison
    │   ├── fig2_rtotal_rn.png                # R_total = g(q)*r_s for 4 charge values
    │   ├── fig3_exact_relation.png           # g = f^2/s verified numerically
    │   └── fig4_series_diagram.png           # D3 series Papers 1-6
    └── code/
        └── verify_rn_charge.py              # Numerical verification
```

---

## Reproduce the Results

```bash
git clone https://github.com/bsharma173860-oss/d3-research.git
cd d3-research/rn-charge/code
pip install numpy matplotlib
python verify_rn_charge.py
# Output:
# Relation g = f^2/s verified
# q=0.00: R_total/r_s = 1.00001
# q=0.50: R_total/r_s = 1.00001
# q=0.90: R_total/r_s = 1.00001
# q=0.99: R_total/r_s = 1.00001
```

---

## Citation

```bibtex
@article{sharma2026rncharge,
  title   = {Charge-Suppressed Information-Geometry in
             Reissner-Nordstr{\"o}m Black Holes: The D3
             Charge-Suppression Factor and its Relation to
             the Kerr Spin-Suppression},
  author  = {Sharma, Bharat},
  journal = {Zenodo},
  year    = {2026},
  doi     = {10.5281/zenodo.20561229},
  url     = {https://doi.org/10.5281/zenodo.20561229},
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
[4] B. Sharma, Paper V — QG Boundary. Zenodo (2026). DOI: 10.5281/zenodo.20549980
[5] B. Sharma, Paper IV — Kerr Invariant. Zenodo (2026). DOI: 10.5281/zenodo.20549627
[6] S. W. Hawking, Commun. Math. Phys. 43, 199 (1975)
[7] J. D. Bekenstein, Phys. Rev. D 7, 2333 (1973)
[8] R. Landauer, IBM J. Res. Develop. 5, 183 (1961)
[9] M. Cortés, A. R. Liddle, EPL 149, 59001 (2025)
