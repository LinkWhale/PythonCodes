import random

ai_choice = 0
your_choice = 0
cont = True
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]
imgchoice = 0

while cont == True:
    #Establish the choices
    print("Welcome to rock paper scissors\nPlease input either \"rock\", \"paper\" or \"scissors\" to make your choice.")
    your_choice = input()
    ai_choice = random.randrange(0,3)
    ai_img = ai_choice
    if ai_choice == 0:
        ai_choice = "rock"
    elif ai_choice == 1:
        ai_choice = "paper"
    elif ai_choice == 2:
        ai_choice = "scissors"

    if your_choice == "rock":
        imgchoice = 0
    elif your_choice == "paper":
        imgchoice = 1
    elif your_choice == "scissors":
        imgchoice = 2

    print("You chose {}\n{}\nYour opponent chose {}\n{}".format(your_choice, images[imgchoice], ai_choice, images[ai_img]))

    #check the outcome
    if your_choice == "rock" and ai_choice == "scissors" or your_choice == "scissors" and ai_choice == "paper" or your_choice == "paper" and ai_choice == "rock":
        print("You win")
    elif your_choice == ai_choice:
        print("You draw")
    elif your_choice != "rock" and your_choice != "paper" and your_choice != "scissors":
        print("You chose an invalid answer, you lose")
    else:
        print("You lose")

    #stops the program if anything but y is inputed
    contstr = input("Input \"y\" to play again.\n")
    if contstr != "y":
        cont = False