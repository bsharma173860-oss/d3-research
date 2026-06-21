> ## ⚠️ Status: superseded — corrected
> Original note II of the D3 nine-paper series, kept for the record. The spin-suppression factor **f(χ)** was an artifact of pairing the Kerr temperature ratio with the *Schwarzschild* bit-count. Corrected statement: **R_total = r_h** (the actual outer-horizon radius), with f(χ) reinterpreted as a ratio of Hawking temperatures. See [`../ERRATA.md`](../ERRATA.md) and the corrected [`../consolidated/`](../consolidated/) paper.

---

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20535347.svg)](https://doi.org/10.5281/zenodo.20535347)

# Kerr Extension of the D3 Formula

**Spin-Dependent Information-Geometry in Rotating Black Holes: Kerr Extension of the D3 Formula and a Universal Spin-Suppression Factor**

*Bharat Sharma — PhenexAI Research, Vancouver, BC, Canada*

> **Part of the D3 Research Series** | Paper I: [D3 Original](https://doi.org/10.5281/zenodo.20502577) | Paper II: This work

---

## The Spin-Suppression Factor

$$f(\chi) = \frac{2\sqrt{1-\chi^2}}{1 + \sqrt{1-\chi^2}}$$

where χ = a/M is the dimensionless spin parameter (0 ≤ χ < 1).

This gives the ratio of the D3 horizon-radius shift for a Kerr black hole to its Schwarzschild counterpart at the same mass:

$$f(\chi) = \frac{\Delta r_\text{Kerr}}{\Delta r_\text{Schwarz}} = \frac{T_\text{Kerr}}{T_\text{Schwarz}}$$

**Key property:** f(χ) is universal — it depends only on spin, not on black hole mass.

---

## Derivation in 5 Steps

Starting from the Kerr Hawking temperature and the D3 formula [1]:

| Step | Operation | Result |
|---|---|---|
| 1 | Define s = √(1−χ²) in geometrised units | s² + χ² = 1 |
| 2 | Outer horizon | r₊ = 1 + s |
| 3 | Numerator: r₊ − r₋ | = 2s |
| 4 | Denominator: r₊² + a² | = 2(1+s) [key identity] |
| 5 | Ratio T_Kerr / T_Schwarz | = 2s/(1+s) = f(χ) ✓ |

The identity **s² + χ² = 1** is the key algebraic step that collapses the denominator.

---

## Exact Limits

| Limit | χ | f(χ) | Physical meaning |
|---|---|---|---|
| Schwarzschild | 0 | 1.000 | D3 recovered exactly |
| Near-extremal | 1 − ε | ~2√(2ε) | Approaches zero |
| Extremal | →1 | →0 | T_Kerr → 0 |

---

## Numerical Results

| χ | f(χ) | Physical context |
|---|---|---|
| 0.00 | 1.000000 | Schwarzschild (non-rotating) |
| 0.10 | 0.997487 | Slowly rotating |
| 0.50 | 0.928203 | Moderate spin |
| 0.67 | 0.852132 | GW150914 remnant [Abbott et al. 2016] |
| 0.70 | 0.833236 | Typical X-ray binary |
| 0.90 | 0.607136 | GRS 1915+105 [McClintock et al. 2014] |
| 0.99 | 0.247255 | Near-extremal |
| 0.999 | 0.085593 | Ultra-near-extremal |

Mass independence verified to **10 significant figures** across 0.1 to 10⁶ solar masses.

---

## Repository Structure

```
d3-research/
└── kerr_paper/
    ├── Kerr_D3_Final_Sharma_2026.pdf        # Submitted manuscript
    ├── figures/
    │   ├── fig1_spin_suppression.png         # Universal f(chi) curve
    │   ├── fig2_mass_independence.png        # f(chi,M) vs analytical f(chi)
    │   ├── fig3_limits_verification.png      # Schwarzschild & extremal limits
    │   └── fig4_derivation_flow.png          # Algebraic derivation diagram
    └── code/
        └── verify_kerr_suppression.py        # Mass independence verification
```

---

## Reproduce the Results

```bash
git clone https://github.com/bsharma173860-oss/d3-research.git
cd d3-research/kerr_paper/code
pip install numpy matplotlib
python verify_kerr_suppression.py
# Output: Mass independence verified to 10 significant figures
```

---

## Relation to Prior Work

- **Sharma (2026) [D3 Original]** — established Δr_s = 2G·k_B·T·ln(2)/c⁴ for Schwarzschild black holes. This paper extends that result to Kerr geometry.
- **Bagchi, Ghosh & Sen (2024)** — *Gen. Relativ. Gravit. 56, 108* — Kerr extension via area quantisation; their per-bit energy includes angular momentum emission (Ω_H·ΔJ). D3_Kerr gives only the thermal horizon-radius shift at fixed spin. The two results are complementary, not contradictory.
- **Cortés & Liddle (2024)** — *EPL 149, 59001* — established per-bit mass loss; D3 Kerr extends this to rotating geometry.

---

## Astrophysical Context

For **GW150914** (χ ~ 0.67), the D3 shift is suppressed to **85%** of the Schwarzschild value.
For **GRS 1915+105** (χ > 0.98), suppression exceeds **80%**.
For **Sgr A*** (χ ~ 0.9), f ~ 0.607.

---

## Citation

```bibtex
@article{sharma2026kerr,
  title   = {Spin-Dependent Information-Geometry in Rotating Black Holes:
             Kerr Extension of the D3 Formula and a Universal
             Spin-Suppression Factor},
  author  = {Sharma, Bharat},
  journal = {Zenodo},
  year    = {2026},
  doi     = {10.5281/zenodo.20535347},
  url     = {https://doi.org/10.5281/zenodo.20535347},
  note    = {PhenexAI Research, Vancouver}
}
```

---

## License

Code: MIT License
Paper: © 2026 Bharat Sharma. All rights reserved pending journal submission.

---

## References

[1] B. Sharma, "Geometric Cost of Information Erasure," Zenodo (2026). DOI: 10.5281/zenodo.20502577
[2] M. Cortés, A. R. Liddle, EPL 149, 59001 (2025)
[3] B. Bagchi, A. Ghosh, S. Sen, Gen. Relativ. Gravit. 56, 108 (2024)
[4] J. E. McClintock et al., Space Sci. Rev. 183, 295 (2014)
[5] B. P. Abbott et al. (LIGO), Phys. Rev. Lett. 116, 061102 (2016)
[6] S. W. Hawking, Commun. Math. Phys. 43, 199 (1975)
