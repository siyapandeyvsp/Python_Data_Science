from turtle import *
dis=[200,200,150,150,190,175,70,80,70,400,200,200,150,410,150,410]
ngl=[90,72,40,68,90,90,90,90,90,0,90,72,18,162,18,40]
#our home

speed('fast')
bgcolor('yellow')
pencolor('brown')
fillcolor('red')

pensize(3)
for d,a in zip(dis,ngl):
    forward(d)
    left(a)
    
   


mainloop()
