from turtle import *
speed('slowest')
bgcolor('pink')
pencolor('red')

pensize(3)
data = [0,105,0,-105]#list

for val in data:
    fd(val)
    lt(360/3)
    write(val)
    circle(val,180) 
hideturtle()
mainloop()