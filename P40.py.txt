import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("players.csv")

top_goals = df.sort_values('goals', ascending=False).head(5)
top_salaries = df.sort_values('weekly_salary', ascending=False).head(5)
avg_age = df['age'].mean()
above_avg = df[df['age'] > avg_age]

print("Top 5 goal scorers:\n", top_goals[['name','goals']].to_string(index=False))
print("\nTop 5 salaries:\n", top_salaries[['name','weekly_salary']].to_string(index=False))
print(f"\nAverage age: {avg_age:.2f}")
print("\nPlayers above average age:\n", above_avg[['name','age']].to_string(index=False))

# Position distribution
pos_counts = df['position'].value_counts()
pos_counts.plot(kind='bar')
plt.xlabel("Position")
plt.ylabel("Count")
plt.title("Player Distribution by Position")
plt.savefig("position_distribution.png")
print("\nSaved plot: position_distribution.png")
