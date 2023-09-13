from turtle import *
dis=[100,200,150,150,190,150,70,20,70,500]
ngl=[90,72,40,68,90,90,90,90,90,90]
#our home

speed('slow')
bgcolor('yellow')
pencolor('brown')

pensize(3)
for d,a in zip(dis,ngl):
    fd(d)
    if a<0:
        rt(abs(a))
    else:
        lt(a)    

hideturtle()
mainloop()