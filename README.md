# Island Survivors
**Authors:** John Watkins, Gabby Malagari, Darren Rozario, Maya Cantillo

## **Repository Contents:**
#### **`1. algorithm1.py`** 
- Contains the core function responsible for updating the player's survival statistics throughout the game. It processes daily changes to the player's health, hunger, and energy, and the applies any efefcts caused by the player's actions, available resources, and environmental changes.
- Ensures all stats remain within the acceptable ranges (0-100).
#### **`2. algorithm 2.py`**
- Handles the random event system used in the game. It stores a list of possible survival events, wahc with it's own description, set of choices, and outcomes. The main function, generate_random_event(), selects a random event, presents the available choices to the player, and applies the consequences of their decision to their current stats.
- This file is responsible for introducing unpredictability into the game and ensuring the player's stats do not go below zero.
#### **`3. algorithm 3.py`**
- Simulates how resources, such as wood, food, stone, and iron change over time.
- automatically runs through each day in the scenario, calculates changes for every resource, and prints out a detailed log of increases or decreases. By the end, it returns an updated dictionary showing the total amount of each resource collected. Overall, this file provides the logic that models environmental randomness.
#### **`4. algorithm 4.py`**
- Determines whether the player survives each day of the game. The function evaluates the player's current health and compares the current day to the total number of required survival days.
- Prints messages indicating whether the player lived through the day, completed the full survival run, or died. It then returns a Boolean value that signals whether the game should continue. This file essentially controls the end-of-day outcome logic, ensuring the game can identify win and loss conditions.
#### **`5. final_project.py `**
- This brings all of our components and all of our algorithms together and runs the full game. Also, it has each member's second function/method.
- Begins with a Player Class that store all of the player's stats (health, hunger, energy, etc.). I acts as the character system for the game.
- Contains update_survival_stats() that updates the player's stats every day.
- Contains check_stat_warning() which checks if any of your stats are getting dangerously low and gives warning messages to the player.
- Contains generate_random_event() which creates the daily event and give sthe player 4 options to choose from. Also, it updates the play's health status.
- Contains daily_resource_updates() where each day resouces can go up or down depending on luck or what you chose.
- Contains survival_check() which tells the player if the survived the day.
- Contains metric functions like total runs played, longest survival, and average days survived.
- Contains parse_game_args() which reads like a command line argument and allows users to say how may days they want to play for and on what difficulty level.
#### **`6.team_members.py`**
- This file is really simple. It's just a small module that prints out each team member's name and a short message. It stores the members in a list of dictionaries, and the loops the team member's name and message they wrote.
- We  created this file at the beginning to ensure we could all work GitHub and had experience with commit.

## How to Run the Program (Windows)
- Open up either VS Code or your PowerShell prompt
- Change into the directory that contains the game file using (cd path/to/folder)
- Run the game with:
    - python final_project.py
- Enter the amount of days and the difficulty you want to play at
- Play by following the prompts and enjoy!

## Annotated Bibliography
We made up the game and all of the functions on our own, so we did not use any outside sources.

## Attribution Table:

| Method/Function | Primary Author | Techniques Demonstrated|
|------------------|--------------------|--------------------|
| algroithm2.py    | Gabriella Malagari | Sequence Unpacking |
| algorithm3.py    | John Watkins       | Key Functions: max()| 
| algorithm1.py    | Darren Rozario     | Dictionary mutation |
| algorithm4.py    | Maya Cantillo      | F-strings containing expressions |
| parse_game_args()| Gabriella Malagari |ArgumentParser class from the argparse module|
| initializing, updating, and printing metrics | Maya Cantillo | Optional parameters and/or keyword arguments |
|run_island_survivor|John Watkins       |conditional expression|
| check_stat_warning() | Darren Rozario | List comprehension with filtering |
