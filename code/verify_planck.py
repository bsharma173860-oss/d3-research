"""
verify_planck.py
Numerically verifies: Delta-r_s(T_P) / l_P = 2 * ln(2) [exact]
Usage: python verify_planck.py
"""
import numpy as np

G    = 6.67430e-11
c    = 2.99792458e8
hbar = 1.054571817e-34
k_B  = 1.380649e-23
l_P  = np.sqrt(hbar * G / c**3)
T_P  = np.sqrt(hbar * c**5 / (G * k_B**2))

def d3(T):
    return 2 * G * k_B * T * np.log(2) / c**4

print("=" * 55)
print("D3 Formula — Planck Coincidence Verification")
print("=" * 55)
print(f"l_P = {l_P:.6e} m")
print(f"T_P = {T_P:.6e} K")
print()
computed = d3(T_P) / l_P
expected = 2 * np.log(2)
print(f"Computed: Delta-r_s(T_P) / l_P = {computed:.10f}")
print(f"Expected: 2 * ln(2)            = {expected:.10f}")
print(f"Match: {np.isclose(computed, expected, rtol=1e-10)}")
print()
print("Scale Hierarchy:")
cases = [
    ("CMB",              2.725),
    ("Room temp",        300),
    ("Body temp",        310),
    ("Hawking (solar)",  6.17e-8),
    ("LHC plasma",       5.5e12),
    ("Planck",           T_P),
]
for name, T in cases:
    dr = d3(T)
    if T == T_P:
        print(f"  {name:<20} T={T:.3e} K  ->  2*ln(2)*l_P  [exact]")
    else:
        print(f"  {name:<20} T={T:.3e} K  ->  {dr:.3e} m  ({dr/l_P:.3e} l_P)")
print("=" * 55)
