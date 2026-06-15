# The D3 Framework — Information-Geometry of Black-Hole Evaporation

**Bharat Sharma — Independent Researcher, Vancouver, BC, Canada**
[bharatsharma@phenex.ai](mailto:bharatsharma@phenex.ai)

This repository develops a single information-geometric identity for black holes:
the per-bit Landauer erasure cost, expressed as a horizon-radius shift, integrates
over complete Hawking evaporation to reconstruct the horizon radius itself.

> **Status (2026):** the original nine-note series has been **consolidated into two
> corrected papers** and re-verified end to end. Earlier separate notes are archived
> under [`superseded/`](superseded/); corrections are documented in
> [`ERRATA.md`](ERRATA.md). The central result is an **exact identity** — a
> re-expression of the first law of black hole mechanics — and is presented as an
> interpretive, unifying statement, not a claim of new physics.

## The core formula

$$\Delta r_s = \frac{2G\,k_B\,T\,\ln 2}{c^4}$$

the perturbative Schwarzschild-radius shift from erasing one bit at temperature
*T*, combining Landauer's principle, mass–energy equivalence, and the linearised
Schwarzschild relation. At the Planck temperature it reduces to the exact
identity Δr_s(T_P) = 2 ln2 · ℓ_P.

## Canonical papers

| | Paper | Result | Location |
|---|---|---|---|
| I | Geometric Cost of Information Erasure | Δr_s = 2G k_B T ln2 / c⁴; Planck identity | [`D3_paper/`](D3_paper/) |
| II | The Evaporation Invariant & Generalisations | R_total = r_h (Schwarzschild, Kerr, RN, KN, all *d*, AdS), via the first law | [`consolidated/`](consolidated/) |

The total information-geometry displacement over complete evaporation equals the
outer-horizon radius:

$$R_{\text{total}} = \int_0^{M_0}\frac{dr_h}{dM}\,dM = r_h(M_0),$$

with all quantum constants cancelling. For Schwarzschild this is r_s = 2GM₀/c².
The factors f(χ), g(q), h(χ,q) that appear for spinning/charged holes are ratios
of **Hawking temperatures**, not of integrated displacements (see
[`ERRATA.md`](ERRATA.md)).

## Reproduce / verify

```bash
git clone https://github.com/bsharma173860-oss/d3-research.git
cd d3-research/code
pip install numpy matplotlib sympy
python verify_planck.py
```

## Repository layout

- [`D3_paper/`](D3_paper/) — Paper I (corrected)
- [`consolidated/`](consolidated/) — Paper II (consolidated, corrected)
- [`code/`](code/) — verification / figure scripts
- [`superseded/`](superseded/) — original nine notes, retained for the record
- [`ERRATA.md`](ERRATA.md) — corrections and consolidation notice

## License

Code: MIT. Papers: © 2026 Bharat Sharma.
