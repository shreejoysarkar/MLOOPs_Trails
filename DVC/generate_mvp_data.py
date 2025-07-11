import pandas as pd
import os

# creating a sample DataFrame 

data = {
    "season": [
        "2021-22", "2020-21", "2019-20", "2018-19", "2017-18", "2016-17", "2015-16", "2014-15", "2013-14", "2012-13"
    ],
    "player": [
        "Nikola Jokic", "Nikola Jokic", "Giannis Antetokounmpo", "Giannis Antetokounmpo",
        "James Harden", "Russell Westbrook", "Stephen Curry", "Stephen Curry",
        "Kevin Durant", "LeBron James"
    ],
    "team": [
        "Denver Nuggets", "Denver Nuggets", "Milwaukee Bucks", "Milwaukee Bucks",
        "Houston Rockets", "Oklahoma City Thunder", "Golden State Warriors", "Golden State Warriors",
        "Oklahoma City Thunder", "Miami Heat"
    ],
    "games_played": [74, 72, 63, 72, 72, 81, 79, 80, 81, 76],
    "points_per_game": [27.1, 26.4, 29.5, 27.7, 30.4, 31.6, 30.1, 23.8, 32.0, 26.8],
    "assists_per_game": [7.9, 8.3, 5.6, 5.9, 8.8, 10.4, 6.7, 7.7, 5.5, 7.3],
    "rebounds_per_game": [13.8, 10.8, 13.6, 12.5, 5.4, 10.7, 5.4, 4.3, 7.4, 8.0],
    "team_wins": [48, 47, 56, 60, 65, 47, 73, 67, 59, 66],
    "mvp": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)


# ensuring that "Data" directory exists at the root level
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

# defining the file path
file_path = os.path.join(data_dir, "mvp_data.csv")

# Saving the DataFrame to a csv file, including column names
df.to_csv(file_path, index =False)

print(f"csv file save to {file_path}")
