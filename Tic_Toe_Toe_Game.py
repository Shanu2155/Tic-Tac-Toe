import turtle
import sys
import numpy as np

#turtle to draw the initial boxes

turtle.speed(0)
turtle.bgcolor("white")
turtle.pencolor("black")
turn=0
arr1=np.zeros(9)
arr2=np.zeros(9)
count=0
sw=1
c=np.zeros(8)
d=np.zeros(8)
def draw_maze():
    def rectan(x,y):
        turtle.penup()
        turtle.goto(x,y)
        for i in range(4):
            turtle.pendown()
            turtle.fd(100)
            turtle.left(90)
  
    rectan(-100,-100)
    rectan(0,-100)
    rectan(100,-100)
    rectan(-100,0)
    rectan(0,0)
    rectan(100,0)
    rectan(-100,100)
    rectan(0,100)
    rectan(100,100)

draw_maze()
turtle.penup()

#function insert checks the position of symbol and marks it in respective array
def insert(x,y,col):
    global count
    if -100<=x<0 and -100<=y<0 and col==1:
        arr1[0]=1
        if arr2[0]==1:
            arr2[0]=0
        else:
            count=count+1
    elif -100<=x<0 and -100<=y<0 and col==2:
        arr2[0]=1
        if arr1[0]==1:
            arr1[0]=0
        else:
            count=count+1
    elif 0<=x<100 and -100<=y<0 and col==1:
        arr1[1]=1
        if arr2[1]==1:
            arr2[1]=0
        else:
            count=count+1
    elif 0<=x<100 and -100<=y<0 and col==2:
        arr2[1]=1
        if arr1[1]==1:
            arr1[1]=0
        else:
            count=count+1
    elif 100<=x<200 and -100<=y<0 and col==1:
        arr1[2]=1
        if arr2[2]==1:
            arr2[2]=0
        else:
            count=count+1
    elif 100<=x<200 and -100<=y<0 and col==2:
        arr2[2]=1
        if arr1[2]==1:
            arr1[2]=0
        else:
            count=count+1

            
    elif -100<=x<0 and 0<=y<100 and col==1:
        arr1[3]=1
        if arr2[3]==1:
            arr2[3]=0
        else:
            count=count+1
    elif -100<=x<0 and 0<=y<100 and col==2:
        arr2[3]=1
        if arr1[3]==1:
            arr1[3]=0
        else:
            count=count+1
    elif 0<=x<100 and 0<=y<100 and col==1:
        arr1[4]=1
        if arr2[4]==1:
            arr2[4]=0
        else:
            count=count+1
    elif 0<=x<100 and 0<=y<100 and col==2:
        arr2[4]=1
        if arr1[4]==1:
            arr1[4]=0
        else:
            count=count+1
    elif 100<=x<200 and 0<=y<100 and col==1:
        arr1[5]=1
        if arr2[5]==1:
            arr2[5]=0
        else:
            count=count+1
    elif 100<=x<200 and 0<=y<100 and col==2:
        arr2[5]=1
        if arr1[5]==1:
            arr1[5]=0
        else:
            count=count+1

    elif -100<=x<0 and 100<=y<200 and col==1:
        arr1[6]=1
        if arr2[6]==1:
            arr2[6]=0
        else:
            count=count+1
    elif -100<=x<0 and 100<=y<200 and col==2:
        arr2[6]=1
        if arr1[6]==1:
            arr1[6]=0
        else:
            count=count+1
    elif 0<=x<100 and 100<=y<200 and col==1:
        arr1[7]=1
        if arr2[7]==1:
            arr2[7]=0
        else:
            count=count+1
    elif 0<=x<100 and 100<=y<200 and col==2:
        arr2[7]=1
        if arr1[7]==1:
            arr1[7]=0
        else:
            count=count+1
    elif 100<=x<200 and 100<=y<200 and col==1:
        arr1[8]=1
        if arr2[8]==1:
            arr2[8]=0
        else:
            count=count+1
    elif 100<=x<200 and 100<=y<200 and col==2:
        arr2[8]=1
        if arr1[8]==1:
            arr1[8]=0
        else:
            count=count+1

#func check() checks for the winning logic of game for either player.
#It also checks for invalid move or game draw

def check():
    global sw
    c[0]=arr1[0]+arr1[1]+arr1[2]
    c[1]=arr1[3]+arr1[4]+arr1[5]
    c[2]=arr1[6]+arr1[7]+arr1[8]
    c[3]=arr1[0]+arr1[3]+arr1[6]
    c[4]=arr1[1]+arr1[4]+arr1[7]
    c[5]=arr1[5]+arr1[8]+arr1[2]
    c[6]=arr1[0]+arr1[4]+arr1[8]
    c[7]=arr1[6]+arr1[4]+arr1[2]

    d[0]=arr2[0]+arr2[1]+arr2[2]
    d[1]=arr2[3]+arr2[4]+arr2[5]
    d[2]=arr2[6]+arr2[7]+arr2[8]
    d[3]=arr2[0]+arr2[3]+arr2[6]
    d[4]=arr2[1]+arr2[4]+arr2[7]
    d[5]=arr2[5]+arr2[8]+arr2[2]
    d[6]=arr2[0]+arr2[4]+arr2[8]
    d[7]=arr2[6]+arr2[4]+arr2[2]

    for i in range(0,8):
        if c[i]==3 and sw==1:
            print "Player 1 is winner"
            sw=2
            turtle.done()
            exit()
        elif d[i]==3 and sw==1:
            print "Player 2 is winner"
            sw=2
            turtle.done()
            exit()
        elif sw==2:
            print "Invalid"
            turtle.done()
            exit()
        elif count==9:
            print "Game Draw"
            turtle.done()
            exit()

#func blue color is for both players. It checks the coordinate and mark color.
#It then calls insert and that logic is performed
            
def bluecol():
    global count
    global turn
    turtle.pendown()
    x=turtle.xcor()
    y=turtle.ycor()
    if turn==0:
        insert(x,y,1)
        turtle.dot(50,'blue')
        turn=1
    else:
        insert(x,y,2)
        turtle.dot(50,'red')
        turn=0
    turtle.penup()
    check()
    if count==9:
        print "Match is draw"
        turtle.done()
        exit()

        
##def greencol():
##    global count
##    turtle.pendown()
##    x=turtle.xcor()
##    y=turtle.ycor()
##    insert(x,y,2)
##    turtle.dot(70,'green')
##    turtle.penup()
##    check()
##    if count==9:
##        print "Match is draw"
##        turtle.done()
##        exit()

        
turtle.onscreenclick(turtle.goto)
turtle.onkey(bluecol,"a")
#turtle.onkey(greencol,"b")

turtle.listen()
turtle.mainloop()
