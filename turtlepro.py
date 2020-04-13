import math
import random
import turtle
#import time

win_length = 700
win_height = 700

turtles = 6

turtle.screensize(win_length, win_height)


class racer(object):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.turt = turtle.Turtle()
        self.turt.shape('turtle')
        self.turt.color(color)
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.left(90)

    def move(self):
        r = random.randrange(1, 20)
        self.pos = (self.pos[0], self.pos[1] + r)
        self.turt.pendown()
        self.turt.forward(r)

    def reset(self):
        self.turt.penup()
        self.turt.setpos(self.pos)

def startGame():
    tList = []
    turtle.clearscreen()
    turtle.hideturtle()
    colors = ["red", "green", "blue", 'yellow', 'purple', 'black', 'grey']
    start = -(win_length/2) + 25
    for t in range(turtles):
        newPosX = start + t*(win_length)/turtles
        tList.append(racer(colors[t],(newPosX, -230)))
        tList[t].turt.showturtle()

    run = True
    while run:
        for t in tList:
            t.move()

        wincolor = []
        maxDis = 0
        for t in tList:
            if t.pos[1] > 230 and t.pos[1] > maxDis:
                maxDis = t.pos[1]
                wincolor = []
                wincolor.append(t.color)
            elif t.pos[1] > 230 and t.pos[1] == maxDis:
                maxDis = t.pos[1]
                wincolor.append(t.color)

        if len(wincolor) > 0:
            run = False
            print('The winner is: ')
            for win in wincolor:
                print(win)


start = input('Would you like to play')
startGame()

while True:
    print('-----------------------------------')
    start = input('Would you like to play again')
    startGame()
