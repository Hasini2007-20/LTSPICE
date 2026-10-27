# # # import pandas as pd
# # # import matplotlib.pyplot as plt

# # # W_um = 1.0   # device width in um (change if your W is different)

# # # d1 = pd.read_csv("idvg_0.05.csv")
# # # d2 = pd.read_csv("idvg_1.1.csv")

# # # # normalise current to uA/um
# # # d1["j"] = d1["id"] / W_um * 1e6
# # # d2["j"] = d2["id"] / W_um * 1e6

# # # fig, ax = plt.subplots(1, 2, figsize=(11, 4.5))

# # # # Linear axes
# # # ax[0].plot(d1.vg, d1.j, label="VDS = 50 mV")
# # # ax[0].plot(d2.vg, d2.j, label="VDS = 1.1 V")
# # # ax[0].set_xlabel("VG (V)")
# # # ax[0].set_ylabel("ID (A/µm)")
# # # ax[0].set_title("ID-VG (linear)")

# # # # Log axes (drop zero values, which cannot be shown on a log scale)
# # # p1 = d1[d1.j > 0]
# # # p2 = d2[d2.j > 0]
# # # ax[1].semilogy(p1.vg, p1.j, label="VDS = 50 mV")
# # # ax[1].semilogy(p2.vg, p2.j, label="VDS = 1.1 V")
# # # ax[1].set_xlabel("VG (V)")
# # # ax[1].set_ylabel("ID (A/µm)")
# # # ax[1].set_title("ID-VG (log)")

# # # for a in ax:
# # #     a.grid(True, which="both", alpha=0.3)
# # #     a.legend()

# # # plt.tight_layout()
# # # plt.savefig("S2_idvg.png", dpi=300)
# # # plt.show()
# # # 
# # import pandas as pd
# # import numpy as np
# # import matplotlib.pyplot as plt

# # # ==========================================
# # # S2: LOAD THE NEW LTSPICE FILES
# # # ==========================================

# # data_50mV = pd.read_csv("idvg_0.05.csv", sep="\t")
# # data_1_1V = pd.read_csv("idvg_1.1.csv", sep="\t")

# # Vg_50mV = data_50mV["GATE"].to_numpy()
# # Id_50mV = np.abs(data_50mV["Id(M2)"].to_numpy())

# # Vg_1_1V = data_1_1V["GATE"].to_numpy()
# # Id_1_1V = np.abs(data_1_1V["Id(M2)"].to_numpy())

# # # ==========================================
# # # GRAPH 1: LINEAR SCALE
# # # ==========================================

# # plt.figure(figsize=(8, 5))

# # plt.plot(Vg_50mV, Id_50mV, label="VDS = 50 mV")
# # plt.plot(Vg_1_1V, Id_1_1V, label="VDS = 1.1 V")

# # plt.xlim(0, 1.1)
# # plt.xlabel("Gate Voltage VGS (V)")
# # plt.ylabel("Drain Current ID (A)")
# # plt.title("S2: Transfer Characteristics (Linear Scale)")
# # plt.legend()
# # plt.grid(True, alpha=0.4)
# # plt.tight_layout()
# # plt.savefig("S2_Linear.png", dpi=300)
# # plt.show()

# # # ==========================================
# # # GRAPH 2: LOGARITHMIC SCALE
# # # ==========================================

# # plt.figure(figsize=(8, 5))

# # plt.semilogy(
# #     Vg_50mV, np.maximum(Id_50mV, 1e-15),
# #     label="VDS = 50 mV"
# # )

# # plt.semilogy(
# #     Vg_1_1V, np.maximum(Id_1_1V, 1e-15),
# #     label="VDS = 1.1 V"
# # )

# # plt.xlim(0, 1.1)
# # plt.ylim(1e-12, 1e-3)
# # plt.xlabel("Gate Voltage VGS (V)")
# # plt.ylabel("Drain Current ID (A)")
# # plt.title("S2: Transfer Characteristics (Log Scale)")
# # plt.legend()
# # plt.grid(True, which="both", linestyle="--", alpha=0.4)
# # plt.tight_layout()
# # plt.savefig("S2_Log.png", dpi=300)
# # plt.show()
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# W_um = 1.0   # device width in um

# def load(fname):
#     d = pd.read_csv(fname, sep=None, engine="python", encoding="latin-1")
#     vg = d.iloc[:, 0].to_numpy(dtype=float)
#     i = np.abs(d.iloc[:, 1].to_numpy(dtype=float)) / W_um   # A/um
#     return vg, i

# vg1, id1 = load("idvg_0.05.csv")   # VDS = 50 mV
# vg2, id2 = load("idvg_1.1.csv")    # VDS = 1.1 V

# print("50 mV: ID(VG=0) =", id1[0], " ID(VG=1.1) =", id1[-1])
# print("1.1 V: ID(VG=0) =", id2[0], " ID(VG=1.1) =", id2[-1])

# # ---------------- Graph 1: linear ----------------
# plt.figure(figsize=(8, 5))
# plt.plot(vg1, id1 * 1e6, label="VDS = 50 mV")
# plt.plot(vg2, id2 * 1e6, label="VDS = 1.1 V")
# plt.xlim(0, 1.1)
# plt.xlabel("Gate Voltage VGS (V)")
# plt.ylabel("Drain Current ID (µA/µm)")
# plt.title("S2: Transfer Characteristics (Linear Scale)")
# plt.legend()
# plt.grid(True, alpha=0.4)
# plt.tight_layout()
# plt.savefig("S2_Linear.png", dpi=300)
# plt.show()

# # ---------------- Graph 2: log ----------------
# m1 = id1 > 1e-13
# m2 = id2 > 1e-13

# plt.figure(figsize=(8, 5))
# plt.semilogy(vg1[m1], id1[m1], label="VDS = 50 mV")
# plt.semilogy(vg2[m2], id2[m2], label="VDS = 1.1 V")
# plt.xlim(0, 1.1)
# plt.ylim(1e-10, 1e-2)
# plt.xlabel("Gate Voltage VGS (V)")
# plt.ylabel("Drain Current ID (A/µm)")
# plt.title("S2: Transfer Characteristics (Log Scale)")
# plt.legend()
# plt.grid(True, which="both", linestyle="--", alpha=0.4)
# plt.tight_layout()
# plt.savefig("S2_Log.png", dpi=300)
# plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

W_um = 1.0   # device width in um

def load(fname):
    d = pd.read_csv(fname, sep=None, engine="python", encoding="latin-1")
    vg = d.iloc[:, 0].to_numpy(dtype=float)
    i = np.abs(d.iloc[:, 1].to_numpy(dtype=float)) / W_um   # A/um
    return vg, i

vg1, id1 = load("idvg_0.05.csv")   # VDS = 50 mV
vg2, id2 = load("idvg_1.1.csv")    # VDS = 1.1 V

print("50 mV: ID(VG=0) =", id1[0], " ID(VG=1.1) =", id1[-1])
print("1.1 V: ID(VG=0) =", id2[0], " ID(VG=1.1) =", id2[-1])

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# ---- linear ----
ax[0].plot(vg1, id1 * 1e6, label="VDS = 50 mV")
ax[0].plot(vg2, id2 * 1e6, label="VDS = 1.1 V")
ax[0].set(xlim=(0, 1.1), xlabel="Gate Voltage VGS (V)",
          ylabel="Drain Current ID (µA/µm)",
          title="S2: Transfer Characteristics (Linear)")

# ---- log ----
m1 = id1 > 1e-13
m2 = id2 > 1e-13
ax[1].semilogy(vg1[m1], id1[m1], label="VDS = 50 mV")
ax[1].semilogy(vg2[m2], id2[m2], label="VDS = 1.1 V")
ax[1].set(xlim=(0, 1.1), ylim=(1e-10, 1e-2),
          xlabel="Gate Voltage VGS (V)",
          ylabel="Drain Current ID (A/µm)",
          title="S2: Transfer Characteristics (Log)")

for a in ax:
    a.grid(True, which="both", linestyle="--", alpha=0.4)
    a.legend()

plt.tight_layout()
plt.savefig("S2_Linear_Log.png", dpi=300)
plt.show()