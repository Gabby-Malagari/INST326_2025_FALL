import random

def daily_resource_updates(resources, day_range, characteristics):
    """_summary_

    Args:
        resources (_type_): _description_
        day (_type_): _description_
        characteristics (_type_): _description_
    Returns:
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
    
    # Creating random resource variation for a week long survival scenerio
    for day in range (1, day_range+1):
        print(f"\n---- Day {day} resources ----")
        
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
