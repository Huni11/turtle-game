import turtle
import random

asteroids=[]
for i in range(10):
    a1=turtle.Turtle()
    a1.color("red") #소행성은 빨간색입니다.
    a1.shape("circle")
    a1.penup()
    a1.speed(0)
    a1.goto(random.randint(-300,300),random.randint(-300,300))
    asteroids.append(a1) #소행성 리스트에 추가합니다.

import turtle
player=turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)

screen=player.getscreen()
def turnleft():
    player.left(40) #왼쪽으로 40도 회전한다.

def turnright():
    player.right(40) #오른쪽으으로 40도 회전한다.

def turnup():
    player.forward(30)

screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright,"Right")
screen.onkeypress(turnup)
screen.listen()

def play():
    player.forward(2)   #터틀 우주선2픽셀 전진

    for a in asteroids: #리스트에 저장된 모든 소행성에 대하여
        a.right(random.randint(-180,180))   #소행성들이 -180~180사이의 값으로
        a.forward(5)

        if player.distance(a)<20:
            player.write("clear")
            a.ht()

    screen.ontimer(play,10)     #10ms가 지나면 play를 다시 호출합니다.

screen.ontimer(play,10)
