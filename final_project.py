import random
class Player:
    """Represents the player with the given stats. """
    
    def __init__(self, health=70, hunger=40, energy=70):
        """Initializes the player object with included stats.
        
        Args:
            health (int, optional): health value. Default 70.
            hunger (int, optional): hunger value. Default 40.
            energy (int, optional): energy value. Default 70.
            
        Side effects:
            Creates a stats dictionary to store player statistics.
        """
        self.stats = {"health": health, "hunger": hunger, "energy": energy}
        

    def update_survival_stats(self, resources, actions, environment):
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
        stats["hunger"] += 10
        stats["energy"] -= 5
        
        # If hunger becomes too high, health declines
        if stats["hunger"] > 80:
            stats["health"] -= 10
            
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
    

    def check_stat_warning(self):
        """Analyzes the player's stats and returns a warning if any values are 
            low.
        
        Returns:
            list of str: Warning messages if health, hunger, or energy is low.
        """
        limits = {
            "health": 25,
            "hunger": 75, 
            "energy": 25
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
    event_list = [{ 
                    "description": "You find berries in the forest.",
                    "choices": [{"text": "Eat them", "effects": {"hunger": -15, "health": -5}},
                {"text": "Save them for later", "effects": {"hunger": 0}}]},
        {         "description": "A storm hits unexpectedly.",
                  "choices": [
                {"text": "Take shelter", "effects": {"energy": -10}},
                {"text": "Push forward", "effects": {"health": -10, "energy": -5}} ] } ]
    
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
def daily_resource_updates(resources, day_range, characteristics):
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
    
    # getting characteristics from variables defined
    # outside of the function (These are static as of now)
    # if these three are missing then it defaults to the value present here
    efficiency = characteristics.get("efficiency",1)
    luck = characteristics.get("luck",0)
    strength = characteristics.get("strength",1)
    
    # Creating modifiers tbat will come into play with how resources are
    # generated or reduced
    efficiency_modifier = 1+(efficiency*.05)
    luck_modifier = 1+(luck*.04)
    strength_modifier = 1+(strength*.06)
    
    # Creating random fluctuation and factor choices for day to day changes
    fluctuations = [-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5]
    factors = [0.8 * luck_modifier, 0.85 * luck_modifier, 
                      0.9 * luck_modifier, 0.95 * luck_modifier,
                      1.0 * luck_modifier, 1.05 * luck_modifier, 
                      1.1 * luck_modifier, 1.15 * luck_modifier,
                      1.2 * luck_modifier]
    
    # Creating random resource variation for a week long survival scenerio
    for day in range (1, day_range+1):
        print(f"\n---- Day {day} resources ----")
        for resource, values in resources.items():
            base = values['base value']
            growth = values['growth value']
            
            # Creating random fluctuation from previously defined list
            random_fluctuation = random.choice(fluctuations)
            # Creating random factors from list above
            random_factor = random.choice(factors)
            
            # making sure the proper modifier is being
            if resource in ("stone","iron"):
                characteristic_bonus = strength_modifier
            else:
                characteristic_bonus = efficiency_modifier
                
            # Creating change of losing resources through decay 
            # (spoiling materials)
            decay = random.choice([0,-0.05,-0.1,-0.2,-1,-1.5,0.05,0.1])
            # Calcuating how the resources will change after each day
            change = ((base+day*growth)*characteristic_bonus*random_factor 
                      * (1+random_fluctuation+decay))
            new_amount = max(0,int(values['amount']+change))
            amount_changed = new_amount-values['amount']
            values['amount']=new_amount
            if amount_changed>0:
                trend = "+"
            elif amount_changed<0:
                trend = "-"
            else:
                trend = "0"
            
            # Printing out all the changes and showing the change in the old
            # amount and new amount
            print(f"{resource}: {trend} {abs(amount_changed)} -> Total: {new_amount}")
        
    return resources
        
resources = {
    "wood":{'base value':4, 'growth value':5, 'amount':0},
    "food":{'base value':10, 'growth value':1.5, 'amount':0},
    "stone":{'base value':5, 'growth value':2, 'amount':0},
    "iron":{'base value':0, 'growth value':1.4, 'amount':0} 
}

characteristics = {
    "efficiency":4.95,
    "luck": 2.5,
    "strength": 3.5
}
total_days = 7
final_resources = daily_resource_updates(resources,total_days,characteristics)

print("\n ---- Final Resource Totals ----")
for name, values in final_resources.items():
    print(f"{name}: {values['amount']} units")

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
