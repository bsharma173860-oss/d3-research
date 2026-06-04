[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20502577.svg)](https://doi.org/10.5281/zenodo.20502577) — D3 Original
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20535347.svg)](https://doi.org/10.5281/zenodo.20535347) — Kerr Extension
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20548070.svg)](https://doi.org/10.5281/zenodo.20548070) — Invariant (Paper III)

# Geometric Cost of Information Erasure — D3 Research Series

**A Schwarzschild-Radius Formulation of the Landauer–Einstein–Schwarzschild Identity**

*Bharat Sharma — PhenexAI Research, Vancouver, BC, Canada*

---

## The D3 Formula

$$\Delta r_s = \frac{2G \cdot k_B \cdot T \cdot \ln 2}{c^4}$$

This formula gives the perturbative Schwarzschild-radius shift of a black hole that loses one Landauer-worth of mass at temperature $T$. It combines three independently confirmed physical results:

| Result | Expression | Confirmed |
|---|---|---|
| Landauer's Principle | $E \geq k_B T \ln 2$ | Bérut et al., *Nature* 2012 |
| Mass–Energy Equivalence | $m = E/c^2$ | Einstein 1905 |
| Perturbative Schwarzschild shift | $\Delta r_s = 2G\Delta M/c^2$ | LIGO 2016 |

---

## The Planck Coincidence

At the Planck temperature $T_P = \sqrt{\hbar c^5 / G k_B^2}$, all physical constants cancel:

$$\Delta r_s(T_P) = 2 \ln(2) \cdot \ell_P \quad \text{[exact]}$$

where $\ell_P = \sqrt{\hbar G / c^3}$ is the Planck length. Verified numerically:

```
Computed:  Delta-r_s(T_P) / l_P  =  1.386294
Expected:  2 * ln(2)             =  1.386294
```

---

## Numerical Scale

| Physical Context | Temperature [K] | Δr_s [m/bit] | Δr_s / ℓ_P |
|---|---|---|---|
| Cosmic microwave background | 2.725 | 4.31 × 10⁻⁶⁶ | 2.67 × 10⁻³¹ |
| Room temperature | 300 | 4.74 × 10⁻⁶⁵ | 2.93 × 10⁻³⁰ |
| Human body temperature | 310 | 4.90 × 10⁻⁶⁵ | 3.03 × 10⁻³⁰ |
| Hawking temp. (solar mass) | 6.17 × 10⁻⁸ | 9.75 × 10⁻⁷⁵ | 6.03 × 10⁻⁴⁰ |
| LHC quark-gluon plasma | 5.5 × 10¹² | 8.70 × 10⁻⁵⁵ | 5.38 × 10⁻²⁰ |
| **Planck temperature** | **1.42 × 10³²** | **2·ln(2)·ℓ_P** | **2 ln 2 (exact)** |

---

## Repository Structure

```
d3-research/
├── paper/
│   └── D3_Paper_Final_v5_Sharma_2026.pdf   # Submitted manuscript
├── figures/
│   ├── fig1_derivation_flow.png             # Three-step derivation diagram
│   ├── fig2_dr_vs_T.png                     # Delta-r_s vs temperature (log-log)
│   └── fig4_planck_coincidence.png          # Planck coincidence proof figure
├── code/
│   ├── generate_figures.py                  # Reproduces all paper figures
│   └── verify_planck_coincidence.py         # Numerical verification of exact identity
├── data/
│   └── scale_hierarchy.csv                  # Table 1 values (CODATA 2018)
└── README.md
```

---

## Reproduce the Results

```bash
git clone https://github.com/bsharma173860-oss/d3-research.git
cd d3-research
pip install matplotlib numpy
python code/generate_figures.py
python code/verify_planck_coincidence.py
```

All results are reproducible from the formula and CODATA 2018 constants. No external data or proprietary tools required.

---

## Paper II — Kerr Extension

**Spin-Dependent Information-Geometry in Rotating Black Holes: Kerr Extension of the D3 Formula and a Universal Spin-Suppression Factor**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20535347.svg)](https://doi.org/10.5281/zenodo.20535347)

Extends D3 to rotating (Kerr) black holes. The exact spin-suppression factor:

$$f(\chi) = \frac{2\sqrt{1-\chi^2}}{1 + \sqrt{1-\chi^2}}$$

is **universal** — mass-independent to 10 significant figures. At χ=0 recovers D3 exactly; at χ→1 (extremal) f→0.

| χ | f(χ) | Physical context |
|---|---|---|
| 0.00 | 1.000 | Schwarzschild (non-rotating) |
| 0.67 | 0.852 | GW150914 remnant |
| 0.90 | 0.607 | GRS 1915+105 |
| 0.99 | 0.247 | Near-extremal |

📄 Full paper: [kerr_paper/](kerr_paper/)

---

## Paper III — Schwarzschild Radius as Invariant

**The Schwarzschild Radius as an Information-Geometry Invariant: Total D3 Displacement over Complete Hawking Evaporation**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20548070.svg)](https://doi.org/10.5281/zenodo.20548070)

The total D3 displacement over complete Hawking evaporation equals **exactly** the Schwarzschild radius:

$$R_{\text{total}} = \int_0^{M_0} D3(M)\, dN(M) = \frac{2GM_0}{c^2} = r_s(M_0) \quad \text{[exact]}$$

Five constants cancel (M, ℏ, k_B, ln2, π) — only G and c survive. The universal displacement rate:

$$\frac{dR}{dM} = \frac{2G}{c^2} = 1.485 \times 10^{-27} \text{ m/kg}$$

is constant across all masses, temperatures, and times. Verified across 24 decades of mass.

| Black Hole | r_s(M₀) [m] | R_total [m] | Ratio |
|---|---|---|---|
| Primordial (10¹¹ kg) | 1.49 × 10⁻¹⁶ | 1.49 × 10⁻¹⁶ | 1.00000 |
| Stellar (1 M☉) | 2.95 × 10³ | 2.95 × 10³ | 1.00001 |
| Supermassive (4×10⁶ M☉) | 1.18 × 10¹⁰ | 1.18 × 10¹⁰ | 1.00001 |

📄 Full paper: [rs-invariant/](rs-invariant/)

---

## Relation to Prior Work

This paper makes explicit a Schwarzschild-radius statement implicit in prior work:

- **Cortés & Liddle (2024)** — *EPL 149, 59001* — established the per-bit mass loss $\Delta M = k_B T_H \ln 2 / c^2$ but did not write the radius form
- **Kim, Lee & Lee (2010)** — *Mod. Phys. Lett. A 25, 1581* — showed black holes are maximally efficient Landauer erasers; derived mass-loss but not radius form
- **Herrera (2020)** — *Entropy 22, 340* — introduced $M_\text{bit} = k_B T \ln 2 / c^2$ at arbitrary $T$; D3 is $\Delta r_s = (2G/c^2) \cdot M_\text{bit}$
- **Bagchi, Ghosh & Sen (2024)** — *Gen. Relativ. Gravit. 56, 108* — Kerr extension via area quantisation

The exact Planck coincidence $\Delta r_s(T_P) = 2 \ln 2 \cdot \ell_P$ has not appeared in the mass or area formulations of prior work.

---

## Collaboration

This research is being prepared for submission to *Europhysics Letters* (EPL) or *Physics Letters B*.

I am actively seeking collaboration with researchers who have:
- Expertise in black-hole thermodynamics or information theory
- Access to GPU compute clusters for related AI/physics simulation work
- Interest in extending this result to Kerr and Reissner–Nordström geometries

**Contact:** bharatsharma@phenex.ai

If you are affiliated with UBC, SFU, or another BC institution and are interested in discussing this work or a potential collaboration, please reach out.

---

## Citation

**Paper I — D3 Original:**
```bibtex
@article{sharma2026d3,
  title   = {Geometric Cost of Information Erasure: A Schwarzschild-Radius
             Formulation of the Landauer-Einstein-Schwarzschild Identity},
  author  = {Sharma, Bharat},
  journal = {Zenodo},
  year    = {2026},
  doi     = {10.5281/zenodo.20502577},
  url     = {https://doi.org/10.5281/zenodo.20502577},
  note    = {PhenexAI Research, Vancouver}
}
```

**Paper II — Kerr Extension:**
```bibtex
@article{sharma2026kerr,
  title   = {Spin-Dependent Information-Geometry in Rotating Black Holes:
             Kerr Extension of the D3 Formula and a Universal Spin-Suppression Factor},
  author  = {Sharma, Bharat},
  journal = {Zenodo},
  year    = {2026},
  doi     = {10.5281/zenodo.20535347},
  url     = {https://doi.org/10.5281/zenodo.20535347},
  note    = {PhenexAI Research, Vancouver}
}
```

**Paper III — Invariant:**
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

---

## License

Code: MIT License  
Paper: © 2026 Bharat Sharma. All rights reserved pending journal submission.
