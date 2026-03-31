import pandas as pd

# ── Load the data ──────────────────────────────
df = pd.read_csv('data.csv')

print("=" * 40)
print("   FACTORY MACHINE REPORT")
print("=" * 40)

# ── Overview ───────────────────────────────────
total = len(df)
running = len(df[df['status'] == 'running'])
warning = len(df[df['status'] == 'warning'])
fault   = len(df[df['status'] == 'fault'])

print(f"\n📊 MACHINE STATUS OVERVIEW")
print(f"   Total Machines  : {total}")
print(f"   Running         : {running}")
print(f"   Warning         : {warning}")
print(f"   Fault           : {fault}")

# ── Temperature Analysis ───────────────────────
avg_temp = df['temperature'].mean()
max_temp = df['temperature'].max()
hot_machine = df[df['temperature'] == max_temp]['machine_id'].values[0]

print(f"\n🌡️  TEMPERATURE ANALYSIS")
print(f"   Average Temp    : {avg_temp:.1f}°C")
print(f"   Highest Temp    : {max_temp}°C → {hot_machine}")

# Flag overheating machines (above 90°C)
overheating = df[df['temperature'] > 90]['machine_id'].tolist()
if overheating:
    print(f"   ⚠️  Overheating   : {', '.join(overheating)}")

# ── Downtime Analysis ──────────────────────────
total_downtime = df['downtime_mins'].sum()
worst_machine  = df[df['downtime_mins'] == df['downtime_mins'].max()]

print(f"\n⏱️  DOWNTIME ANALYSIS")
print(f"   Total Downtime  : {total_downtime} mins")
print(f"   Worst Machine   : {worst_machine['machine_id'].values[0]}"
      f" ({worst_machine['downtime_mins'].values[0]} mins)")

# ── Fault List ─────────────────────────────────
faults = df[df['status'] == 'fault']
print(f"\n🚨 MACHINES IN FAULT")
for _, row in faults.iterrows():
    print(f"   {row['machine_id']} → {row['temperature']}°C"
          f" | {row['rpm']} RPM | {row['downtime_mins']} mins down")

# ── Healthy Machines ───────────────────────────
healthy = df[(df['status'] == 'running') & (df['downtime_mins'] == 0)]
print(f"\n✅ FULLY HEALTHY MACHINES")
for _, row in healthy.iterrows():
    print(f"   {row['machine_id']} → {row['temperature']}°C"
          f" | {row['rpm']} RPM")

print("\n" + "=" * 40)
print("   END OF REPORT")
print("=" * 40)