#!/usr/bin/python3

import time		# used to add wait time during printing
import sys		# used to exit the program
import os		# used to clear the console
from termcolor import cprint 	# print in different colors
# dialogue is in color
import random
import HadesQuotes as quote

islands = []

inventory = ["sword"]

global space # new Line
space = "\n" # very inconsistant

global look
look = 0

def inventoryAdd():
    inventory.append("food")
    inventory.append("water")
    print("Inventory:", inventory, space)

def inventoryLoss():
    inventory.remove("food")
    inventory.remove("water")
    print("Inventory:", inventory, space)

def cheat(): # bypass lack of inventory
    inventory.append("food")
    inventory.append("water")

def clear():
	os.system("clr" if os.name == "nt" else "clear")

def progress():
    print("Time to board the ship.\n")
    inventoryLoss()
    global look
    look = 0
    time.sleep(12)
    clear()

def revisit(): # only if you look, you can revisit previous island
    global look
    look = 1
    return look   

damage = random.randint(0, 2)

global puzzle
puzzle = 0
 

print("You are traveling with Odysseus. After the Trojan War, you are on the journey home to Ithaca, but the Gods have other plans. You are on a ship with dwindling supplies.\n")

def Ismaros(): # island 1
    print("You have been on the ship for weeks. Finally, you see an island. Land ahoy! There is a town at the base of the mountain. This island has a volcano. Has it erupted yet? You have landed on Ismaros, the Land of the Cicones.\n")
    print("Inventory:", inventory, space)
    action = input("What would you like to do? \n1. Look around \n2. Go forward \n3. Go right \n4. Go left \n5. Back to the ship \n\n")
    if action == "1":
        print(space+ "The Cicones seem unaware of the Trojan war. They live comfortably. No one goes thirsty or hungry. The men of the town are proud of their collection of gold and war trophies.\n")
        Ismaros()
    elif action == "2":
        print(space+ "You go into town and bump into a local. They invite you to dinner. You regall them about your stories during the Trojan war.\n")
        inventoryAdd()
        islands.append("island 1")
    elif action == "3":
        print(space+ "You have wondered off towards the volcano. As you climb up, the town gets smaller. The volcano is accompanied by hot springs. There is vegetation and intesting types of volcanic rock. You reach the top where it seems the volcano is dormant. No recreation of Pompeii today.\n")
        inventoryAdd()
        islands.append("island 1")
    elif action == "4":
        print(space+ "One of your shipmates realize the town is full of resources. They plan to raid the town. The crew plunders the town and take food and water back to the ship.\n")
        inventoryAdd()
        islands.append("island 1")
    elif action == "5":
        print(space+ "You have run out of food and water. The Gods do not favor you and you perish at sea.")
        sys.exit()
    else:
        cprint("\nThat is not a valid choice. Try again.\n", "grey", "on_red")
        Ismaros()

def LotusEaters(): # island 2
    print("Inventory:", inventory, space+ "\nYour ship comes across an island covered in plants. It is dominated by the lotus tree. There are fruits of all kinds and flowers of all colors. You have landed on the Island of the Lotus Eaters. The inhabitants seem friendly.\n")
    action = input("What would you like to do? \n1. Look around \n2. Go forward \n3. Go right \n4. Go left \n5. Back to the ship \n\n")
    if action == "1":
        print(space+ "The population seems to be at ease. Every one is calm with no plans to move. There are inhabitants scattered on the island laying next to the mysterious fruit. You realize this island may hinder you on your way home.", space)
        revisit()
        LotusEaters()
    elif action == "2":
        print(space+ "The lotus fruit grows in abundance. You want to harvest the fruit to take with you. The inhabitants are more than happy to comply and share the fruit.", space)
        if "Lotus fruit" not in inventory:
                inventory.append("Lotus fruit")
        else:
            pass
        inventoryAdd()
        islands.append("island 2")
    elif action == "3":
        print(space+ "There is an area on the island that has deserted boats. You scavenge the vessels to take resources with you.", space)
        inventoryAdd()
        islands.append("island two")
    elif action == "4":
        print(space+ "The inhabitants are persistant that you try the mysterious fruit. The sweet, addictive liquid is comforting. You want more, you need more. Nothing else matters. You have stayed on the island for years. Going home to Ithaca is a mere past.", space)
        sys.exit()
    elif action == "5":
        if look == 1:
            islands.remove("island 1")
            cheat()
        else:
            print(space+ "The time at sea has caused the crew to go stir crazy. The crew start fighting between each other for food. No one is left.")
            sys.exit()
    else:
        cprint("\nThat is not a valid choice. Try again.\n", "grey", "on_red")
        LotusEaters()

def Sicily(): # island 3
    print("Inventory:", inventory, space+ "\nYou've landed on the Island of Sicily, home of the Cyclops. They are the sons of Posiden. They dwell in remote caves. Sheep are abundant on this island.\n")
    action = input("What would you like to do? \n1. Look around \n2. Go forward \n3. Go right \n4. Go left \n5. Back to the ship \n\n")
    if action == "1":
        print(space+ "There is a boatload worth of food, water, gold, and supplies in the caves.", space)
        revisit()
        Sicily()
    elif action == "2":
        print(space+ "You walk up to the nearest Cyclop. Cyclopes do not like to be disturbed. They are not welcoming to strangers. The Cylcop will make you his dinner. He has his eye set on you, he attacks.", space)
        if damage == 1 :
                print("You were eaten alive.")
                sys.exit()
        else:
            print("You strategically stab the Cyclop in the eye with your sword. He's blinded. You hide under the sheep as they run out of the cave and escape.", space)
            inventoryAdd()
            islands.append("island three")
    elif action == "3":
        print(space+ "You wander into the open cave of a Cyclops. You take barrels of water, a dozen sheep, and beeswax. Avoiding the Cyclopes, you leave the cave undetected.", space)
        if "beeswax" not in inventory:
                inventory.append("beeswax")
        else:
            pass
        inventoryAdd()
        islands.append("island 3")
    elif action == "4":
        print(space+ "There is an alter to Posiden. You lack supplies for a proper sacrifice.\n")
        if "Lotus fruit" in inventory:
                inventory.remove("Lotus fruit")
                print("You pray to the Gods to recieve good blessings on your travels. You tribute the fruit from the Island of the Lotus Eaters to Demeter, Goddess of the harvest and agriculture. She blesses you with a gift.\n")
        else:
                print("You promise the Gods that you will make ammends as you take the food and water from the alter.\n")
        inventoryAdd()
        islands.append("island 3")
    elif action == "5":
        if look == 1:
            islands.remove("island 2")
            cheat()
        else:
            print(space+ "The crew has resorted to eating mysterious brown objects on the ship. It does not end well.")
            sys.exit()
    else:
        cprint("\nThat is not a valid choice. Try again.\n", "grey", "on_red")
        Sicily()

def Aeaea(): # island 4
    print("Inventory:", inventory, space+ "\nThis island is alive with animals. The woods have potential to supply your ship. Great beasts prowl the area as you approach. You have landed on Aeaea.", space)
    action = input("What would you like to do? \n1. Look around \n2. Go forward \n3. Go right \n4. Go left \n5. Back to the ship \n\n")
    if action == "1":
        print(space+ "There are many trees to provide adequate shade. A palace is guarded by lions and wolves. You dare not provoke them.\n")
        revisit()
        Aeaea()
    elif action == "2":
        print(space+ "You open the door to the palace with your sword in hand. To your surprise, an enchanting, young Goddess resides there. She introduces herself as the Goddess Circe. Her voice is alluring as she invites you to a feast.", space)
        user_pick = input("What do you do? \n1. Ask to stay the night \n2. Eat the feast \n\n")
        if user_pick == "1":
            print(space+ "As hostess, she grants you the privilegde to spend the night. You have a dream where Hermes visits you. He gives you advice to charm Circe. In the morning, you convince Circe to supply you for your way home. She advices you to travel to the Land of the Dead and talk to Tiresias.", space)
            inventoryAdd()
            islands.append("island 4")
        elif user_pick == "2":
            print("As you stuff your face with the hearty meal, she tempts you to drink an elixir. The Goddess laughs at you.")
            cprint("Now you swine, be off to the pigsty where you belong.", "cyan")
            print("You realize, Circe is a sorcorress, but it is too late as your hands become hooves and your nose transforms to a snout. \n\nOink Oink.")
            sys.exit()
        else:
            cprint("\nThat is not a valid choice. Try again.\n", "grey", "on_red")
            Aeaea()
    elif action == "3":
        print(space+ "There is a pigsty with countless amounts of swine. Pigs won't attack you, but these ones look almost human-like. A storm approaches. You collect the rainwater and stock your ship with pigs.\n")
        inventoryAdd()
        islands.append("island 4")
    elif action == "4":
        print(space+ "You check the trees and bushes for bird eggs. It's not much, but you collect a decent amount. Those clouds bring rain. You collect the rainwater and settle for bird eggs.\n")
        inventoryAdd()
        islands.append("island 4")
    elif action == "5":
        if look == 1:
            if "island 3" in islands:
                islands.remove("island 3")
            else:
                islands.remove("island two")
            cheat()
        else:
            print(space+ "There is a storm. One of the crew members did not anchor down the boat. Your boat capsizes and you drown.")
            sys.exit()
    else:
        cprint("\nThat is not a valid choice. Try again.\n", "grey", "on_red")
        Aeaea()

def Underworld(): # island 5
    print("Inventory:", inventory, space+ "\nThe Gods have meddled in your life. The sea has not been kind to you on your journey home. Per Circes' instructions, you pour libations and perform sacrifices. This give you passage through the River of Ocean to the Underworld. Welcome to the Underworld. Home of Hades.", space)
    action = input("What would you like to do? \n1. Look around \n2. Go forward \n3. Go right \n4. Go left \n5. Back to the ship \n\n")
    if action == "1":
        print(space+ "The Underworld has many wandering souls. If you're lucky, not all of them are insane. Hades is known for his guard dog, Cerberus. Cerberus is a 3 headed dog. He looks hungry. Luckily, you found treats nearby. You toss as many as you can to all the heads. He settles down and lays next to you. You are free to pet him.\n")
        revisit()
        Underworld()
    elif action == "2":
        print(space+ "You run into the God of the Underworld himself.\n")
        if random.choice(quote.Hades) == (quote.Hades[6]):
            cprint(quote.Hades[6], "cyan")
            cprint("\nThe minions always lose when we play chess.\n", "cyan")
        else:
            cprint(random.choice(quote.Hades), "cyan")
        print(space+ "Hades leads you through the Elysium fields.\n")
        inventoryAdd()
        islands.append("island 5")
    elif action == "3":
        print(space+ "You run into Tieresias. He is a blind prophet.")
        cprint("\nJourney past the Sirens. They will sing you sweet music. You must not listen. Plug your ears with beeswax.", "cyan")
        print(space+ "Tieresias has heard about your travels and gives you supplies for your journey.\n")
        inventoryAdd()
        islands.append("island 5")
        global puzzle
        puzzle = 1
        return puzzle
    elif action == "4":
        print(space+ "You run into Eurydice. Wasn't she part of a tragic love story?\n")
        cprint(random.choice(quote.Eurydice), "cyan")
        print(space+ "Eurydice wants you to get home to your loved ones.\n")
        inventoryAdd()
        islands.append("island 5")
    elif action == "5":
        if look == 1:
            if "island 4" in islands:
                islands.remove("island 4")
            else:
                islands.remove("island 7")
            cheat()
        else:
            print(space+ "You can hear the spirits underneath the boat. You start to recognize faces as they drift on by. You miss them so much. You jump ship to join them...")
            sys.exit()
    else:
        cprint("\nThat is not a valid choice. Try again.\n", "grey", "on_red")
        Underworld()

def Sirens(): # island 6
    print("Inventory:", inventory, space+ "\nIt has been smooth sailing the closer you get to the Island of the Sirens. What could they have in store for you?", space)
    action = input("What would you like to do? \n1. Look around \n2. Go forward \n3. Go right \n4. Go left \n5. Back to the ship \n\n")
    if action == "1":
        print(space+ "The path in front of you is a strait. Sirens are on either side of the boat. Are you prepared for the Sirens?\n")
        revisit()
        Sirens()
    elif action == "2":
        if puzzle == 1:
            if "beeswax" in inventory:
                inventory.remove("beeswax")
                print(space+ "You and the crew cover your ears in beeswax. You sail smoothly through the waters of the Sirens. You find an abandoned ship. The crew must not have been as fortunate. You ransack the boat to find food and water.", space)
                inventoryAdd()
                islands.append("island 6")
            else:
                print(space+ "Inventory:", inventory)
                print(space+ "Beeswax is not in your inventory. Come back when you have explored a few islands.\n")
                del (islands[:])
                Ismaros()
        else:
            print(space+ "You are not prepared for the Sirens. Come back when you have explored a few islands.")
            del (islands[:])
            Ismaros()
    elif action == "3":
        print(space+ "The Sirens are deceitful with their alluring voice. You listened to the Sirens. The Sirens sang a song so beautiful that it turned you into a mermaid. Welcome to the deep blue sea.")
        sys.exit()
    elif action == "4":
        print(space+ "The boat steered left. Unfortunately, you could not avoid the rock and crashed.")
        sys.exit()
    elif action == "5":
        islands.remove("island 5")
        cheat() #bypass lack of inventory
    else:
        cprint("\nThat is not a valid choice. Try again.\n", "grey", "on_red")
        Sirens()

def Ogygia(): # island 7
    print("Inventory:", inventory, space+ "\nYou see the mansion first. As your drift closer, it is an island with a beautiful palace. It is unclear who or what lives in that palace. You have landed on Ogygia.", space)
    action = input("What would you like to do? \n1. Look around \n2. Go forward \n3. Go right \n4. Go left \n5. Back to the ship \n\n")
    if action == "1":
        print(space+ "The terrain is rocky. Where are the animals?")
        revisit()
        Ogygia()
    elif action == "2":
        print(space+ "There is a cave, but the entrance seems to be underground. You lower your body into the crevasse and immediately hear the sound of rushing water. The underground river provides you with fresh water and an assortment of fish.\n")
        inventoryAdd()
        islands.append("island 7")
    elif action == "3":
        print(space+ "You find Calypso. The nymph with lovely braids. She favors you. Her home and servants are yours to enjoy.", space)
        user_pick = input("What would you like to do? \n1. Pray to the Gods \n2. Stay on the island \n\n")
        if user_pick == "1":
            print(space+ "The Gods hear your desire to return home to Ithaca. They command Calypso to provide you nurishment and supplies.", space)
            inventoryAdd()
            islands.append("island 7")
        elif user_pick == "2":
            print(space+ "On Calypso's Island, time is different. You gain immortality on the island. You are free to indulge in your vices.")
            sys.exit()
        else:
            cprint("\nThat is not a valid choice. Try again.\n", "grey", "on_red")
            Ogygia()
    elif action == "4":
        print(space+ "The rocks are loose as you climb to get a viewpoint. Your foot slipped and you cause a rockslide. You do not survive.")
        sys.exit()
    elif action == "5":
        if look == 1:
            if "island 6" in islands:
                islands.remove("island 6")
            else:
                islands.remove("island three")
            cheat()
        else:
            print(space+ "You have run out of food and water.")
            sys.exit()
    else:
        cprint("\nThat is not a valid choice. Try again.\n", "grey", "on_red")
        Ogygia()

def Ithaca(): # island 8
    print("Inventory:", inventory, space+ "\nIt has been years at sea. The Trojan War is over. The Gods allow you to return home. You arrive on the shore of Ithaca.\n")
    action = input("What would you like to do? \n1. Look around \n2. Go forward \n3. Go right \n4. Go left \n5. Back to the ship \n\n")
    if action == "1":
        print(space+ "The city is lively and your home is in order. The island is mountainous, covered in pine forests, cypresses, olive trees, and vineyards.\n")
        Ithaca()
    elif action == "2":
        print(space+ "At your home, you prepare a proper tribute to the Gods. It was a long journey, but you are safe at home.")
        print("Until the next journey...")
        sys.exit()
    elif action == "3":
        print(space+"You have missed the smell vineyards. You froalic through the fields and get drunk on wine. Eat, drink, and be merry.")
        print("Until the next journey...")
        sys.exit()
    elif action == "4":
        print(space+"The agora is a public space. You tell the masses about the Trojan war and your wild journey home. You are named a hero.")
        print("Until the next journey...")
        sys.exit()
    elif action == "5":
        user_pick = input(space+ "Would you like to play again? \n\n")
        if (user_pick == "yes" or user_pick == "y" or user_pick == "Yes"):
            Ismaros()
            del (islands[:])
        else:
            print("Until the next journey...")
            sys.exit()    
    else:
        cprint("\nThat is not a valid choice. Try again.\n", "grey", "on_red")
        Ithaca()

while True:
    if ("island 1" and "island 2" and "island three" and "island 7" and "island 5" and "island 6" in islands): # solves Underworld redundancy
        Ithaca()
    elif ("island three" and "island 7" in islands): # Ogygia to Underworld
        Underworld()
        progress()

    if ("island 5" and "island 6" not in islands) and ("island 5" in islands): # Underworld to Sirens
        Sirens()
        progress()
    elif "island 7" in islands:
        Ithaca()
        progress()
    elif "island 6" in islands:
        Ogygia()
        progress()
    elif "island 5" in islands:
        Sirens()
        progress()
    elif "island 4" in islands:
        Underworld()
        progress()
    elif "island 3" in islands:
        Aeaea()
        progress()
    elif "island three" in islands: # skip Aeanea - island 4
        Ogygia()
        progress()
    elif "island 2" in islands:
        Sicily()
        progress()
    elif "island two" in islands: # skip Sicily - island 3
        Aeaea()
        progress()
    elif "island 1" in islands:
        LotusEaters()
        progress()
    elif "island 1" not in islands: # begins the game
        Ismaros()
        progress()
