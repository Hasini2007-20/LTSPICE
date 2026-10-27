import pandas as pd
import matplotlib.pyplot as plt

for f in ["id_vg_vds_at_0.05.csv", "id_vg_vds_at_1.1.csv"]:
    d = pd.read_csv(f)
    print("=====", f)
    print("rows:", len(d))
    print(d.head(5))
    print(d.tail(3))
    print("vg step:", d.vg.iloc[1] - d.vg.iloc[0])
    print("is vg increasing?", d.vg.is_monotonic_increasing)
    print("is id increasing?", d.id.is_monotonic_increasing)

d1 = pd.read_csv("id_vg_vds_at_0.05.csv")
d2 = pd.read_csv("id_vg_vds_at_1.1.csv")
plt.semilogy(d1.vg, d1.id, "o-", ms=3, label="50 mV")
plt.semilogy(d2.vg, d2.id, "o-", ms=3, label="1.1 V")
plt.xlabel("VG (V)"); plt.ylabel("ID (A)"); plt.legend(); plt.grid(True, which="both", alpha=.3)
plt.show()