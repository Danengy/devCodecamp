# print("Hello World")
# (5 points): As a developer, I want to make at least three commits with descriptive messages.

# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists.

# (5 points): As a user, I want a destination to be randomly selected for my day trip.

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.

# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

# (10 points): As a user, I want to display my completed trip in the console.

# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!




destination_list = ["Miami", "Chicago", "Seattle", "Los Angeles"] 


restaurant_list_miami = ["Stubborn Seed", "La Mar", "Ariete", "Makoto"]
restaurant_list_chicago = ["Aba", "Claudia", "Proxi", "Elske"]
restaurant_list_seattle = ["Copine", "Mean Sandwich", "Samara", "Sawyer"]
restaurant_list_LA = ["Hatchet Hall", "Rosalind's", "Horses", "Republique"]

transportation_list = ["car", "plane", "Train"] 

entertainment_list_miami = ["Cruise", "Everglades", "Helicopter ride", "Island Adventure"]
entertainment_list_chicago = ["Architecture rooms", "Midway Plaisance", "Lincoln park zoo", "Museums"]
entertainment_list_seattle = ["Seattle Great wheel", "Kunota Garden", "Chihuly Garden and Glass", "the Space Needle"]
entertainment_list_LA = ["Getty Center", "Broad", "Universal Studio", "Manhattan Beach Pier"]


# def generator_results():
#     return(f"Here are your results: You will be traveling to {} by {}, There you will be {} and then finishing off the night by dining at the {} restaurant.")

print("Welcome to the Day Trip Generator.")


while True: #Destination
    user_choice = input(f"""Here are four randomly picked destinations: {destination_list[0]}, {destination_list[1]}, {destination_list[2]}, {destination_list[3]}. 
# Please select and enter the one you'll go with: """)

    if user_choice == destination_list[0]:
        yes_or_no = input(f"Is {destination_list[0]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            destination_picked = destination_list[0] 
            break 
        elif yes_or_no == "n":
            print("Please pick again.")
            continue


    elif user_choice == destination_list[1]:
        yes_or_no = input(f"Is {destination_list[1]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            destination_picked = destination_list[1] 
            break 


        elif yes_or_no == "n":
            print("Please pick again.")
            continue

    elif user_choice == destination_list[2]:
        yes_or_no = input(f"Is {destination_list[2]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            destination_picked = destination_list[2] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue

    elif user_choice == destination_list[3]:
        yes_or_no = input(f"Is {destination_list[3]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            destination_picked = destination_list[3] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    else:
        print("Sorry, that's not an option, please select and enter the option you want.")



while True:  # Transportation
    user_choice = input(f"""How would you get there? By: {transportation_list[0]}, {transportation_list[1]}, {transportation_list[2]}. 
# Please select and enter the one you'll like to visit: """)

    if user_choice == transportation_list[0]:
        yes_or_no = input(f"Is traveling by {transportation_list[0]} the way you want to travel? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            transportation_picked = transportation_list[0] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue

    elif user_choice == transportation_list[1]:
        yes_or_no = input(f"Is traveling by {transportation_list[1]} the way you want to travel? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            transportation_picked = transportation_list[1] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue

    elif user_choice == transportation_list[2]:
        yes_or_no = input(f"Is traveling by {transportation_list[2]} the way you want to travel? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            transportation_picked = transportation_list[2] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    else:
        print("Sorry, that's not an option, please select and enter the option you want.")



while destination_picked == destination_list[0]:   #restaraunt list for Miami
    user_choice = input(f"""Here's are four random restaurants: {restaurant_list_miami[0]}, {restaurant_list_miami[1]}, {restaurant_list_miami[2]}, {restaurant_list_miami[3]}. 
# Please select and enter the one you'll like to dine at: """)

    if user_choice == restaurant_list_miami[0]:
        yes_or_no = input(f"Is {restaurant_list_miami[0]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            restaurant_picked = restaurant_list_miami[0] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue

    elif user_choice == restaurant_list_miami[1]:
        yes_or_no = input(f"Is {restaurant_list_miami[1]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            restaurant_picked = restaurant_list_miami[1] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue

    elif user_choice == restaurant_list_miami[2]:
        yes_or_no = input(f"Is {restaurant_list_miami[2]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            restaurant_picked = restaurant_list_miami[2] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue

    elif user_choice == restaurant_list_miami[3]: 
        yes_or_no = input(f"Is {restaurant_list_miami[3]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            restaurant_picked = restaurant_list_miami[3] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    else:
        print("Sorry, that's not an option, please select and enter the option you want.")



while destination_picked == destination_list[0]:   #entertainment list for Miami
    user_choice = input(f"""Here's are four random avtivities you might like to try while in Miami: {entertainment_list_miami[0]}, {entertainment_list_miami[1]}, {entertainment_list_miami[2]}, {entertainment_list_miami[3]}. 
# Please select and enter the activity you'll like to try: """)

    if user_choice == entertainment_list_miami[0]:
        yes_or_no = input(f"Is visiting the {entertainment_list_miami[0]} the avtivity you want to try? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            entertainment_picked= entertainment_list_miami[0] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    elif user_choice == entertainment_list_miami[1]:
        yes_or_no = input(f"Is visiting the {entertainment_list_miami[1]} the avtivity you want to try? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            entertainment_picked= entertainment_list_miami[1] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    elif user_choice == entertainment_list_miami[2]:
        yes_or_no = input(f"Is visiting the {entertainment_list_miami[2]} the avtivity you want to try? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            entertainment_picked= entertainment_list_miami[2] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    elif user_choice == entertainment_list_miami[3]:
        yes_or_no = input(f"Is visiting the {entertainment_list_miami[3]} the avtivity you want to try? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            entertainment_picked= entertainment_list_miami[3] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    else:
        print("Sorry, that's not an option, please select and enter the option you want.")



while destination_picked == destination_list[1]:   #restaraunt list for Chicago
    user_choice = input(f"""Here's are four random restaurants: {restaurant_list_chicago[0]}, {restaurant_list_chicago[1]}, {restaurant_list_chicago[2]}, {restaurant_list_chicago[3]}. 
# Please select and enter the one you'll like to dine at: """)

    if user_choice == restaurant_list_chicago[0]:
        yes_or_no = input(f"Is {restaurant_list_chicago[0]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            restaurant_picked = restaurant_list_chicago[0] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue

    elif user_choice == restaurant_list_chicago[1]:
        yes_or_no = input(f"Is {restaurant_list_chicago[1]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            restaurant_picked = restaurant_list_chicago[1] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue

    elif user_choice == restaurant_list_chicago[2]:
        yes_or_no = input(f"Is {restaurant_list_chicago[2]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            restaurant_picked = restaurant_list_chicago[2] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue

    elif user_choice == restaurant_list_chicago[3]: 
        yes_or_no = input(f"Is {restaurant_list_chicago[3]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            restaurant_picked = restaurant_list_chicago[3] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    else:
        print("Sorry, that's not an option, please select and enter the option you want.")


while destination_picked == destination_list[1]:   #entertainment list for Chicago
    user_choice = input(f"""Here's are four random avtivities you might like to try while in Miami: {entertainment_list_miami[0]}, {entertainment_list_miami[1]}, {entertainment_list_miami[2]}, {entertainment_list_miami[3]}. 
# Please select and enter the activity you'll like to try: """)

    if user_choice == entertainment_list_chicago[0]:
        yes_or_no = input(f"Is visiting the {entertainment_list_chicago[0]} the avtivity you want to try? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            entertainment_picked= entertainment_list_chicago[0] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    elif user_choice == entertainment_list_chicago[1]:
        yes_or_no = input(f"Is visiting the {entertainment_list_chicago[1]} the avtivity you want to try? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            entertainment_picked= entertainment_list_chicago[1] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    elif user_choice == entertainment_list_chicago[2]:
        yes_or_no = input(f"Is visiting the {entertainment_list_chicago[2]} the avtivity you want to try? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            entertainment_picked= entertainment_list_chicago[2] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    elif user_choice == entertainment_list_chicago[3]:
        yes_or_no = input(f"Is visiting the {entertainment_list_chicago[3]} the avtivity you want to try? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            entertainment_picked= entertainment_list_chicago[3] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    else:
        print("Sorry, that's not an option, please select and enter the option you want.")



while destination_picked == destination_list[2]:   #restaraunt list for Miami
    user_choice = input(f"""Here's are four random restaurants: {restaurant_list_seattle[0]}, {restaurant_list_seattle[1]}, {restaurant_list_seattle[2]}, {restaurant_list_seattle[3]}. 
# Please select and enter the one you'll like to dine at: """)

    if user_choice == restaurant_list_seattle[0]:
        yes_or_no = input(f"Is {restaurant_list_seattle[0]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            restaurant_picked = restaurant_list_seattle[0] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue

    elif user_choice == restaurant_list_seattle[1]:
        yes_or_no = input(f"Is {restaurant_list_seattle[1]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            restaurant_picked = restaurant_list_seattle[1] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue

    elif user_choice == restaurant_list_seattle[2]:
        yes_or_no = input(f"Is {restaurant_list_seattle[2]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            restaurant_picked = restaurant_list_seattle[2] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue

    elif user_choice == restaurant_list_seattle[3]: 
        yes_or_no = input(f"Is {restaurant_list_seattle[3]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            restaurant_picked = restaurant_list_seattle[3] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    else:
        print("Sorry, that's not an option, please select and enter the option you want.")



while destination_picked == destination_list[2]:   #entertainment list for Miami
    user_choice = input(f"""Here's are four random avtivities you might like to try while in Miami: {entertainment_list_seattle[0]}, {entertainment_list_seattle[1]}, {entertainment_list_seattle[2]}, {entertainment_list_seattle[3]}. 
# Please select and enter the activity you'll like to try: """)

    if user_choice == entertainment_list_seattle[0]:
        yes_or_no = input(f"Is visiting the {entertainment_list_seattle[0]} the avtivity you want to try? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            entertainment_picked= entertainment_list_seattle[0] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    elif user_choice == entertainment_list_seattle[1]:
        yes_or_no = input(f"Is visiting the {entertainment_list_seattle[1]} the avtivity you want to try? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            entertainment_picked= entertainment_list_seattle[1] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    elif user_choice == entertainment_list_seattle[2]:
        yes_or_no = input(f"Is visiting the {entertainment_list_seattle[2]} the avtivity you want to try? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            entertainment_picked= entertainment_list_seattle[2] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    elif user_choice == entertainment_list_seattle[3]:
        yes_or_no = input(f"Is visiting the {entertainment_list_seattle[3]} the avtivity you want to try? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            entertainment_picked= entertainment_list_seattle[3] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    else:
        print("Sorry, that's not an option, please select and enter the option you want.")



while destination_picked == destination_list[3]:   #restaraunt list for Miami
    user_choice = input(f"""Here's are four random restaurants: {restaurant_list_LA[0]}, {restaurant_list_LA[1]}, {restaurant_list_LA[2]}, {restaurant_list_LA[3]}. 
# Please select and enter the one you'll like to dine at: """)

    if user_choice == restaurant_list_LA[0]:
        yes_or_no = input(f"Is {restaurant_list_LA[0]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            restaurant_picked = restaurant_list_LA[0] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue

    elif user_choice == restaurant_list_LA[1]:
        yes_or_no = input(f"Is {restaurant_list_LA[1]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            restaurant_picked = restaurant_list_LA[1] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue

    elif user_choice == restaurant_list_LA[2]:
        yes_or_no = input(f"Is {restaurant_list_LA[2]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            restaurant_picked = restaurant_list_LA[2] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue

    elif user_choice == restaurant_list_LA[3]: 
        yes_or_no = input(f"Is {restaurant_list_LA[3]} where you wanted to go? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            restaurant_picked = restaurant_list_LA[3] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    else:
        print("Sorry, that's not an option, please select and enter the option you want.")



while destination_picked == destination_list[3]:   #entertainment list for Miami
    user_choice = input(f"""Here's are four random avtivities you might like to try while in Miami: {entertainment_list_LA[0]}, {entertainment_list_LA[1]}, {entertainment_list_LA[2]}, {entertainment_list_LA[3]}. 
# Please select and enter the activity you'll like to try: """)

    if user_choice == entertainment_list_LA[0]:
        yes_or_no = input(f"Is visiting the {entertainment_list_LA[0]} the avtivity you want to try? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            entertainment_picked= entertainment_list_LA[0] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    elif user_choice == entertainment_list_LA[1]:
        yes_or_no = input(f"Is visiting the {entertainment_list_LA[1]} the avtivity you want to try? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            entertainment_picked= entertainment_list_LA[1] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    elif user_choice == entertainment_list_LA[2]:
        yes_or_no = input(f"Is visiting the {entertainment_list_LA[2]} the avtivity you want to try? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            entertainment_picked= entertainment_list_LA[2] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    elif user_choice == entertainment_list_LA[3]:
        yes_or_no = input(f"Is visiting the {entertainment_list_LA[3]} the avtivity you want to try? Enter y/n: ")
        if yes_or_no == "y":
            print("Awesome, let's get to the next part") 
            entertainment_picked= entertainment_list_LA[3] 
            break 

        elif yes_or_no == "n":
            print("Please pick again.")
            continue
    
    else:
        print("Sorry, that's not an option, please select and enter the option you want.")


print("")
print("Congrats!! You have completed generating your day trip. Now let's just confirm this is the trip you wanted.")
print("The trip we've prepared for you is: ")
print("Destination: "+ destination_picked)
print("Transportation: " + transportation_picked)
print("Restaurant: " + restaurant_picked)
print("Entertainment: " + entertainment_picked)
finalization_input = input("Would you like to finalize this trip? Enter y/n:")
if finalization_input == "y":
    print(f"Prepare for a dream come true. You will be going to {destination_picked} by {transportation_picked}. The events planned are: visiting the {entertainment_picked} and then ending the day by dining at the {restaurant_picked}")
    print("We're glad to help you today. Have a fantastic trip.")

elif finalization_input == "n":
    print("Restart the program and try again.") 