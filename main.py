
import random

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

restaurant_list = ["Stubborn Seed", "La Mar", "Ariete", "Makoto"]

transportation_list = ["Car", "Plane", "Train"] 

entertainment_list_ = ["Seattle Great wheel", "Kunota Garden", "Chihuly Garden and Glass", "the Space Needle"]


def random_destination_generator():
    user_validation = False
    while user_validation == False:
        random_chosen_destination = random.choice(destination_list)
        user_input = input(f"The destination randomly chosen is: {random_chosen_destination}. Is this a place that you would like to visit. Enter y/n: ")
        if user_input == "y":
            print("Awesome! You have chosen a great destination. Let's move on the next part.")
            return random_chosen_destination
            user_validation = True
        elif user_input == "n":
            print("Sorry you didn't like this destination, here's another one.")
destination = random_destination_generator()

def random_transportation_generator():
    user_validation = False
    while user_validation == False:
        random_chosen_transportation = random.choice(transportation_list)
        user_input = input(f"The transportation randomly chosen is: {random_chosen_transportation}. Is this the way you would like to travel? Enter y/n: ")
        if user_input == "y": 
            print("Awesome! You have chosen a great way of transportation. Let's move on the next part.")
            return random_chosen_transportation
            user_validation = True
        elif user_input == "n":
            print("Sorry you didn't like this way of transportation, here's another one.")
transportation = random_transportation_generator()

def random_restaurant_generator():
    user_validation = False
    while user_validation == False:
        random_chosen_restaurant = random.choice(restaurant_list)
        user_input = input(f"The restaurant randomly chosen is: {random_chosen_restaurant}. Is this a place that you would like to dine in? Enter y/n:")
        if user_input == "y":
            print("Awesome! You have chosen a great restaurant. Let's move on the next part.")
            return random_chosen_restaurant
            user_validation = True
        elif user_input == "n":
            print("Sorry you didn't like this restaurant, here's another one.")
restaurant = random_restaurant_generator()

def random_entertainment_generator():
    user_validation = False 
    while user_validation == False:
        random_chosen_entertainment = random.choice(entertainment_list_)
        user_input = input(f"The for of entertainment randomly chosen is: {random_chosen_entertainment}. Is this a place that you would like to visit? Enter y/n:")
        if user_input == "y":
            print("Awesome! That is a great choic of entertainment. Let's move on the next part.")
            return random_chosen_entertainment
            user_validation = True
        elif user_input == "n": 
            print("Sorry you didn't like this place, here's another one.")
entertainment = random_entertainment_generator()

def daytrip_display():
    print("Here's what your trip is going to look like:")
    print("Destination: " + destination) 
    print("Transportation: " + transportation) 
    print("Restaurant: " + restaurant)
    print("Entertainment: " + entertainment)
daytrip_display()

