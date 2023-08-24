import turtle
from turtle import Turtle,Screen
from update import Update

import pandas

data=pandas.read_csv('50_states.csv')
states=data['state']
cursor=Turtle()
screen=Screen()
screen.title('Us states game')
image='blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
update_score=Update()
score=0
for x in range(0,len(states)):
    user=screen.textinput(f"{score}/{x}","Guess a state").title()
    for state in states:
        if f"{user}" == f"{state}":
            score+=1
            user = data[states == f'{user}']
            print(user)
            update_score.update_data(int(user['x']),int(user['y']),f'{state}')
        else:
            pass

screen.exitonclick()