import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

VDD = 1.1

d = pd.read_csv("s7_vtc.txt", sep="\t", encoding="latin-1")
d.columns = ["vin", "vout"]
vin, vout = d.vin.values, d.vout.values

# switching threshold VM: where Vout = Vin
k = np.argmin(np.abs(vout - vin))
vm = vin[k]

# Vout = VDD/2 crossing
v_half = np.interp(VDD / 2, vout[::-1], vin[::-1])

# gain = dVout/dVin and its peak
gain = np.gradient(vout, vin)
gmax = np.abs(gain).max()

# noise-margin points: where gain = -1
idx = np.where(np.abs(gain) >= 1)[0]
vil, vih = vin[idx[0]], vin[idx[-1]]
voh = np.interp(vil, vin, vout)
vol = np.interp(vih, vin, vout)
nmh, nml = voh - vih, vil - vol

fig, ax = plt.subplots(1, 2, figsize=(11, 4.5))

ax[0].plot(vin, vout, label="Vout")
ax[0].plot(vin, vin, "--", color="gray", label="Vout = Vin")
ax[0].plot(vm, vm, "ro", label=f"VM = {vm:.3f} V")
ax[0].set(xlabel="Vin (V)", ylabel="Vout (V)", title="CMOS inverter VTC")

ax[1].plot(vin, gain)
ax[1].set(xlabel="Vin (V)", ylabel="dVout/dVin", title="Inverter gain")

for a in ax:
    a.grid(True, alpha=0.3)
ax[0].legend()
plt.tight_layout()
plt.savefig("S7_vtc.png", dpi=300)

print(f"VOH (Vin=0)        = {vout[0]:.3f} V")
print(f"VOL (Vin=VDD)      = {vout[-1]:.4f} V")
print(f"VM (Vout = Vin)    = {vm:.3f} V")
print(f"Vin at Vout=VDD/2  = {v_half:.3f} V")
print(f"Max gain           = {gmax:.1f}")
print(f"VIL = {vil:.3f} V, VIH = {vih:.3f} V")
print(f"NMH = {nmh:.3f} V, NML = {nml:.3f} V")
plt.show()