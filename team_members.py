import random

""" A module that outputs each team member's name and message. """

def main():
    """ Displays the team members' names and messages in the console through a 
    list of dictionaries.
    
    Side effects:
        Prints the list in a format in the console. 
    """
    team = [
        {"Name": "Darren Rozario", "Message": "Hi, my name is Darren!"},
        {"Name": "Curtis", "Message": "Hi im Curtis"},
        {"Name: Maya Cantillo", "Message": "Hi, my name is Maya"},
        {"Name: Gabby Malagari", "Message": "Hi, my name is Gabby"}
        
    ]
    
    for members in team:
        print(f"{members['Name']}: {members['Message']}")

# Algorithm 
def generate_random_event(current_day, player_stats, event_list):
    """
    Input
    """
    player_stats = #whatever that algs name is
    
    # Step 1: Choose a random event from the list
    event = random.choice(event_list)
    print(f"\nDay" {current_day})
    print("Event", event["description"])
    
    # Step 2: Show player choices
    print("Choices:")
    for i, choice in enumerate(event["choices"], 1):
        print(i, "-", choice["text"])
        
    # Step 3: Ask player to pick a choice
    choice_num = int(input("Enter the number of your choice:"))

        # Make sure choice is valid
        while choice_num <1 or choice_num > len(event["choices"]):
        choice_num = int(input("Invalid choice. Please enter a valid number: "))
    chosen  = event["choices"][choice_num - 1]
    print(f"\nYou chose: {chosen['text']}")

    # Step 4: Apply the effects to player stats
    for stat, change in chosen["effects"].items():
        player_stats[stat] = player_stats.get(stat, 0) + change
        if player_stats[stat] < 0:
            player_stats[stat] = 0

    # Show the result
    print(f"Outcome: {chosen['outcome']}")
    print(f"New Stats: {player_stats}")
    print("-" * 30)

    return player_stats
    
if __name__ == "__main__": 
    main()
