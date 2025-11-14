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
