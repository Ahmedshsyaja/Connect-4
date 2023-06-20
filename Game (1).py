import turtle 
import time
global m
m=False
loc1 = [[0 for j in range(8)] for i in range(2)]
loc2 = [[0 for j in range(8)] for i in range(2)]
loc3 = [[0 for j in range(8)] for i in range(2)]
loc4 = [[0 for j in range(8)] for i in range(2)]
loc5 = [[0 for j in range(8)] for i in range(2)]
loc6 = [[0 for j in range(8)] for i in range(2)]
loc7 = [[0 for j in range(8)] for i in range(2)]
loc8 = [[0 for j in range(8)] for i in range(2)]
result = [[0 for j in range(8)] for i in range(8)]
# Create a turtle object
t = turtle.Turtle()
t.speed(0)
# Move turtle to the starting position
t.penup()
t.goto(-275, 350)
t.pendown()
turtle.title("Player 1 Turn")
# Draw the box and fill it with light blue color
# set the fill color to white
# start filling the shape
for i in range(4):
    t.forward(610)
    t.right(90)
t.end_fill() # end filling the shape

t.hideturtle()
t.penup()
t.goto(-270, -240)
t.pendown()
for i in range(2):
    t.forward(70)
    t.right(90)
    t.forward(10)
    t.right(90)
t.end_fill()
t.hideturtle()
t.penup()
t.goto(-195, -240)
t.pendown()
for i in range(2):
    t.forward(70)
    t.right(90)
    t.forward(10)
    t.right(90)
t.end_fill()
t.hideturtle()
t.penup()
t.goto(-120, -240)
t.pendown()
for i in range(2):
    t.forward(70)
    t.right(90)
    t.forward(10)
    t.right(90)
t.end_fill()
t.hideturtle()
t.penup()
t.goto(-45, -240)
t.pendown()
for i in range(2):
    t.forward(70)
    t.right(90)
    t.forward(10)
    t.right(90)
t.end_fill()
t.hideturtle()
t.penup()
t.goto(30, -240)
t.pendown()
for i in range(2):
    t.forward(70)
    t.right(90)
    t.forward(10)
    t.right(90)
t.end_fill()
t.hideturtle()
t.penup()
t.goto(105, -240)
t.pendown()
for i in range(2):
    t.forward(70)
    t.right(90)
    t.forward(10)
    t.right(90)
t.end_fill()
t.hideturtle()
t.penup()
t.goto(180, -240)
t.pendown()
for i in range(2):
    t.forward(70)
    t.right(90)
    t.forward(10) 
    t.right(90)
t.end_fill()
t.hideturtle()
t.penup()
t.goto(255, -240)
t.pendown()
for i in range(2):
    t.forward(70)
    t.right(90)
    t.forward(10)
    t.right(90)
t.end_fill()

global pos1_x1
pos1_x1=0
global pox1_y2
pox1_y2=0
global pos1_x2
pos1_x2=0
global pox1_y3
pox1_y3=0
global pos1_x3
pos1_x3=0
global pox1_y4
pox1_y4=0
global pos1_x4
pos1_x4=0
global pox1_y5
pox1_y5=0
global pos1_x5
pos1_x5=0
global pox1_y6
pox1_y6=0
global pos1_x6
pos1_x6=0
global pox1_y7
pox1_y7=0
global pos1_x7
pos1_x7=0
global pox1_y8
pox1_y8=0
global pos1_x8
pos1_x8=0
global pox1_y9
pox1_y9=0
global count
count=0
def draw_circle(x,y,count):
    global pos1_x1
    global pox1_y2
    global pos1_x2
    global pox1_y3
    global pos1_x3
    global pox1_y4
    global pos1_x4
    global pox1_y5
    global pos1_x5
    global pox1_y6
    global pos1_x6
    global pox1_y7
    global pos1_x7
    global pox1_y8
    global pos1_x8
    global pox1_y9
    if count%2==0:
        turtle.pencolor("blue")
    else:
        turtle.pencolor("black")
    #print(x)
    if x >= -275 and x <=-195 :
         if loc1[0][pos1_x1]<=-235 and loc1[1][pox1_y2]<-230:
             tx=-235
             ty=loc1[1][pox1_y2-1]
             ty=ty+70
             loc1[0][pos1_x1]=-235
             loc1[1][pox1_y2]=ty
             if count%2==0:
                 result[pox1_y2][0]=1
             else:
                 result[pox1_y2][0]=0
             pox1_y2=pox1_y2+1
             turtle.speed(0)
             turtle.penup()
             turtle.setpos(tx, ty)
             turtle.pendown()
             if count%2==0:
                 turtle.fillcolor("purple")
             else:
                  turtle.fillcolor("blue")
             turtle.begin_fill()
             turtle.circle(30)
             turtle.end_fill()
         if  pos1_x1==0 and pox1_y2==0:
             turtle.speed(0)
             turtle.penup()
             turtle.setpos(loc1[0][pos1_x1], loc1[1][pox1_y2])
             turtle.pendown()
             if count%2==0:
                 turtle.fillcolor("purple")
             else:
                  turtle.fillcolor("blue")
             turtle.begin_fill()
             turtle.circle(30)
             turtle.end_fill() 
             if count%2==0:
                 result[pox1_y2][0]=1
             else:
                 result[pox1_y2][0]=0  
             pos1_x1=pos1_x1+1
             pox1_y2=pox1_y2+1
    if x > -195 and x <=-128 :
         if loc2[0][pos1_x2]<=-160 and loc2[1][pox1_y3]<-230:
             tx=-160
             ty=loc2[1][pox1_y3-1]
             ty=ty+70
             loc2[0][pos1_x2]=-160
             loc2[1][pox1_y3]=ty
             if count%2==0:
                 result[pox1_y3][1]=1
             else:
                 result[pox1_y3][1]=0 
             pox1_y3=pox1_y3+1
             turtle.speed(0)
             turtle.penup()
             turtle.setpos(tx, ty)
             turtle.pendown()
             if count%2==0:
                 turtle.fillcolor("purple")
             else:
                  turtle.fillcolor("blue")
             turtle.begin_fill()
             turtle.circle(30)
             turtle.end_fill()
         if  pos1_x2==0 and pox1_y3==0:
             turtle.speed(0)
             turtle.penup()
             turtle.setpos(loc2[0][pos1_x2], loc2[1][pox1_y3])
             turtle.pendown()
             if count%2==0:
                 turtle.fillcolor("purple")
             else:
                  turtle.fillcolor("blue")
             turtle.begin_fill()
             turtle.circle(30)
             turtle.end_fill()
             if count%2==0:
                 result[pox1_y3][1]=1
             else:
                 result[pox1_y3][1]=0 
             pos1_x2=pos1_x2+1
             pox1_y3=pox1_y3+1
    if x > -128 and x <= -53:
        if loc3[0][pos1_x3] <= -85 and loc3[1][pox1_y4] < -230:
             tx = -85
             ty = loc3[1][pox1_y4 - 1]
             ty = ty + 70
             loc3[0][pos1_x3] = -85
             loc3[1][pox1_y4] = ty
             if count%2==0:
                 result[pox1_y4][2]=1
             else:
                 result[pox1_y4][2]=0 
             pox1_y4 = pox1_y4 + 1
             turtle.speed(0)
             turtle.penup()
             turtle.setpos(tx, ty)
             turtle.pendown()
             if count%2==0:
                 turtle.fillcolor("purple")
             else:
                  turtle.fillcolor("blue")
             turtle.begin_fill()
             turtle.circle(30)
             turtle.end_fill()
        if pos1_x3 == 0 and pox1_y4 == 0:
             turtle.speed(0)
             turtle.penup()
             turtle.setpos(loc3[0][pos1_x3], loc3[1][pox1_y4])
             turtle.pendown()
             if count%2==0:
                 turtle.fillcolor("purple")
             else:
                  turtle.fillcolor("blue")
             turtle.begin_fill()
             turtle.circle(30)
             turtle.end_fill()
             if count%2==0:
                 result[pox1_y4][2]=1
             else:
                 result[pox1_y4][2]=0 
             pos1_x3 = pos1_x3 + 1
             pox1_y4 = pox1_y4 + 1
    if x > -53 and x <= 25:
        if loc4[0][pos1_x4] <= -10 and loc4[1][pox1_y5] < -230:
             tx = -10
             ty = loc4[1][pox1_y5 - 1]
             ty = ty + 70
             loc4[0][pos1_x4] = -10
             loc4[1][pox1_y5] = ty
             if count%2==0:
                 result[pox1_y5][3]=1
             else:
                 result[pox1_y5][3]=0 
             pox1_y5 = pox1_y5 + 1
             turtle.speed(0)
             turtle.penup()
             turtle.setpos(tx, ty)
             turtle.pendown()
             if count%2==0:
                 turtle.fillcolor("purple")
             else:
                  turtle.fillcolor("blue")
             turtle.begin_fill()
             turtle.circle(30)
             turtle.end_fill()
        if pos1_x4 == 0 and pox1_y5 == 0:
             turtle.speed(0)
             turtle.penup()
             turtle.setpos(loc4[0][pos1_x4], loc4[1][pox1_y5])
             turtle.pendown()
             if count%2==0:
                 turtle.fillcolor("purple")
             else:
                  turtle.fillcolor("blue")
             turtle.begin_fill()
             turtle.circle(30)
             turtle.end_fill()
             if count%2==0:
                 result[pox1_y5 ][3]=1
             else:
                 result[pox1_y5 ][3]=0 
             pos1_x4 = pos1_x4 + 1
             pox1_y5 = pox1_y5 + 1
    if x > 25 and x <= 98:
        if loc5[0][pos1_x5] <= 65 and loc5[1][pox1_y6] < -230:
              tx = 65
              ty = loc5[1][pox1_y6 - 1]
              ty = ty + 70
              loc5[0][pos1_x5] = 65
              loc5[1][pox1_y6] = ty
              if count%2==0:
                 result[pox1_y6][4]=1
              else:
                 result[pox1_y6][4]=0 
              pox1_y6 = pox1_y6 + 1
              turtle.speed(0)
              turtle.penup()
              turtle.setpos(tx, ty)
              turtle.pendown()
              if count%2==0:
                 turtle.fillcolor("purple")
              else:
                  turtle.fillcolor("blue")
              turtle.begin_fill()
              turtle.circle(30)
              turtle.end_fill()
        if pos1_x5 == 0 and pox1_y6 == 0:
             turtle.speed(0)
             turtle.penup()
             turtle.setpos(loc5[0][pos1_x5], loc5[1][pox1_y6])
             turtle.pendown()
             if count%2==0:
                 turtle.fillcolor("purple")
             else:
                  turtle.fillcolor("blue")
             turtle.begin_fill()
             turtle.circle(30)
             turtle.end_fill()
             if count%2==0:
                 result[pox1_y6][4]=1
             else:
                 result[pox1_y6][4]=0 
             pos1_x5 = pos1_x5 + 1
             pox1_y6 = pox1_y6 + 1
    if x > 98 and x <= 175:
        if loc6[0][pos1_x6] <= 140 and loc6[1][pox1_y7] < -230:
              tx = 140
              ty = loc6[1][pox1_y7 - 1]
              ty = ty + 70
              loc6[0][pos1_x6] = 140
              loc6[1][pox1_y7] = ty
              if count%2==0:
                 result[pox1_y7][5]=1
              else:
                 result[pox1_y7][5]=0 
              pox1_y7 = pox1_y7 + 1
              turtle.speed(0)
              turtle.penup()
              turtle.setpos(tx, ty)
              turtle.pendown()
              if count%2==0:
                 turtle.fillcolor("purple")
              else:
                  turtle.fillcolor("blue")
              turtle.begin_fill()
              turtle.circle(30)
              turtle.end_fill()
              turtle.hideturtle()
        if pos1_x6 == 0 and pox1_y7 == 0:
              turtle.speed(0)
              turtle.penup()
              turtle.setpos(loc6[0][pos1_x6], loc6[1][pox1_y7])
              turtle.pendown()
              if count%2==0:
                 turtle.fillcolor("purple")
              else:
                  turtle.fillcolor("blue")
              turtle.begin_fill()
              turtle.circle(30)
              turtle.end_fill()
              turtle.hideturtle()
              if count%2==0:
                 result[pox1_y7][5]=1
              else:
                 result[pox1_y7][5]=0 
              pos1_x6 = pos1_x6 + 1
              pox1_y7 = pox1_y7 + 1
    if x > 175 and x <= 248:
        if loc7[0][pos1_x7] <= 215 and loc7[1][pox1_y8] < -230:
              tx = 215
              ty = loc7[1][pox1_y8 - 1]
              ty = ty + 70
              loc7[0][pos1_x7] = 215
              loc7[1][pox1_y8] = ty
              if count%2==0:
                 result[pox1_y8][6]=1
              else:
                 result[pox1_y8][6]=0 
              pox1_y8 = pox1_y8 + 1
              turtle.speed(0)
              turtle.penup()
              turtle.setpos(tx, ty)
              turtle.pendown()
              if count%2==0:
                 turtle.fillcolor("purple")
              else:
                  turtle.fillcolor("blue")
              turtle.begin_fill()
              turtle.circle(30)
              turtle.end_fill()
              turtle.hideturtle()
        if pos1_x7 == 0 and pox1_y8 == 0:
              turtle.speed(0)
              turtle.penup()
              turtle.setpos(loc7[0][pos1_x7], loc7[1][pox1_y8])
              turtle.pendown()
              if count%2==0:
                 turtle.fillcolor("purple")
              else:
                  turtle.fillcolor("blue")
              turtle.begin_fill()
              turtle.circle(30)
              turtle.end_fill()
              turtle.hideturtle()
              if count%2==0:
                 result[pox1_y8][6]=1
              else:
                 result[pox1_y8][6]=0 
              pos1_x7 = pos1_x7 + 1
              pox1_y8 = pox1_y8 + 1
    if x > 248 and x <= 325:
        if loc8[0][pos1_x8] <= 290 and loc8[1][pox1_y9] < -230:
              tx = 290
              ty = loc8[1][pox1_y9 - 1]
              ty = ty + 70
              loc8[0][pos1_x8] = 290
              loc8[1][pox1_y9] = ty
              if count%2==0:
                 result[pox1_y9][7]=1
              else:
                 result[pox1_y9][7]=0 
              pox1_y9 = pox1_y9 + 1
              turtle.speed(0)
              turtle.penup()
              turtle.setpos(tx, ty)
              turtle.pendown()
              if count%2==0:
                 turtle.fillcolor("purple")
              else:
                  turtle.fillcolor("blue")
              turtle.begin_fill()
              turtle.circle(30)
              turtle.end_fill()
              turtle.hideturtle()
        if pos1_x8 == 0 and pox1_y9 == 0:
              turtle.speed(0)
              turtle.penup()
              turtle.setpos(loc8[0][pos1_x8], loc8[1][pox1_y9])
              turtle.pendown()
              if count%2==0:
                 turtle.fillcolor("purple")
              else:
                  turtle.fillcolor("blue")
              turtle.begin_fill()
              turtle.circle(30)
              turtle.end_fill()
              turtle.hideturtle()
              if count%2==0:
                 result[pox1_y9][7]=1
              else:
                 result[pox1_y9][7]=0 
              pos1_x8 = pos1_x8 + 1
              pox1_y9 = pox1_y9 + 1


def check():
   for i in range(8):
    for j in range(8):
        print(result[i][j], end=' ')
    print() # print a new line for each row

           
def check_consecutive_ones(arr):
    for i in range(4):
        for j in range(4):
            if arr[i][j] == arr[i+1][j+1] == arr[i+2][j+2] == arr[i+3][j+3] == 1:
                return True
    
    # check upper left diagonal
    for i in range(4):
        for j in range(3, 8):
            if arr[i][j] == arr[i+1][j-1] == arr[i+2][j-2] == arr[i+3][j-3] == 1:
                return True
    
    # check left diagonal
    for i in range(5):
        for j in range(4):
            if arr[i][j] == arr[i+1][j+1] == arr[i+2][j+2] == arr[i+3][j+3] == 1:
                return True
    
    # check lower left diagonal
    for i in range(3, 8):
        for j in range(4):
            if arr[i][j] == arr[i-1][j+1] == arr[i-2][j+2] == arr[i-3][j+3] == 1:
                return True
    
    # check lower right diagonal
    for i in range(3, 8):
        for j in range(3, 8):
            if arr[i][j] == arr[i-1][j-1] == arr[i-2][j-2] == arr[i-3][j-3] == 1:
                return True
    
    # check left columns
    for i in range(8):
        for j in range(5):
            if arr[i][j] == arr[i][j+1] == arr[i][j+2] == arr[i][j+3] == 1:
                return True
    
    # check lower rows
    for i in range(5):
        for j in range(8):
            if arr[i][j] == arr[i+1][j] == arr[i+2][j] == arr[i+3][j] == 1:
                return True
    
    # check right columns
    for i in range(8):
        for j in range(3, 8):
            if arr[i][j] == arr[i][j-1] == arr[i][j-2] == arr[i][j-3] == 1:
                return True
    
    # check special cases
    if arr[0][0] == arr[1][1] == arr[2][2] == arr[3][3] == 1:
        return True
    
    for j in range(1, 8):
        if arr[0][j] == arr[1][j-1] == arr[2][j-2] == arr[3][j-3] == 1:
            return True
    
    if arr[0][7] == arr[1][6] == arr[2][5] == arr[3][4] == 1:
        return True
    
    for i in range(1, 8):
        if arr[i][0] == arr[i-1][1] == arr[i-2][2] == arr[i-3][3] == 1:
            return True
    
    # if no consecutive zeros found, return False
    return False


def check_consecutive_zeros(arr):
    for i in range(4):
        for j in range(4):
            if arr[i][j] == arr[i+1][j+1] == arr[i+2][j+2] == arr[i+3][j+3] == 0:
                return True
    
    # check upper left diagonal
    for i in range(4):
        for j in range(3, 8):
            if arr[i][j] == arr[i+1][j-1] == arr[i+2][j-2] == arr[i+3][j-3] == 0:
                return True
    
    # check left diagonal
    for i in range(5):
        for j in range(4):
            if arr[i][j] == arr[i+1][j+1] == arr[i+2][j+2] == arr[i+3][j+3] == 0:
                return True
    
    # check lower left diagonal
    for i in range(3, 8):
        for j in range(4):
            if arr[i][j] == arr[i-1][j+1] == arr[i-2][j+2] == arr[i-3][j+3] == 0:
                return True
    
    # check lower right diagonal
    for i in range(3, 8):
        for j in range(3, 8):
            if arr[i][j] == arr[i-1][j-1] == arr[i-2][j-2] == arr[i-3][j-3] == 0:
                return True
    
    # check left columns
    for i in range(8):
        for j in range(5):
            if arr[i][j] == arr[i][j+1] == arr[i][j+2] == arr[i][j+3] == 0:
                return True
    
    # check lower rows
    for i in range(5):
        for j in range(8):
            if arr[i][j] == arr[i+1][j] == arr[i+2][j] == arr[i+3][j] == 0:
                return True
    
    # check right columns
    for i in range(8):
        for j in range(3, 8):
            if arr[i][j] == arr[i][j-1] == arr[i][j-2] == arr[i][j-3] == 0:
                return True
    
    # check special cases
    if arr[0][0] == arr[1][1] == arr[2][2] == arr[3][3] == 0:
        return True
    
    for j in range(1, 8):
        if arr[0][j] == arr[1][j-1] == arr[2][j-2] == arr[3][j-3] == 0:
            return True
    
    if arr[0][7] == arr[1][6] == arr[2][5] == arr[3][4] == 0:
        return True
    
    for i in range(1, 8):
        if arr[i][0] == arr[i-1][1] == arr[i-2][2] == arr[i-3][3] == 0:
            return True
    
    # if no consecutive zeros found, return False
    return False


def player(x,y):
    global m
    global count
    count=count+1;
    if count%2==0:
        turtle.title("Player 2 Turn")
    else:
        turtle.title("Player 1 Turn")
    if m!=True :
         draw_circle(x,y,count)
    check()
    if check_consecutive_ones(result)==True:
           turtle.title("Winner ! Player 1")
           m=True
    if check_consecutive_zeros(result)==True: 
           turtle.title("Winner ! Player 2") 
           m=True
    print()
    
    

    


             


#location intilizer
for i in range(2):
    for j in range(8):
        loc1[i][j]=-1111111111111
        if i==0:
          loc1[i][j]=-235
        if i==1 and j==0 :
            loc1[i][j]=-230

for i in range(2):
    for j in range(8):
        loc2[i][j]=-1111111111111
        if i==0:
          loc2[i][j]=-160
        if i==1 and j==0 :
            loc2[i][j]=-230    

for i in range(2):
    for j in range(8):
        loc3[i][j]=-1111111111111
        if i==0:
          loc3[i][j]=-85
        if i==1 and j==0 :
            loc3[i][j]=-230  

for i in range(2):
    for j in range(8):
        loc4[i][j]=-1111111111111
        if i==0:
          loc4[i][j]=-10
        if i==1 and j==0 :
            loc4[i][j]=-230   

for i in range(2):
    for j in range(8):
        loc5[i][j]=-1111111111111
        if i==0:
          loc5[i][j]=65
        if i==1 and j==0 :
            loc5[i][j]=-230  

for i in range(2):
    for j in range(8):
        loc6[i][j]=-1111111111111
        if i==0:
          loc6[i][j]=140
        if i==1 and j==0 :
            loc6[i][j]=-230    

for i in range(2):
    for j in range(8):
        loc7[i][j]=-1111111111111
        if i==0:
          loc7[i][j]=215
        if i==1 and j==0 :
            loc7[i][j]=-230 
             
for i in range(2):
    for j in range(8):
        loc8[i][j]=-1111111111111
        if i==0:
          loc8[i][j]=290
        if i==1 and j==0 :
            loc8[i][j]=-230  

for i in range(8):
    for j in range(8):
        result[i][j]=-1

#for i in range(2):
    #for j in range(8):
        #print(loc1[i][j])
        

#turtle.speed(0)
#turtle.penup()
#turtle.goto(-235, -230)
#turtle.pendown()
#turtle.circle(30)
#turtle.end_fill()
#turtle.hideturtle()

#turtle.speed(0)
#turtle.penup()
#turtle.goto(-235, -160)
#turtle.pendown()
#turtle.circle(30)
#turtle.end_fill()
#turtle.hideturtle()
# next plate
turtle.onscreenclick(player)
count=count+1;
print(count)
turtle.end_fill()
turtle.hideturtle()



# Hide the turtle
t.hideturtle()

#my_turtle = turtle.Turtle()
#my_turtle.speed(0)
#my_turtle.penup()
#my_turtle.goto(-220, 240)
#my_turtle.pendown()
#my_turtle.speed(0)
#my_turtle.circle(30)
#my_turtle.hideturtle()
# Keep the turtle window open until manually closed
turtle.done()



#for i in range(4):
 #   t.forward(100)
  #  t.right(90)

#turtle.done()
#import turtle
#screen = turtle.Screen()
#screen.bgcolor("blue")
#turtle.done()

