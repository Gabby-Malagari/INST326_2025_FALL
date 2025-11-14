import random

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