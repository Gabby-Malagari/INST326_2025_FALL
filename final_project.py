import random
import argparse

class Player:
    """Represents the player with the given stats. """
    
    def __init__(self, health=70, hunger=40, energy=70, thirst = 50):
        """Initializes the player object with included stats.
        
        Args:
            health (int, optional): health value. Default 70.
            hunger (int, optional): hunger value. Default 40.
            energy (int, optional): energy value. Default 70.
            
        Side effects:
            Creates a stats dictionary to store player statistics.
        """
        self.stats = {"health": health, "hunger": hunger, "energy": energy, "thirst":thirst}
        
    ## Algorithm 1
    def update_survival_stats(self, resources, actions, environment,difficulty_mod):
        """Updates the player's survival stats based on daily cycles,
        player actions, available resources and environmental conditions.
        
        Args:
            resources (dict): A dictionary contianing any available resources.
                - "food" (int): amount of food available
                - "water" (int): amount of water available
                - "medicine" (int): amount of healing items available
            actions (list of str): actions the player can choose to alter stats.
                - "eat": consume 1 food
                - "drink": consume 1 water
                - "rest": increases energy
                - "forage": increases hunger, decreases energy
                - "heal": uses 1 medicine object
            environment (dict): conditions that effect the player.
                "weather" (str): type of weather (clear, storm, heatwave)
                "temperature" (int): degrees in F
                
        Returns:
            dict: The updated stats dictionary that has modified values which all 
            return as 0-100.
            
        Side effects:
            The 'resources' dictionary is modified if any resources within it is
            consumed from player actions.
        """

        stats = self.stats

        # hunger increases everyday while energy decreases
        stats["hunger"] += difficulty_mod["hunger_rate"]
        stats["energy"] -= difficulty_mod["energy_drop"]
        
        # If hunger becomes too high, health declines
        if stats["hunger"] > 80:
            stats["health"] -= difficulty_mod["health_penalty"]
            
        # The effects of the environment on the player
        if environment["weather"] == "storm":
            stats["energy"] -= 10
            stats["health"] -= 5
        elif environment["weather"] == "heatwave":
            stats["hunger"] += 5
            stats["energy"] -= 5
            stats["health"] -= 5
        
        # The different actions the player performs that alter stats
        for action in actions:
            if action == "eat" and resources.get("food", 0) > 0:
                resources["food"] -= 1
                stats["hunger"] -= 20
            elif action == "drink" and resources.get("water", 0) > 0:
                resources["water"] -= 1
                stats["energy"] += 10
                stats["thirst"] +=15
            elif action == "rest":
                stats["energy"] += 20
            elif action == "forage":
                stats["hunger"] += 5
                stats["energy"] -= 10
            elif action == "heal" and resources.get("medicine", 0) > 0:
                resources["medicine"] -= 1
                stats["health"] += 25
            
        # The stats stay within range
        for stat in stats:
            stats[stat] = max(0, min(stats[stat], 100))
            
        return stats
    
    ## Darren's 2nd Function
    def check_stat_warning(self):
        """Analyzes the player's stats and returns a warning if any values are 
            low.
        
        Returns:
            list of str: Warning messages if health, hunger, or energy is low.
        """
        limits = {
            "health": 25,
            "hunger": 75, 
            "energy": 25,
            "thirst": 75
        }
        
        # Uses current statistics to detect if the stats are at a dangerous level.
        warning = [
            f"Warning: {stat} is at {value}!"
            for stat, value in self.stats.items()
            if (
                (stat == "hunger" and value > limits["hunger"]) or
                (stat != "hunger" and value < limits[stat])
            )
        ]
        
        return warning

## Algorithm 2

def generate_random_event(current_day, player_stats):
    """
    Generates a random survival event for the player, presents choices, 
    and updates stats based on what the player decides.
    
    Args:
        current_day (int): The current day in the game.
        
        player_stats (dict): A dictionary containing the player's current stats.
                            Keys are stat names and values are integers.
                            
    Returns:
        dict: The updated player_stats dictionary after applying the effects of 
        the player's chosen option.
    """

    # List of possible survival events
    event_list = [
         {"description": "You find some berries in the forest.",
         "choices": [
             {"text": "Eat them immediately", "effects": {"hunger": -15, "health": -5}},
             {"text": "Save them for later", "effects": {"hunger": 0}},
             {"text": "Share with an animal", "effects": {"hunger": -10, "energy": +5}},
             {"text": "Ignore them", "effects": {"hunger": +5}} 
         ]},
        
        {"description": "A storm hits unexpectedly.",
         "choices": [
             {"text": "Take shelter under a tree", "effects": {"energy": -5, "health": -20}},
             {"text": "Push through the storm", "effects": {"health": -40, "energy": -40}},
             {"text": "Find a cave to hide in", "effects": {"energy": -10, "health": 0}},
             {"text": "Set up a quick tent", "effects": {"energy": -5, "hunger": +0}}
         ]},

        {"description": "A wild animal blocks your path.",
         "choices": [
             {"text": "Try to scare it away", "effects": {"health": -10, "energy": -5}},
             {"text": "Take a detour around it", "effects": {"energy": -15}},
             {"text": "Stay calm and wait", "effects": {"energy": -5}},
             {"text": "Throw some food to distract it", "effects": {"hunger": -5, "health": -2}}
         ]},

        {"description": "You discover an abandoned campsite.",
         "choices": [
             {"text": "Search for useful items", "effects": {"hunger": +0, "energy": +5}},
             {"text": "Rest for a while", "effects": {"energy": +15, "hunger": +5}},
             {"text": "Set up camp there for the night", "effects": {"energy": +10, "health": +5}},
             {"text": "Ignore it and move on", "effects": {"energy": -5, "hunger": +0}}
         ]},
        
        {"description": "You come across a river with murky water.",
     "choices": [
         {"text": "Drink the water", "effects": {"thirst": -20, "health": -5}},
         {"text": "Use a cloth to filter it", "effects": {"thirst": -15, "energy": -5}},
         {"text": "Look for a safer water source", "effects": {"energy": -10}},
         {"text": "Ignore it and move on", "effects": {"thirst": +5}}
     ]},

    {"description": "You hear strange noises at night.",
     "choices": [
         {"text": "Investigate the noise", "effects": {"health": -5, "energy": -5}},
         {"text": "Stay in your shelter", "effects": {"energy": -2}},
         {"text": "Light a fire to scare animals", "effects": {"energy": -10, "health": +0}},
         {"text": "Move to a different location", "effects": {"energy": -15, "hunger": +5}}
     ]}
]
    # Choose a random event
    event = random.choice(event_list)
    
    print(f"\nDay {current_day}")
    print("Event:", event["description"])
    
    # Show player choices 
    print("\nChoices:")
    for i, choice in enumerate(event["choices"], start=1):
        print(f"{i}. {choice['text']}")
        
    # Get player choice 
    choice_num = int(input("\nEnter the number of your choice: "))
    
    while choice_num < 1 or choice_num > len(event["choices"]):
        choice_num = int(input("Invalid choice. Please enter a valid number: "))
    
    chosen = event["choices"][choice_num - 1]
    print(f"\nYou chose: {chosen['text']}")
    
    # Apply choice effects to player stats
    for stat, change in chosen["effects"].items():
        player_stats[stat] = player_stats.get(stat, 0) + change
        if player_stats[stat] < 0:
            player_stats[stat] = 0
        
    print("\nUpdated Stats:", player_stats)
    print("-" * 30)
    
    return player_stats

## Algorithm 3
def daily_resource_updates(resources, current_day, characteristics):
    """This function updates resources an island survivor has over a multiple
    day survival scenerio. These resources can increase or decrease over these 
    days. This function also uses charactereistics defined in the code, 
    efficiency, luck, and stregnth. The program runs by itself and doesnt need a
    user input at all as of now.

    Args:
        resources (dict): a dictionary that holds 4 resource key value pairs.
                        Those resources being wood, food, iron, and stone. 
                        each resource has a base value (what you start with), a
                        growth value which is used in the caluation of the
                        amount changed, and amount which is how much the
                        surivor has gathered throughout the scenerio
        day (int): The total number of days in this scenerio
        characteristics (dict): a dictionary that holds the characteristics of
                                the survivor. Those characteristics being
                                effeciency, luck, and strength. Strength affects
                                how much stone and iron you get. Effeciency
                                effects how much wood and food you get. Luck is
                                a multiplier and affects all resources
    Returns:
        resources (dict): An updated dictionary with the final total of 
                            resources at the end of the scenerio
    """
    daily_gains={}
    # getting characteristics from variables defined
    # outside of the function (These are static as of now)
    # if these three are missing then it defaults to the value present here
    efficiency = characteristics.get("efficiency",1)
    luck = characteristics.get("luck",0)
    
    # Creating modifiers tbat will come into play with how resources are
    # generated or reduced
    efficiency_modifier = 1+(efficiency*.05)
    luck_modifier = 1+(luck*.04)
    
    # Creating random fluctuation and factor choices for day to day changes
    fluctuations = [-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5]
    factors = [0.8 * luck_modifier, 0.85 * luck_modifier, 
                      0.9 * luck_modifier, 0.95 * luck_modifier,
                      1.0 * luck_modifier, 1.05 * luck_modifier, 
                      1.1 * luck_modifier, 1.15 * luck_modifier,
                      1.2 * luck_modifier]
    
    # Creating random resource variation for a week long survival scenerio
    print(f"\n---- Day {current_day} resources ----")
    for resource, values in resources.items():
        base = values['base value']
        growth = values['growth value']
        
        # Creating random fluctuation from previously defined list
        random_fluctuation = random.choice(fluctuations)
        # Creating random factors from list above
        random_factor = random.choice(factors)
        
        characteristic_bonus = efficiency_modifier
            
        # Creating change of losing resources through decay 
        # (spoiling materials)
        decay = random.choice([0,-0.05,-0.1,-0.2,-1,-1.5,0.05,0.1])
        # Calcuating how the resources will change after each day
        change = ((base+current_day*growth)*characteristic_bonus*random_factor 
                    * (1+random_fluctuation+decay))
        change = int(change)
        
        old_amount = values['amount']
        values['amount'] += change
        values['amount'] = max(0, values['amount'])
        
        # Record the gain for today
        daily_gains[resource] = values['amount'] - old_amount
        trend = "+" if daily_gains[resource]>0 else("-" if daily_gains[resource]<0 else "0")
        
        # Printing out all the changes and showing the change in the old
        # amount and new amount
        print(f"{resource}: {trend} {abs(daily_gains[resource])} -> Total: {values['amount']}")
        
    return daily_gains


## Algorithm 4
def survival_check(player_health, day, total_days):
    """Checks if the player survived the current day.
    
    Args:
        player_health (int): The player's current health value. Must be an
            integer. If this value is less than or equal to 0, the player is
            considered dead.
        day (int): The current day number within the survival sequence.
            Must be a positive integer.
        total_days (int): The total number of days the player must survive
            to win the game. Must be a positive integer.

    Returns:
        bool: True if the player survives the current day or has completed all
            required days; False if the player has died.

    Side effects:
        Prints messages to the console indicating whether the player survived,
        died, or completed the full set of survival days.

    Raises:
        None."""
    
    if player_health <= 0:
        print(f"Day {day}: The player has died.")
        print(f"Survived {day - 1} days total.")
        return False
    elif day >= total_days:
        print(f"Day {day}: The player has survived all {total_days} days! You win!")
        return True
    else:
        print(f"Day {day}: The player has survived another day.")
        return True



## Maya's 2nd function
def initialize_metrics():
    """Create a metrics dictionary used for tracking game stats across runs."""
    return {
        "total_runs": 0,
        "longest_run": 0,
        "total_days_survived": 0,
        "average_days_survived": 0.0,

        "water_collected": 0,
        "food_collected": 0,

        "most_water_in_day": 0,
        "most_food_in_day": 0,
    }

def update_survival_metrics(metrics, days_survived):
    """Update overall survival stats at the end of a run."""
    metrics["total_runs"] += 1
    metrics["total_days_survived"] += days_survived

    # update longest survival
    if days_survived > metrics["longest_run"]:
        metrics["longest_run"] = days_survived

    # update average survival
    metrics["average_days_survived"] = (
        metrics["total_days_survived"] / metrics["total_runs"]
    )

def record_resources_collected(metrics, water=0, food=0):
    """Adds collected resources to totals and updates daily max records."""
    metrics["water_collected"] += water
    metrics["food_collected"] += food
    
    if water > metrics["most_water_in_day"]:
        metrics["most_water_in_day"] = water
    if food > metrics["most_food_in_day"]:
        metrics["most_food_in_day"] = food

def display_metrics(metrics):
    """Print a summary of recorded game statistics."""
    print("\n=== GAME STATS ===")
    print(f"Total Runs Played: {metrics['total_runs']}")
    print(f"Longest Survival: {metrics['longest_run']} days")
    print(f"Average Survival: {metrics['average_days_survived']:.2f} days")

    print("\n--- Resource Stats ---")
    print(f"Water Collected (Total): {metrics['water_collected']}")
    print(f"Food Collected (Total): {metrics['food_collected']}")

    print("\n--- Daily Maximums ---")
    print(f"Most Water in a Day: {metrics['most_water_in_day']}")
    print(f"Most Food in a Day: {metrics['most_food_in_day']}")

# Curtis's second function
def run_island_survivor(total_days,difficulty):
    player = Player()
    player_stats=player.stats
            
    resources = {
        "food":{'base value':10, 'growth value':1.5, 'amount':0},
        "water":{'base value':10, 'growth value':4, 'amount':0}
    }

    number_list=[-3,-2,-1,0,1,2,3,]
    
    characteristics = {
        "efficiency":random.choice(number_list),
        "luck": random.choice(number_list),
        "strength": random.choice(number_list)
    }
    
    player_consumables = {
        "food":3,
        "water":2.5,
        "medicine":3.5
    }
    difficulty_settings = {
        "easy": {"hunger_rate": 4,"energy_drop": 2,"health_penalty": 5},
        "normal": {"hunger_rate": 8,"energy_drop": 4,"health_penalty": 10},
        "hard": {"hunger_rate": 15,"energy_drop": 10,"health_penalty": 30}
    }
    difficulty_mod = difficulty_settings[difficulty]
    metrics=initialize_metrics()
    for day in range(1, total_days+1):
        print(f"----DAY {day}----")
        daily_gains = daily_resource_updates(resources,day,characteristics)
        record_resources_collected(metrics,water=daily_gains.get("water",0),food=daily_gains.get("food",0))
        generate_random_event(day,player_stats)
        
        
        environment={
            "weather": random.choice(["storm","heatwave"]),
            "temperature": random.randint(50,100)
        }
        print("\nChoose actions (seperate via comma):")
        print("Options: eat, drink, rest, forage, heal")
        actions = input("Actions: ")
        actions = [a.strip() for a in actions.split(",")]
        player.update_survival_stats(player_consumables,actions,environment,difficulty_mod)
        
        warnings = player.check_stat_warning()
        for w in warnings:
            print(w)
        
        status_check = survival_check(player_stats["health"],day,total_days)
        status_message = (f"You did not survive the deserted island" if not 
                          status_check else f"Congratulations, survived for {day} days on {difficulty} difficulty")
        print(status_message)
        update_survival_metrics(metrics,days_survived=day)
        display_metrics(metrics)   
## Gabby's second function

def parse_game_args():
    """
        Parse command-line arguments for the Island Survivor game.

    Returns:
        argparse.Namespace: An object containing the parsed values for:
            - days (int or None): The number of in-game days, if provided.
            - difficulty (str or None): The selected difficulty level
              ("easy", "normal", or "hard"), if provided.
    """
    parser = argparse.ArgumentParser(description="Island Survivor Game Settings")
    parser.add_argument("--days", type=int, default=None)
    parser.add_argument("--difficulty", type=str, default=None,
                        choices=["easy", "normal", "hard"])
    return parser.parse_args()

args = parse_game_args()

if args.days is None:
    total_days = int(input("Enter the number of days you want to play for: "))
else:
    total_days = args.days

if args.difficulty is None:
    difficulty = input("Choose difficulty (easy, normal, hard): ").lower()
    while difficulty not in ["easy", "normal", "hard"]:
        difficulty = input("Invalid choice. Choose difficulty (easy, normal, hard): ").lower()
else:
    difficulty = args.difficulty

print(f"Game will run for {total_days} days at {difficulty} difficulty.")

if __name__ == "__main__":
    args = parse_game_args()
    run_island_survivor(total_days, difficulty)
