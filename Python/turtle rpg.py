import turtle

dialog = ["Oooh hello traveler! You probably want to go thorugh don't you?", 
"Well if you want to get past me, you must answer me, these riddles three.","The alphabet goes A-Z but I go Z-A, What am I?"]
page = -1
question = False

ws = turtle.Screen()
ws.screensize(600, 600)
ws.bgcolor("black")
ws.title("RPG")
ws.listen()

player = turtle.Turtle()
player.penup()
player.color("white")
player.speed(0)
player.shape("classic")
player.goto(200,200)
player.shapesize(2)
player.hideturtle()

enemy = turtle.Turtle()
enemy.shape("circle")
enemy.shapesize(1.5)
enemy.penup()
enemy.hideturtle()
enemy.goto(0,100)
enemy.color("green")

txt = turtle.Turtle()
txt.color("white")
txt.penup()
txt.speed(0)
txt.goto(0,260)
txt.hideturtle()
txt.write("PRESS ANY KEY TO START", align="center", font=("Arial", 26, "normal"))

def nextline():
    global page
    page += 1
    txt.clear()
    if page == 2:
        question = True
    if question == False:
        txt.write(dialog[page], align="center", font=("Arial", 20, "normal"))

def drawroom():
    player.penup()
    player.goto(200,-200)
    player.pendown()
    for x in range(4):
        player.left(90)
        player.fd(400)
    player.penup()
    player.goto(0,-100)
    player.left(90)

gamestarted = False

def goblinroom():
    drawroom()
    global gamestarted
    gamestarted = True
    enemy.goto(0,100)
    enemy.shape("circle")
    enemy.shapesize(1.5)
    enemy.showturtle()
    player.showturtle()

if gamestarted != True:
    ws.onkeypress(goblinroom)

if gamestarted == True:
    ws.onkeypress(nextline, "space")

while True:
    ws.update()