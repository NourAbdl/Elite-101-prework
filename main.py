print("Welcome to the Drink Chatbot! Where our goal is to keep you refreshed!")
name = input("What is your name? ")
age = int(input("Hello " + name + ", how old are you? "))

print("Welcome, " + name + "! How can I help you today?")
print("Here are all the things I can do for you today:")
print("1. Suggest a drink based on your mood")
print("2. Get information about a specific drink")
print("3. Surprise me with a random drink idea")
print("4. Exit conversation")

optionChoice = input("What would you like to do today? ")

drinks = {
    "coffee": "A hot, energizing drink made from roasted coffee beans. Great for mornings!",
    "tea": "A calming beverage that can be enjoyed hot or iced — green, black, or herbal!",
    "lemonade": "A refreshing sweet-and-sour drink, perfect for a hot day.",
    "smoothie": "A thick, fruity blend often made with yogurt or milk — healthy and delicious!",
    "water": "Simple, hydrating, and essential for your body.",
    "soda": "A bubbly, sweet drink — fun but best enjoyed in moderation!",
}

import random

if optionChoice == "1":
    print("Let's find the perfect drink for your mood!")
    mood = input("How are you feeling today? (happy, tired, relaxed, adventurous, thirsty): ").lower()
    
    if mood == "tired":
        if age>13:
            suggestion = "coffee"
        else:
            suggestion = "smoothie"
    elif mood == "relaxed":
        suggestion = "tea"
    elif mood == "happy":
        suggestion = random.choice(["lemonade", "smoothie"])
    elif mood == "adventurous":
        suggestion = "soda"
    elif mood == "thirsty":
        suggestion = "water"
    else:
        suggestion = random.choice(list(drinks.keys()))

    print(f"I recommend you try some {suggestion}!")
    print("Fun fact:", drinks[suggestion])

elif optionChoice == "2":
    drink_name = input("Which drink would you like to learn about? ").lower()
    if drink_name in drinks:
        print("Here's some info about " + drink_name + ":")
        print(drinks[drink_name])
    else:
        print("Sorry, I don’t have information on that drink yet.")

elif optionChoice == "3":
    random_drink = random.choice(list(drinks.keys()))
    print(f"Surprise! How about some {random_drink}?")
    print(drinks[random_drink])

elif optionChoice == "4":
    print("Bye, " + name + "! I hope to see you soon! Stay hydrated!")

else:
    print("Hmm, I didn't understand that choice. Please try again next time!")
