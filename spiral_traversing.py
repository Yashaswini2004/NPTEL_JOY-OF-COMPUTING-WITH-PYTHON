import turtle
turtle.bgcolor("black")
t=turtle.Turtle()
width=5
height=7
dot_distance=25
t.setpos(-250,250)
def spiral(m,n):
    l=0
    k=0
    f=0
    t.color("white")
    while(k<m and l<n):
        if(f==1):
            t.right(90)
        for i in range(l,n):
            t.forward(dot_distance)
        k+=1
        f=1
        t.right(90)
        for i in range(k,m):
            t.forward(dot_distance)
        n-=1
        t.right(90)
        if(k<m):
            for i in range(n-1,l-1,-1):
                t.forward(dot_distance)
            m-=1
        t.right(90)
        if(l<n):
            for i in range(m-1,k-1,-1):
                t.forward(dot_distance)
            l+=1
spiral(20,20)
turtle.done()