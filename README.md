# The D3 Framework — Information-Geometry of Black-Hole Evaporation

**Bharat Sharma — Independent Researcher, Vancouver, BC, Canada**
[bharatsharma@phenex.ai](mailto:bharatsharma@phenex.ai)

This repository develops a single information-geometric identity for black holes:
the per-bit Landauer erasure cost, expressed as a horizon-radius shift, integrates
over complete Hawking evaporation to reconstruct the horizon radius itself.

> **Status (2026):** the original **nine-paper series** is preserved below, each paper in
> its own folder. Following a full internal re-verification the series was **consolidated
> into two corrected canonical papers**; several original notes contain errors that were
> later corrected. Every folder's README states its status, and all corrections are
> documented in [`ERRATA.md`](ERRATA.md). The central result is an **exact identity** — a
> re-expression of the first law of black-hole mechanics — presented as an interpretive,
> unifying statement, not a claim of new physics.

## The core formula

$$\Delta r_s = \frac{2G\,k_B\,T\,\ln 2}{c^4}$$

the perturbative Schwarzschild-radius shift from erasing one bit at temperature *T*,
combining Landauer's principle, mass–energy equivalence, and the linearised Schwarzschild
relation. At the Planck temperature it reduces to the exact identity Δr_s(T_P) = 2 ln2 · ℓ_P.

## Canonical papers (current)

| | Paper | Result | Folder |
|---|---|---|---|
| I  | Geometric Cost of Information Erasure | Δr_s = 2G k_B T ln2 / c⁴; Planck identity | [`Paper-I_Information-Erasure-Cost/`](Paper-I_Information-Erasure-Cost/) |
| II | The Evaporation Invariant & Generalisations | R_total = r_h (Schwarzschild, Kerr, RN, KN, all *d*, AdS), via the first law | [`consolidated/`](consolidated/) |

## The nine-paper series

Each note has its own folder (paper PDF, figures, README with status). ⚠️ marks notes whose
original results were later corrected — see each README and [`ERRATA.md`](ERRATA.md).

| # | Topic | Status | Folder | Zenodo |
|---|---|---|---|---|
| I    | Information-erasure cost | ✅ canonical (corrected) | [`Paper-I_Information-Erasure-Cost/`](Paper-I_Information-Erasure-Cost/) | [20502577](https://doi.org/10.5281/zenodo.20502577) |
| II   | Kerr extension — f(χ) | ⚠️ superseded (corrected) | [`Paper-II_Kerr-Extension/`](Paper-II_Kerr-Extension/) | [20535347](https://doi.org/10.5281/zenodo.20535347) |
| III  | Schwarzschild invariant R_total = r_s | ⚠️ superseded | [`Paper-III_Schwarzschild-Invariant/`](Paper-III_Schwarzschild-Invariant/) | [20548070](https://doi.org/10.5281/zenodo.20548070) |
| IV   | Kerr invariant / unification | ⚠️ superseded (corrected) | [`Paper-IV_Kerr-Invariant/`](Paper-IV_Kerr-Invariant/) | [20549627](https://doi.org/10.5281/zenodo.20549627) |
| V    | Quantum-gravity boundary scale | ⚠️ superseded | [`Paper-V_QuantumGravity-Boundary/`](Paper-V_QuantumGravity-Boundary/) | [20549980](https://doi.org/10.5281/zenodo.20549980) |
| VI   | Reissner–Nordström — g(q) | ⚠️ superseded (corrected) | [`Paper-VI_Reissner-Nordstrom/`](Paper-VI_Reissner-Nordstrom/) | [20561229](https://doi.org/10.5281/zenodo.20561229) |
| VII  | Kerr–Newman master — h(χ,q) | ⚠️ superseded (corrected) | [`Paper-VII_Kerr-Newman/`](Paper-VII_Kerr-Newman/) | [20563756](https://doi.org/10.5281/zenodo.20563756) |
| VIII | All spacetime dimensions | ⚠️ superseded (corrected) | [`Paper-VIII_All-Dimensions/`](Paper-VIII_All-Dimensions/) | [20564313](https://doi.org/10.5281/zenodo.20564313) |
| IX   | AdS–Schwarzschild | ⚠️ superseded | [`Paper-IX_AdS-Schwarzschild/`](Paper-IX_AdS-Schwarzschild/) | [20567233](https://doi.org/10.5281/zenodo.20567233) |

The total information-geometry displacement over complete evaporation equals the
outer-horizon radius, R_total = r_h(M₀); for Schwarzschild this is r_s = 2GM₀/c².
The factors f(χ), g(q), h(χ,q) are ratios of **Hawking temperatures**, not of integrated
displacements (see [`ERRATA.md`](ERRATA.md)).

## Reproduce / verify

```bash
git clone https://github.com/bsharma173860-oss/d3-research.git
cd d3-research/code
pip install numpy matplotlib sympy
python verify_planck.py
```

## Repository layout

- `Paper-I_…` through `Paper-IX_…` — the nine papers, each with its PDF, figures, and a status README
- [`consolidated/`](consolidated/) — Paper II (consolidated, corrected canonical generalisations)
- [`code/`](code/) — verification / figure scripts
- [`ERRATA.md`](ERRATA.md) — corrections and consolidation notice
- [`docs/`](docs/) — collaboration notes

## License

Code: MIT. Papers: © 2026 Bharat Sharma.
