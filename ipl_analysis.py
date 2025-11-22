import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sujalsingh26",
    database="ipl_db"
)

# Fetch data
df = pd.read_sql("SELECT * FROM matches", conn)
conn.close()

# Total matches
print(f"Total matches: {df.shape[0]}\n")

# Wins per team
wins = df['Winner'].value_counts()
print("Wins per team:\n", wins, "\n")

# Top 5 Players of the Match
top_players = df['Player_of_Match'].value_counts().head(5)
print("Top 5 Players:\n", top_players, "\n")

# Average runs per team
avg_runs_team1 = df.groupby('Team1')['Team1_Score'].mean()
avg_runs_team2 = df.groupby('Team2')['Team2_Score'].mean()
avg_runs = avg_runs_team1.add(avg_runs_team2, fill_value=0)
print("Average runs per team:\n", avg_runs, "\n")

# Graph
wins.head(5).plot(kind='bar', color='skyblue')
plt.title("Top 5 Teams by Wins")
plt.xlabel("Team")
plt.ylabel("Wins")
plt.show()