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
- This brings all our components together and runs the full game.
#### **`6.team_members.py`**

## How to Run the Program (Windows)
- Open up either VS code or your powershell prompt
- Run the game
- Enter the amount of days then the difficulty you want to play at
- Enjoy!



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
