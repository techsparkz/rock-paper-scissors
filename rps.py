import random
a = random.randint(1,3)
print("please play this game in full screen mode")
print("""
__________               __            __________                                        _________      .__                                  
\______   \ ____   ____ |  | __        \______   \_____  ______   ___________           /   _____/ ____ |__| ______ _________________  ______
 |       _//  _ \_/ ___\|  |/ /  ______ |     ___/\__  \ \____ \_/ __ \_  __ \  ______  \_____  \_/ ___\|  |/  ___//  ___/  _ \_  __ \/  ___/
 |    |   (  <_> )  \___|     /_____/ |    |     / __ \|  |_> >  ___/|  | \/ /_____/  /        \  \___|  |\___ \ \___ (  <_> )  | \/\___ \ 
 |____|_  /\____/ \___  >__|_ \         |____|    (____  /   __/ \___  >__|            /_______  /\___  >__/____  >____  >____/|__|  /____  >
        \/            \/     \/                        \/|__|        \/                        \/     \/        \/     \/                 \/ 
""")
# Rock Paper Scissors ASCII Art

# Rock
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
print("type:-/n"
"r for rock/n"
"p for paper/n"
"s for scissors/n")
i = input("Enter\n")
print("you:"+i)
if a == 1:
    print("computer:"+"r")
if a == 2:
    print("computer:"+"p")
if a == 3:
    print("computer:"+"s")

if a == 1 and i == "p":
    print("YOU WON")
if a == 1 and i == "s":
    print("COMPUTER WON")
if a == 1 and i == "r":
    print("TIE")
if a == 2 and i == "p":
    print("TIE")
if a == 2 and i == "r":
    print("COMPUTER WON")
if a == 2 and i == "s":
    print("YOU WON")
if a == 3 and i == "p":
    print("COMPUTER WON")
if a == 3 and i == "r":
    print("YOU WON")
if a == 3 and i == "s":
    print("TIE")
