"""
generate_figures.py
-------------------
Reproduces all figures from:
  "Geometric Cost of Information Erasure"
  Sharma (2026), PhenexAI Research

Usage:
    python generate_figures.py

Output:
    ../figures/fig1_derivation_flow.png
    ../figures/fig2_dr_vs_T.png
    ../figures/fig4_planck_coincidence.png
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'figures')
os.makedirs(OUT, exist_ok=True)

# CODATA 2018 constants
G    = 6.67430e-11      # m^3 kg^-1 s^-2
c    = 2.99792458e8     # m s^-1
hbar = 1.054571817e-34  # J s
k_B  = 1.380649e-23     # J K^-1
l_P  = 1.616255e-35     # m  (Planck length)
T_P  = 1.416784e32      # K  (Planck temperature)


def d3(T):
    """D3 formula: Schwarzschild-radius shift per bit at temperature T."""
    return 2 * G * k_B * T * np.log(2) / c**4


# ── Figure 1: Derivation flow diagram ────────────────────────────────────────
print("Generating Fig 1 (derivation flow)...")

fig, ax = plt.subplots(figsize=(8, 5))
ax.axis('off')
fig.patch.set_facecolor('#FAFAF7')

boxes = [
    (0.06, 0.52, "Landauer's Principle\n$E = k_B T \\ln 2$\n(Landauer 1961;\nBérut et al. 2012)", '#1F3864'),
    (0.38, 0.52, "Mass-Energy\nEquivalence\n$\\Delta M = E/c^2$\n(Einstein 1905)", '#2E4D87'),
    (0.70, 0.52, "Perturbative\nSchwarzschild Shift\n$\\Delta r_s = 2G\\Delta M/c^2$\n(Schwarzschild 1916)", '#1A5E3A'),
    (0.38, 0.06, "$\\Delta r_s = \\dfrac{2G k_B T \\ln 2}{c^4}$", '#8B0000'),
]

for (x, y, txt, col) in boxes:
    ax.add_patch(mpatches.FancyBboxPatch((x, y), 0.24, 0.32,
        boxstyle="round,pad=0.02", fc=col, ec='white', lw=1.5,
        transform=ax.transAxes))
    ax.text(x+0.12, y+0.16, txt, ha='center', va='center', fontsize=9,
            color='white', transform=ax.transAxes, fontfamily='serif')

arrows = [
    (0.30, 0.68, 0.38, 0.68),
    (0.62, 0.68, 0.70, 0.68),
    (0.18, 0.52, 0.44, 0.38),
    (0.50, 0.52, 0.50, 0.38),
    (0.82, 0.52, 0.56, 0.38),
]
for sx, sy, ex, ey in arrows:
    ax.annotate('', xy=(ex, ey), xytext=(sx, sy),
        xycoords='axes fraction', textcoords='axes fraction',
        arrowprops=dict(arrowstyle='->', color='#555555', lw=1.8))

ax.text(0.5, 0.97, 'Derivation of the D3 Formula',
    ha='center', va='top', fontsize=13, fontweight='bold',
    color='#1F3864', transform=ax.transAxes, fontfamily='serif')
ax.text(0.5, 0.02,
    'Three independently confirmed results combine into one geometric identity.',
    ha='center', va='bottom', fontsize=8, color='#666666',
    transform=ax.transAxes, fontstyle='italic', fontfamily='serif')

plt.tight_layout()
plt.savefig(os.path.join(OUT, 'fig1_derivation_flow.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Saved fig1_derivation_flow.png")


# ── Figure 2: Delta-r_s vs Temperature ───────────────────────────────────────
print("Generating Fig 2 (Delta-r_s vs T)...")

fig, ax = plt.subplots(figsize=(7, 5))
fig.patch.set_facecolor('#FAFAF7')
ax.set_facecolor('#FAFAF7')

T_arr = np.logspace(-1, 32, 500)
dr    = d3(T_arr)

ax.loglog(T_arr, dr, color='#1F3864', lw=2.5,
    label=r'$\Delta r_s = 2Gk_BT\ln 2\,/\,c^4$')
ax.axhline(l_P, color='#8B0000', lw=1.2, ls='--',
    label=r'Planck length $\ell_P$')

markers = {
    'CMB\n(2.7 K)': 2.725,
    'Lab\n(300 K)': 300,
    'Hawking\n$M_\odot$': 6.17e-8,
    'Planck\n$T_P$': T_P
}
for label, T in markers.items():
    ax.axvline(T, color='#AAAAAA', lw=0.8, ls=':')
    ax.scatter([T], [d3(T)], s=50, zorder=5, color='#2E4D87')
    ax.text(T * 1.4, d3(T) * 2, label, fontsize=7.5,
            color='#333333', fontfamily='serif')

ax.set_xlabel('Temperature $T$ [K]', fontsize=11, fontfamily='serif')
ax.set_ylabel(r'$\Delta r_s$ [m per bit]', fontsize=11, fontfamily='serif')
ax.set_title('Geometric Cost of One-Bit Erasure vs Temperature',
    fontsize=12, fontweight='bold', color='#1F3864', fontfamily='serif')
ax.legend(fontsize=9, framealpha=0.8)
ax.grid(True, which='both', alpha=0.25)
ax.set_xlim(1e-1, 1e33)

plt.tight_layout()
plt.savefig(os.path.join(OUT, 'fig2_dr_vs_T.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Saved fig2_dr_vs_T.png")


# ── Figure 4: Planck coincidence ──────────────────────────────────────────────
print("Generating Fig 4 (Planck coincidence)...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5))
fig.patch.set_facecolor('#FAFAF7')

T2  = np.logspace(28, 33, 400)
rat = d3(T2) / l_P

ax1.set_facecolor('#FAFAF7')
ax1.semilogx(T2, rat, color='#1F3864', lw=2.5)
ax1.axvline(T_P, color='#8B0000', lw=1.5, ls='--', label=r'$T_P$')
ax1.axhline(2 * np.log(2), color='#1A5E3A', lw=1.5, ls=':',
    label=r'$2\ln 2 = 1.386$')
ax1.scatter([T_P], [2 * np.log(2)], s=80, color='#8B0000', zorder=6)
ax1.set_xlabel('Temperature [K]', fontsize=10, fontfamily='serif')
ax1.set_ylabel(r'$\Delta r_s\,/\,\ell_P$', fontsize=10, fontfamily='serif')
ax1.set_title('Approach to Planck Coincidence', fontsize=10,
    fontweight='bold', color='#1F3864', fontfamily='serif')
ax1.legend(fontsize=8)
ax1.grid(True, alpha=0.25)

ax2.axis('off')
ax2.set_facecolor('#FAFAF7')
proof = (
    "Planck Coincidence (Exact)\n\n"
    "Substitute T_P = sqrt(hbar*c^5 / G*k_B^2):\n\n"
    "delta_r(T_P) = 2G*k_B*ln2/c^4 * sqrt(hbar*c^5/G*k_B^2)\n\n"
    "             = 2*ln(2) * sqrt(hbar*G/c^3)\n\n"
    "             = 2*ln(2) * l_P    [exact]\n\n"
    "All constants cancel.\n"
    f"Computed:  delta_r(T_P)/l_P = {d3(T_P)/l_P:.6f}\n"
    f"Expected:  2*ln(2)          = {2*np.log(2):.6f}"
)
ax2.text(0.05, 0.95, proof, transform=ax2.transAxes,
    fontsize=9, va='top', fontfamily='monospace', linespacing=1.6,
    bbox=dict(boxstyle='round,pad=0.6', fc='#F0F4FB', ec='#1F3864', lw=1.5))
ax2.set_title('Algebraic Proof', fontsize=10, fontweight='bold',
    color='#1F3864', fontfamily='serif')

plt.suptitle(r'The Planck Coincidence: $\Delta r_s(T_P) = 2\ln(2)\cdot\ell_P$  [Exact]',
    fontsize=11, fontweight='bold', color='#1F3864', y=1.01)
plt.tight_layout()
plt.savefig(os.path.join(OUT, 'fig4_planck_coincidence.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  Saved fig4_planck_coincidence.png")

print("\nAll figures generated successfully.")
print(f"Output directory: {os.path.abspath(OUT)}")
