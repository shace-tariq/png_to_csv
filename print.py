import pandas as pd

# Step 1: Read and clean the CSV
df = pd.read_csv("output.csv", header=None, dtype=str)
df.fillna("", inplace=True)

# Step 2: Remove excessive columns (optional - keep only first N)
MAX_COLS = 12
df = df.iloc[:, :MAX_COLS]

# Step 3: Strip newlines and whitespace
df = df.applymap(lambda x: x.replace('\n', ' ').strip() if isinstance(x, str) else x)

# Step 4: Drop rows that are mostly empty
df = df[df.apply(lambda row: row.astype(bool).sum() >= 2, axis=1)]

# Step 5: Calculate dynamic column widths
col_widths = []
for col in df.columns:
    max_len = df[col].map(len).max()
    col_widths.append(max(max_len, 10) + 2)  # padding

# Step 6: Print clean aligned table
print("\n📋 Clean Table from output.csv\n")
print("═" * sum(col_widths))

for _, row in df.iterrows():
    line = ""
    for i, val in enumerate(row):
        val = val[:col_widths[i]-2]  # truncate if too long
        line += val.ljust(col_widths[i])
    print(line)

print("═" * sum(col_widths))
