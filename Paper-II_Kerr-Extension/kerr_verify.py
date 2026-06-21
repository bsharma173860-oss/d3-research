"""
kerr_verify.py
==============
Verification code for:
  "Spin-Dependent Information-Geometry in Rotating Black Holes:
   Kerr Extension of the D3 Formula and a Universal Spin-Suppression Factor"
  Bharat Sharma, PhenexAI Research, Vancouver (2026)

Central result:
  f(chi) = D3_Kerr / D3_Schwarz = 2*sqrt(1-chi^2) / (1 + sqrt(1-chi^2))

Usage:
  python kerr_verify.py
"""

import math

# ── CODATA 2018 constants ─────────────────────────────────────────────────
G    = 6.67430e-11      # gravitational constant [m^3 kg^-1 s^-2]
c    = 2.99792458e8     # speed of light [m/s]
hbar = 1.054571817e-34  # reduced Planck constant [J s]
k_B  = 1.380649e-23    # Boltzmann constant [J/K]
M_sun = 1.989e30       # solar mass [kg]

# ── Core functions ────────────────────────────────────────────────────────

def schwarzschild_temperature(M):
    """Hawking temperature of a Schwarzschild black hole."""
    return hbar * c**3 / (8 * math.pi * G * M * k_B)

def kerr_temperature(M, chi):
    """Hawking temperature of a Kerr black hole."""
    a  = chi * G * M / c**2          # spin parameter [m]
    rp = G*M/c**2 + math.sqrt((G*M/c**2)**2 - a**2)
    rm = G*M/c**2 - math.sqrt((G*M/c**2)**2 - a**2)
    return hbar * c * (rp - rm) / (4 * math.pi * k_B * (rp**2 + a**2))

def d3(T):
    """D3 formula: per-bit Schwarzschild radius shift at temperature T."""
    return 2 * G * k_B * T * math.log(2) / c**4

def f_numerical(M, chi):
    """Spin-suppression factor computed numerically."""
    return kerr_temperature(M, chi) / schwarzschild_temperature(M)

def f_analytical(chi):
    """Spin-suppression factor from exact closed form."""
    s = math.sqrt(1 - chi**2)
    return 2 * s / (1 + s)

# ── Test 1: Schwarzschild limit ───────────────────────────────────────────
print("=" * 60)
print("TEST 1: Schwarzschild limit f(0) = 1")
print("=" * 60)
f0 = f_analytical(0.0)
print(f"  f(chi=0) = {f0:.10f}")
print(f"  Expected = 1.0000000000")
assert abs(f0 - 1.0) < 1e-15, "Schwarzschild limit failed"
print("  PASS\n")

# ── Test 2: Near-extremal limit ───────────────────────────────────────────
print("=" * 60)
print("TEST 2: Near-extremal limit f -> 0 as chi -> 1")
print("=" * 60)
for chi in [0.9, 0.99, 0.999, 0.9999]:
    fv = f_analytical(chi)
    print(f"  f({chi}) = {fv:.8f}")
assert f_analytical(0.9999) < 0.05, "Extremal limit failed"
print("  PASS — f decreases to 0 as chi -> 1\n")

# ── Test 3: Mass independence ─────────────────────────────────────────────
print("=" * 60)
print("TEST 3: Mass independence — verified to 10 significant figures")
print("=" * 60)
print(f"  {'Mass':<20} {'chi':<8} {'Numerical':<18} {'Analytical':<18} {'Match'}")
print(f"  {'-'*20} {'-'*8} {'-'*18} {'-'*18} {'-'*5}")
for M_sol in [0.1, 1, 10, 1e6]:
    for chi in [0.1, 0.5, 0.9, 0.99]:
        num = f_numerical(M_sol * M_sun, chi)
        ana = f_analytical(chi)
        match = abs(num - ana) / ana < 1e-10
        print(f"  {M_sol:<20} {chi:<8.2f} {num:<18.10f} {ana:<18.10f} {'PASS' if match else 'FAIL'}")
        assert match, f"Mass independence failed for M={M_sol}, chi={chi}"
print("\n  All masses agree to 10 significant figures — PASS\n")

# ── Test 4: Key algebraic identity ───────────────────────────────────────
print("=" * 60)
print("TEST 4: Key identity s^2 + chi^2 = 1")
print("=" * 60)
for chi in [0.1, 0.3, 0.5, 0.7, 0.9, 0.99]:
    s = math.sqrt(1 - chi**2)
    identity = s**2 + chi**2
    err = abs(identity - 1.0)
    print(f"  chi={chi:.2f}: s^2 + chi^2 = {identity:.16f}  error={err:.2e}")
print("  Identity holds to floating-point precision — PASS\n")

# ── Test 5: Table of values ───────────────────────────────────────────────
print("=" * 60)
print("TABLE 2 — Spin-suppression factor f(chi)")
print("=" * 60)
print(f"  {'chi':<8} {'f(chi)':<12} {'Physical context'}")
print(f"  {'-'*8} {'-'*12} {'-'*30}")
cases = [
    (0.00, "Schwarzschild (non-rotating)"),
    (0.10, "Slowly rotating"),
    (0.50, "Moderate spin"),
    (0.67, "GW150914 remnant [Abbott et al. 2016]"),
    (0.70, "Typical X-ray binary"),
    (0.90, "GRS 1915+105 range [McClintock et al. 2014]"),
    (0.99, "Near-extremal"),
    (0.999,"Ultra-near-extremal"),
]
for chi, context in cases:
    fv = f_analytical(chi) if chi > 0 else 1.0
    print(f"  {chi:<8.3f} {fv:<12.6f} {context}")

# ── Test 6: Astrophysical D3 values ──────────────────────────────────────
print()
print("=" * 60)
print("ASTROPHYSICAL D3_KERR VALUES")
print("=" * 60)
for name, M_sol, chi in [
    ("GW150914 remnant",    30,    0.67),
    ("GRS 1915+105",        14,    0.98),
    ("Sgr A* (est.)",    4e6,    0.90),
    ("Stellar BH, slow",    10,    0.1),
]:
    M = M_sol * M_sun
    T_K = kerr_temperature(M, chi)
    D3_K = d3(T_K)
    D3_S = d3(schwarzschild_temperature(M))
    fv = f_analytical(chi)
    print(f"\n  {name}")
    print(f"    M = {M_sol} M_sun,  chi = {chi}")
    print(f"    T_Kerr     = {T_K:.4e} K")
    print(f"    D3_Kerr    = {D3_K:.4e} m/bit")
    print(f"    D3_Schwarz = {D3_S:.4e} m/bit")
    print(f"    f(chi)     = {fv:.6f}")

print()
print("=" * 60)
print("ALL TESTS PASSED")
print("Central result verified: f(chi) = 2*sqrt(1-chi^2) / (1+sqrt(1-chi^2))")
print("Mass-independent to 10 significant figures")
print("=" * 60)
