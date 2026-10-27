import numpy as np
import pandas as pd

W_um = 1.0       # device width in um
L_um = 0.065     # device length in um (65 nm)
VDD = 1.1

d1 = pd.read_csv("idvg_0.05.csv")   # VDS = 50 mV
d2 = pd.read_csv("idvg_1.1.csv")    # VDS = 1.1 V

vg1, id1 = d1.vg.values, d1.id.values
vg2, id2 = d2.vg.values, d2.id.values

# ---- VTH method 1: max-gm linear extrapolation (VDS = 50 mV) ----
gm = np.gradient(id1, vg1)
k = np.argmax(gm)
vth_gm = vg1[k] - id1[k] / gm[k] - 0.05 / 2

# ---- VTH method 2: constant current ----
icrit = 100e-9 * W_um / L_um
vth_cc_lo = np.interp(icrit, id1, vg1)
vth_cc_hi = np.interp(icrit, id2, vg2)

# ---- ION and IOFF at VDS = 1.1 V ----
ion = np.interp(VDD, vg2, id2) / W_um * 1e6    # uA/um
ioff = np.interp(0.0, vg2, id2) / W_um * 1e9   # nA/um

# ---- Subthreshold swing ----
mask = (id1 > icrit * 1e-4) & (id1 < icrit * 0.5)
print("points used for SS:", mask.sum())
if mask.sum() >= 2:
    slope = np.polyfit(vg1[mask], np.log10(id1[mask]), 1)[0]
    ss = 1e3 / slope
else:
    ss = float("nan")

# ---- DIBL ----
dibl = (vth_cc_lo - vth_cc_hi) / (VDD - 0.05) * 1e3

print("-------- RESULTS --------")
print(f"VTH (gm-max, VDS=50 mV)    = {vth_gm:.3f} V")
print(f"VTH (const-curr, 50 mV)    = {vth_cc_lo:.3f} V")
print(f"VTH (const-curr, 1.1 V)    = {vth_cc_hi:.3f} V")
print(f"ION  (VG=VDS=1.1 V)        = {ion:.1f} uA/um")
print(f"IOFF (VG=0, VDS=1.1 V)     = {ioff:.4f} nA/um")
print(f"SS                         = {ss:.1f} mV/dec")
print(f"DIBL                       = {dibl:.1f} mV/V")