# Errata and Consolidation Notice

The D3 research series originally comprised nine separate notes (kept in their own per-paper folders (see the index in the [README](README.md)) and on Zenodo). Following a full internal
re-verification, the series has been **consolidated into two corrected papers**
and several errors in the original notes have been corrected. This document
records those corrections transparently; the Zenodo records remain citable, and
corrected/superseding versions are being issued there.

## Current canonical papers

1. **Paper I — Geometric Cost of Information Erasure** ([`Paper-I_Information-Erasure-Cost/`](Paper-I_Information-Erasure-Cost/))
   The per-bit result Δr_s = 2G·k_B·T·ln2/c⁴ and the Planck-scale identity.
2. **Consolidated paper — The Evaporation Invariant and its Generalisations**
   ([`consolidated/`](consolidated/)) — the total-displacement result
   R_total = r_h, derived via the first law, including the Kerr, Reissner–Nordström,
   Kerr–Newman, higher-dimensional, and AdS cases in a single section.

## Corrections

**Paper I (scale table).** The cosmic-microwave-background row was off by a
power of ten: Δr_s(2.725 K) = 4.31×10⁻⁶⁷ m (not 10⁻⁶⁶) and Δr_s/ℓ_P = 2.67×10⁻³².
The journal-submitted version additionally corrected the Hawking (1 M☉), LHC, and
Hagedorn rows, whose exponents were similarly misstated.

**Paper VIII (all dimensions) — proof error.** The original proof claimed the
product D₃·(dN/dM) is a mass-independent constant in every dimension. This holds
only in d = 4. For d > 4 the horizon radius scales as r_h ∝ M^{1/(d−3)}, so
dr_h/dM is not constant and the "constant integrand" argument instead gives
R_total ∝ M, contradicting R_total = r_s(d). The **result** R_total = r_h(d) is
correct, but follows from the first law (dR/dM = dr_h/dM, integrated), not from a
mass-independent integrand. The corrected derivation is in the consolidated paper.

**Papers II, IV, VI, VII (Kerr / Reissner–Nordström / Kerr–Newman) — conceptual
error.** These used the Schwarzschild Bekenstein bit-count
dN/dM = 8πGM/(ℏc·ln2) for rotating and charged black holes. That entropy is in
fact spin/charge-dependent, so the bit-count is not the Schwarzschild one. The
"R_total = f(χ)·r_s" type results were artifacts of pairing the Kerr temperature
ratio with the Schwarzschild bit-count. Corrected statement: **R_total equals the
actual outer-horizon radius r_h**, and the factors f(χ), g(q), h(χ,q) are ratios
of **Hawking temperatures** (T/T_Schw), not of integrated displacements. See the
consolidated paper, generalisation section.

## Scope of the result

The consolidated result is an **exact identity** — a re-expression of the first
law of black hole mechanics in information-geometric variables. It is presented
as such: an interpretive, unifying statement, not a claim of new dynamics.
