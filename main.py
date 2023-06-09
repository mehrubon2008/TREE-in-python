''' @avtor --NABIEVMEHRUBON--'''
import turtle
turtle.bgcolor('blueviolet')
from turtle import Turtle, mainloop
from time import perf_counter as clock

def tree(plist, l, a, f):
    if l > 3:
        lst = []
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        for x in tree(lst, l*f, a, f):
            yield None
def maketree():
    p = Turtle()
    p.pensize(10)
    p.setundobuffer(None)
    p.hideturtle()
    p.speed(0)
    p.getscreen().tracer(30,0)
    p.left(90)
    p.penup()
    p.forward(-210)
    p.pendown()
    t = tree([p], 200, 65, 0.6375)
    for x in t:
        pass
def main():
    a=clock()
    maketree()
    b=clock()
    return "done: %.2f sec." % (b-a)
if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()
