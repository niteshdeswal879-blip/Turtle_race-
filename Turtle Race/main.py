from turtle import Turtle,Screen
import time
import random
screen=Screen()
screen.setup(width=600, height=500)

user_input=screen.textinput(title="new_turtle a bet", prompt="Which color turtle will win the race\nChoose from the color (Yellow, Red, Blue, Green, Violet, Orange)")
colors=["red","violet","blue","green","yellow","orange",]
x=-60
all_turtles=[]
for i in colors:
    new_turtle=Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(x=-280,y=x)
    all_turtles.append(new_turtle)
    x+=30
screen.tracer(0)
if user_input:
    is_race=True
while is_race:
    for j in  all_turtles:
        if j.xcor()>270:
            winning_color=j.pencolor()
            if winning_color== user_input:
                print(f"You have won, The winning turtle color is {winning_color}")
                is_race=False
            else:
                print(f"You have lost, The winning turtle color is {winning_color}")
                is_race=False
        j.forward(random.randint(0,10))

    screen.update()
    time.sleep(0.1)







screen.exitonclick()
