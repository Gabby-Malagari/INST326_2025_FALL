""" A module that outputs each team member's name and message. """

def main():
    """ Displays the team members' names and messages in the console through a 
    list of dictionaries.
    
    Side effects:
        Prints the list in a format in the console. 
    """
    team = [
        {"Name": "Darren Rozario", "Message": "Hi, my name is Darren!"}
        {"Name": "Curtis", "Message": "Hi im Curtis"}
    ]
    
    for members in team:
        print(f"{members['Name']}: {members['Message']}")
    
if __name__ == "__main__": 
    main()