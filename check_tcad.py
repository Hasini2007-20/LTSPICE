import pandas as pd
import matplotlib.pyplot as plt

vg = pd.read_csv("tcad_idvg.csv"); vg.columns = ["v", "i"]
vd = pd.read_csv("tcad_idvd.csv"); vd.columns = ["v", "i"]

for name, d in [("IDVG", vg), ("IDVD", vd)]:
    print("=====", name, "rows:", len(d))
    print("first:", d.v.iloc[0], d.i.iloc[0])
    print("last :", d.v.iloc[-1], d.i.iloc[-1])
    print("max current:", d.i.max())

fig, ax = plt.subplots(1, 3, figsize=(14, 4))
ax[0].plot(vg.v, vg.i * 1e6); ax[0].set(title="TCAD ID-VG (linear)", xlabel="VG (V)", ylabel="ID (uA)")
ax[1].semilogy(vg.v, vg.i.abs() * 1e6); ax[1].set(title="TCAD ID-VG (log)", xlabel="VG (V)", ylabel="ID (uA)")
ax[2].plot(vd.v, vd.i * 1e6); ax[2].set(title="TCAD ID-VD", xlabel="VD (V)", ylabel="ID (uA)")
for a in ax: a.grid(True, alpha=0.3)
plt.tight_layout(); plt.show()