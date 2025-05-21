import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('progress_tracking/progress.json')
df['date'] = pd.to_datetime(df['date'])

plt.figure(figsize=(8, 4))
plt.plot(df['date'], df['total_solved'], marker='o', linestyle='-', color='skyblue')
plt.title('LeetCode Problems Solved Over Time')
plt.xlabel('Date')
plt.ylabel('Total Problems Solved')
plt.grid(True)
plt.tight_layout()
plt.savefig('progress_tracking/progress.png')