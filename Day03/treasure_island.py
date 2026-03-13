print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
user_choice = input('You\'re at a crossroad, where do you want to go? Type "Left" or "right". \n ').lower()
if user_choice == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    swim_or_wait = input("Type wait to wait for a boat. Type swim to swim across\n").lower()
    if swim_or_wait == "wait":
        print("You arrived at the island unharmed. There is a house with 3 doors.")
        Door = input("One red, one yellow, and one blue. WHich color do you choose?\n").lower()
        if Door == "yellow":
            print("Congratulations!! You have found the sacred Treasure!!")
        elif Door == "red":
            print("You went into the red door and got eaten alive by tigers :( Game Over.")
        else:
            print("You chose the blue door and once you stepped in, "
                  "you fell into the never ending abyss of death. Game Over")
    else:
        print("You decided to swim and met a not so friendly Moby Dick :( Game Over.")
else:
    print("You went to the right and got struck by lightning :( Game Over.")
