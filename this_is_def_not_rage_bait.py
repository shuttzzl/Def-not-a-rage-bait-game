import random


print("THIS IS DEF NOT RAGE BAIT ")

print("Welcome the most easy peasy game ever.")
print("I am 100% trustworthy.")
print("(Source: urm a dude on discord act multiple dudes on discord)")
print()

score = 0

# LEVEL 1
print("LEVEL 1: THE INTELLIGENCE TEST")
print("What is 2 + 2?")
print("1. 4")
print("2. Fish")
print("3. 22")

answer = input("> ")

if answer == "2":
    print("Correct. Finally, someone intelligent.")
    score += 1
else:
    print("WRONG. The answer was obviously fish.")
    print("Did you even go to school?")

# LEVEL 2
print("\nLEVEL 2: THE RED BUTTON")
print("There is a giant red button.")
print("A sign says: DO NOT PRESS.")
print("1. Press the button")
print("2. Leave it alone")

answer = input("> ")

if answer == "1":
    print("BOOM! You destroyed the universe.")
    print("Luckily, we had a spare universe.")
    score += 1
else:
    print("Wow. You actually follow instructions?")
    print("That's embarrassing.")

# LEVEL 3
print("\nLEVEL 3: FREE MONEY")
print("A suspicious man offers you $1,000,000.")
print("1. Accept the money")
print("2. Refuse the money")

answer = input("> ")

if answer == "1":
    print("Congratulations! You are a millionaire!")
    print("Unfortunately, it's Monopoly money.")
    score += 1
else:
    print("The man gives you the money anyway.")
    print("Unfortunately, it's Monopoly money.")
    score += 1

# LEVEL 4
print("\nLEVEL 4: BOSS FIGHT")
print("A terrifying level 999 boss appears!")
print("It has 10,000 HP!")
print("1. Attack")
print("2. Run away")
print("3. Compliment its shoes")

answer = input("> ")

if answer == "3":
    print("Boss: THANK YOU! Nobody noticed!")
    print("The boss starts crying.")
    print("You win without fighting.")
    score += 1
elif answer == "1":
    print("You deal 0.5 damage.")
    print("The boss laughs and trips over a rock.")
    print("BOSS DEFEATED!")
else:
    print("You run away.")
    print("The boss runs faster.")
    print("Then it gets tired and goes home.")

# LEVEL 5
print("\nLEVEL 5: THE FINAL QUESTION")
print("You can finally win this game.")
print("Which door leads to freedom?")
print("1. Golden door")
print("2. Wooden door")
print("3. Suspiciously normal door")

answer = input("> ")

if answer == "1":
    print("The golden door was painted cardboard.")
elif answer == "2":
    print("The wooden door leads to a brick wall.")
elif answer == "3":
    print("The normal door leads to another door.")
    score += 1
else:
    print("You invented a new door.")
    print("The narrator is genuinely impressed.")
    score += 2

print("\n===================================")
print("           FINAL RESULTS")
print("===================================")

print("Your score:", score, "/ 5")

if score >= 5:
    print("\nSECRET ENDING: TOO SMART")
    print("You outsmarted the entire game.")
    print("The narrator rage quits.")
    print("YOU WIN!")

elif score >= 3:
    print("\nENDING: CERTIFIED TROLL")
    print("You survived the nonsense.")
    print("Your reward is absolutely nothing.")
    print("Congratulations, I guess.")

else:
    print("\nENDING: SKILL ISSUE")
    print("The narrator is disappointed.")
    print("Your gaming license has been revoked.")
    print("Please uninstall your keyboard.")

print("\nThanks for playing!")
print("Just kidding. Leave.")
