stage = 0
answer_correct = True
money = 10
power = 0
hp = 100
enemyHP = 0


def begin():
    global power
    answer = input("You make your way to the cave and upon the entrance you find a rusty sword, would you like to take it with you [y/n]")
    if answer == "y" and power == 10:
        print("You feel the wieght of both weapons slow down your movement.")
    elif answer== "y" and power == 5:
        print("You take the sword and dual wield it with your shortsword")
    elif answer == "y" and power <= 5:
        power += 3
        print("You take the sword, better to have something to defend yourself with right?")
    elif answer == "n" and power > 0:
        print("You decide that carrying that blade would only be an inconvenience.")
    else:
        print("You think that your skills are too good for a blade.")



answer = input("Welcome to a text based RPG, to begin your adventure type in [start]\n")
if answer == "start":
        answer = input("You've heard of the legendary treasue guarded in the deepest cave in the Kingdom of Larion, however if you want to obtain that treasure you will have to slay the great beholder that guards it. Do you wish to begin your adventure of go to the blacksmith and buy a weapon? [begin/buy]")
        if answer == "begin":
            begin()
        elif answer == "buy":
            answer = input("You go to a blacksmith. When you arrive you spot a big, bald man with a mustache that covers half of his face.\n\"If you're here for weapons I have some bad news for you, I was just visited by a group of adventurers so most of my stock is gone, however I do have those two beauties.\" He shows you a longsword for 10 coins and a short sword for 5 coins. What do you want to buy? [longsword/shortsword/leave]")
            if answer == "shortsword":
                money -= 5
                power += 5
                print("You pay 5 coins and your power increased by 5")
                begin()
            elif answer == "longsword":
                money -= 10
                power += 10
                print("You pay 10 coins and your power increased by 10")
                begin()
            else:
                begin()
        else:
            print("Because you didn't use answers in [] you wil automatically begin \n")
            begin()
else:
    print("Because you didn't use answers in [] you wil automatically begin \n")
    begin()
