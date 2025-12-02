
class Player:
    """Represents the player with the given stats. """
    
    def __init__(self, health=25, hunger=40, energy=70):
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

## Algorithm 3

## Algorithm 4