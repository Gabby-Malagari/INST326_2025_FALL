import random

event_list = [
    {
        "description": "You find berries in the forest.",
        "choices": [
            {"text": "Eat them", "effects": {"hunger": -15, "health": -5}},
            {"text": "Save them for later", "effects": {"hunger": +0}}
        ]
    },
    {
        "description": "A storm hits unexpectedly.",
        "choices": [
            {"text": "Take shelter", "effects": {"energy": -10}},
            {"text": "Push forward", "effects": {"health": -10, "energy": -5}}
        ]
    }
]

def generate_random_event(current_day, player_stats, event_list):
    """
    Generates a random survival event for the player, presents choices, 
    and updates stats based on what the player decides.
    
    Args:
        current_day (int): The current day in the game.
        
        player_stats (dict): A dictionary containing the player's current stats.
                            Keys are stat names and values are integers.
                            
        event_list(list): A list of event dictionaries. Each event contains:
            - "description": a string describing the event
            - "choices": a list of choice dictionaries, each containing:
                - "text": the choice description
                - "effects": a dict mapping stats to changes
                
    Returns:
        dict: The updated player_stats dictionary after applying the effects of 
        the player's chosen option.
     
    """
    
    # Choose a random event from the list
    event = random.choice(event_list)
    
    print(f"\nDay {current_day}")
    print("Event:", event["description"])
    
    # Show player choices 
    print("\nChoices:")
    index = 1
    for choice in event["choices"]:
        print(f"{index}. {choice['text']}")
        index += 1
        
    # Get player choice 
    choice_num = int(input("\nEnter the number of your choice: "))
    
    while choice_num < 1 or choice_num > len(event["choices"]):
        choice_num = int(input("Invalid choice. Please enter a valid number: "))
    
    #     
    chosen = event["choices"][choice_num - 1]
    print(f"\nYou chose: {chosen['text']}")
    
    # Apply choices to player stats
    for stat, change in chosen["effects"].items():
        player_stats[stat] = player_stats.get(stat, 0) + change
        
        # Avoid stats going negative
        if player_stats[stat] < 0:
            player_stats[stat] = 0
        
    # Show updated stats
    print("\nUpdated Stats:", player_stats)
    print("-" * 30)
    
    return player_stats