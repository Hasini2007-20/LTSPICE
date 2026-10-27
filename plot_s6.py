import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

TAG = "v1"      # change to v1, v2... after each tuning round

def load_spice(fname):
    d = pd.read_csv(fname, sep="\t", encoding="latin-1")
    d.columns = ["v", "i"]
    d["i"] = d["i"].abs()
    return d

def load_tcad(fname):
    d = pd.read_csv(fname)
    d.columns = ["v", "i"]
    return d

tg, td = load_tcad("tcad_idvg.csv"), load_tcad("tcad_idvd.csv")
sg, sd = load_spice(f"s6_idvg_{TAG}.txt"), load_spice(f"s6_idvd_{TAG}.txt")

fig, ax = plt.subplots(1, 2, figsize=(11, 4.5))

ax[0].plot(tg.v, tg.i * 1e6, "o", ms=3, mfc="none", label="TCAD")
ax[0].plot(sg.v, sg.i * 1e6, "-", label=f"SPICE ({TAG})")
ax[0].set(xlabel="VG (V)", ylabel="ID (µA)", title="ID-VG, VDS = 0.4 V")

ax[1].plot(td.v, td.i * 1e6, "o", ms=3, mfc="none", label="TCAD")
ax[1].plot(sd.v, sd.i * 1e6, "-", label=f"SPICE ({TAG})")
ax[1].set(xlabel="VD (V)", ylabel="ID (µA)", title="ID-VD, VGS = 0.9 V")

for a in ax:
    a.grid(True, alpha=0.3)
    a.legend()
plt.tight_layout()
plt.savefig(f"S6_overlay_{TAG}.png", dpi=300)

# ---- numbers to compare ----
def at(d, x):
    return np.interp(x, d.v, d.i) * 1e6

print(f"{'point':28s} {'TCAD(uA)':>10s} {'SPICE(uA)':>10s} {'ratio':>7s}")
for name, t, s, x in [
    ("ID @ VG=0 (VDS=0.4)",   tg, sg, 0.0),
    ("ID @ VG=0.5",           tg, sg, 0.5),
    ("ID @ VG=0.9",           tg, sg, 0.9),
    ("ID @ VG=1.5",           tg, sg, 1.5),
    ("ID @ VG=3.0",           tg, sg, 3.0),
    ("ID @ VD=0.1 (VGS=0.9)", td, sd, 0.1),
    ("ID @ VD=0.4",           td, sd, 0.4),
    ("ID @ VD=1.0",           td, sd, 1.0),
    ("ID @ VD=1.5",           td, sd, 1.5),
]:
    a, b = at(t, x), at(s, x)
    print(f"{name:28s} {a:10.2f} {b:10.2f} {b/a:7.2f}")

# overall error on each curve (RMS of relative difference, above 5% of max)
for name, t, s in [("ID-VG", tg, sg), ("ID-VD", td, sd)]:
    m = t.i > 0.05 * t.i.max()
    err = np.sqrt(np.mean(((np.interp(t.v[m], s.v, s.i) - t.i[m]) / t.i[m]) ** 2)) * 100
    print(f"RMS error {name}: {err:.1f} %")

plt.show()