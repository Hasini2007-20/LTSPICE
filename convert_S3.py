import pandas as pd

def parse_val(s):
    """Convert LTspice values like '300m', '1.5', '900m' to floats."""
    s = s.strip()
    mult = {"m": 1e-3, "u": 1e-6, "µ": 1e-6, "n": 1e-9, "p": 1e-12, "k": 1e3}
    if s[-1] in mult:
        return float(s[:-1]) * mult[s[-1]]
    return float(s)

rows, vgs = [], None
with open("id_vd_at_diff_vg.txt", encoding="latin-1") as f:
    f.readline()                                  # skip header line
    for line in f:
        line = line.strip()
        if not line:
            continue
        if line.startswith("Step Information"):
            # e.g. 'Step Information: V1=300m  (Run: 1/4)'
            vgs = parse_val(line.split("V1=")[1].split()[0])
        else:
            parts = line.replace(",", " ").split()
            vd, i = float(parts[0]), float(parts[1])
            rows.append((vgs, vd, abs(i)))

df = pd.DataFrame(rows, columns=["vgs", "vd", "id"])
df.to_csv("id_vd_at_diff_vg.csv", index=False)

print(df.groupby("vgs").size())                   # rows per VGS
print(df.head())
print("vgs values:", sorted(df.vgs.unique()))
print("vd range:", df.vd.min(), "to", df.vd.max())