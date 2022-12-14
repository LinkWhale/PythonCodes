answer = input("there is a pathway, you go left or right? [left/right] ")
if answer == "left":
    print("wolves ate yo ass")
elif answer == "right":
    answer = input("There is a river, do you want to swim or jump over? [swim/jump] ")
    if answer == "swim":
        print("a shark ate yo ass")
    elif answer == "jump":
        answer = input("You jump over the river and continue forward, you see an entrance to a cave. Do you go in? [y/n] ")
        if answer == "n":
            print("you decide to not go into the cave but there were graverobbers right behind you that ate yo ass")
        elif answer == "y":
            answer = input("you see a dragon, do you want to kill it, talk to it or ignore? [kill/talk/ignore] ")
            if answer == "kill" or answer == "ignore":
                print("The dragon ate yo ass")
            elif answer == "talk":
                print("The dragon is a really nice guy, you talk to him and he gives you the treasure. YOU WIN!")
            else:
                print("Thats not an answer, you get smited and die.")
        else:
            print("Thats not an answer, you get smited and die.")
    else:
        print("Thats not an answer, you get smited and die.")
else:
    print("Thats not an answer, you get smited and die.")

