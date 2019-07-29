import turtle
'''turtle.shape('square')
finn=turtle.clone()
finn.shape('square')
finn.forward (100)
finn.right(90)
finn.forward(100)
finn.right(90)
finn.forward(100)
finn.right(90)
finn.forward(100)

sam.shape('triangle')
sam.left(45)
sam.stamp()
sam.forward(100)
sam.stamp()
sam.clearstamps()
sam.right(130)
sam.forward(100)'''
sam=turtle.clone()
sam.shape('circle')
turtle.bgcolor('purple')
sam.color('white')           
sam.stamp()



sam.goto(0,0)
sam.pensize(12)
sam.goto(0,100)
sam.color('yellow')
sam.goto(50,100)
sam.goto(50,0)
sam.color('green')
sam.goto(50,-100)
sam.goto(100,-100)
sam.color('blue')
sam.shape('arrow')
sam.goto(100,0)
def up():
    sam.setheading(90)
    sam.forward(50)
sam.onkeypress(up,'w')
def down():
    sam.setheading(180)
    sam.forward(50)
sam.onkeypress(down,'s')
def left():
    sam.setheadling(270)
    sam.left(50)
sam.onkeypress(left,'a')
def right():
    sam.setheading(90)
    sam.right(50)
sam.onkeypress(right,'d')
sam.listen()


    
    

