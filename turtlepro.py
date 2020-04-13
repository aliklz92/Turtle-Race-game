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





# screen = turtle.Screen()
# turtle.setup(1024, 768)
# screen.bgcolor("#FFFFE0")
# box_size = 500
# spe=[50,150,250,350,500,700,850]
# colors = ["black", "red", "orange", "green", "blue"]
#
#
# def create_turtle(color):
#     t = turtle.Turtle()
#     t.speed(0)
#     t.width(3)
#     t.shape("turtle")
#     t.color(color)
#     return t
#
# def create_turtles(colors):
#     turtles = []
#     for color in colors:
#         t = create_turtle(color)
#     turtles.append(t)
#     return turtles
#
# turt=create_turtles(colors)
# def move(t):
#     t.left(90)
#     t.forward(100)
# for i in range(5):
#         for j in turt:
#                 move(j)

# def move_turtle(t):
#         # t.stamp()
#         # angle = random.randint(-90, 90)
#         # t.right(angle)
#         # distance = random.randint(50, 100)
#         # t.forward(distance)
#         t.setpos(-300,-280)
#         t.speed(5)
#         t.left(90)
#         t.forward(300)
#
#
# turtles = create_turtles(colors)
#
# t1 = turtles[0]
# t1.penup()
# t1.goto(box_size / 2, box_size / 2)
# t1.pendown()
#
# for side in range(4):
#         t1.right(90)
#         t1.forward(box_size)
#
# t1.penup()
# t1.goto(0, 0)
# t1.pendown()
#
# for move in range(5):
#         for a_turtle in turtles:
#                 move_turtle(a_turtle)

# seed()
# DELAY = 100
# a = Turtle('turtle', visible=False)
# a.speed(random.randint(0,10))
# a.color('red')
# a.left(90)
# a.penup()
# a.setpos(-280,-280)
# # a.setheading(0)
# a.pendown()
# a.showturtle()
#
# b = Turtle('turtle', visible=False)
# b.speed(random.randint(0,10))
# b.color('green')
# b.left(90)
# b.penup()
# b.setpos(-140,-280)
# b.setheading(90)
# b.pendown()
# b.showturtle()
#
# ### Subsequent variations start here ###
#
# def move(turtle):
#     turtle.forward(10)
#
#     if turtle.distance(0, 0) > 1 :
#         screen.ontimer(lambda t=turtle: move(t), 50)
#
# move(a)
# move(b)


### Subsequent variations end here ###

# screen.mainloop()
# playGround.screensize(*picSize)
# spe=[2,10,20,5,25,35,6,22,33]
# colors = ['red', 'green', 'gray', 'pink', 'black', 'yellow', 'purple', 'brown', 'blue']
# def one():
#     one = turtle.Turtle()
#     one.color(random.choice(colors))
#     one.shape('turtle')
#     one.penup()
#     one.setpos(-280,-280)
#     one.pendown()
#     one.left(90)
# def two():
#     two=turtle.Turtle()
#     two.color(random.choice(colors))
#     two.shape('turtle')
#     two.penup()
#     two.setpos(-140,-280)
#     two.left(90)
#     two.pendown()
#
#
# three=turtle.Turtle()
# three.color(random.choice(colors))
# three.shape('turtle')
# three.penup()
# three.setpos(0,-280)
# three.left(90)
# three.pendown()
#
#
#
# four=turtle.Turtle()
# four.color(random.choice(colors))
# four.shape('turtle')
# four.penup()
# four.setpos(+140,-280)
# four.left(90)
# four.pendown()
# def move():
#     one.speed(random.choice(spe))
#     playGround.ontimer(move, DELAY)
# move()

# five=turtle.Turtle()
# five.color(random.choice(colors))
# five.shape('turtle')
# five.penup()
# five.setpos(+280,-280)
# five.left(90)
# five.pendown()
# turt=[one,two,three,four,five]


# text=input("Do you want to play? "
#            "press Y for yes!"
#            "Press Q for quit the game!")

# one.speed(random.choice(spe))
# two.speed(random.choice(spe))
# three.speed(random.choice(spe))
# four.speed(random.choice(spe))
# five.speed(random.choice(spe))
# one.forward(200)
# two.forward(200)
#
# three.forward(200)
#
# four.forward(200)
# five.forward(200)
# for i in turt:
#      i.speed(random.choice(spe))
#      i.forward(300)


# tlist = list()
# colorlist = ["red", "green", "black", "blue", "brown"]
# for i in range(5):
#     tlist.append(turtle.Turtle(shape="turtle"))
#     tlist[i].color(colorlist[i])
#     tlist[i].speed(1)
# screen = turtle.getscreen()
# for i in range(100):
#     screen.tracer(1000)
#     for t in tlist:
#         t.right((np.random.rand(1) - .5) * 180)
#         t.forward(int((np.random.rand(1) - .5) * 100))
#     screen.update()
#
#
# count=0
# while text !="q":
#
#     if text=="y":
#         one.forward(100)

        # text = input("Do you want to play? "
        #              "press Y for yes!"
        #              "Press Q for quit the game!")








os.system("pause")


# ali=turtle.Turtle()
# colors=['red', 'green', 'gray', 'pink', 'yellow']
# ali.color('red', 'blue')
# ali.width(5)
# ali.begin_fill()
# ali.circle(50)
# ali.end_fill()
# for x in range(5):
#     randColor=random.randrange(0,len(colors))
#     ali.color(colors[randColor],colors[random.randrange(0,len(colors))])
#     rand1=random.randrange(-300,300)
#     rand2=random.randrange(-300,300)
#     ali.penup()
#     ali.setpos(rand1,rand2)
#     ali.pendown()
#     ali.begin_fill()
#     ali.circle(random.randrange(0,70))
#     ali.end_fill()
# class race():
#     def __init__(self,color,pos):
#         self.pos=pos
#         self.color=color
#         self.turt = turtle.Turtle()
#         self.shape('turtle')
#         self.turt.color(color)
#         self.turt.penup()
#         self.turt.setpos(pos)
#         self.turt.setheading(90)
#         def move(self):
#             rand=random.randrange(1,25)
#             self.pos=(self.pos[0],self.pos[1]+rand)
#             self.turt.pendown()
#             self.turt.forward(rand)
#

# ali=turtle.Turtle()
# reza=turtle.Turtle()
# turtle.setworldcoordinates(-5, -5, 130, 130)
#
# ali.color('red')
# ali.pensize(5)
# ali.shape('turtle')
# ali.forward(100)
# reza.color('green')
# reza.pensize(10)
# reza.shape('turtle')
# reza.forward(100)


# window_len = 700
# window_hgh = 700
# turtles = 8
#
# turtle.screensize(window_len, window_hgh)










