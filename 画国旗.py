import turtle as t
t.setup(675,450,700,90)
t.bgcolor("red")
t.color("yellow","yellow")
t.speed(8)
dian_mia = [(-280,100),(-100,160),(-50,110),(-40,50),(-100,10)]
dian_sth = [0,55,30,5,-30]
for i in range(5):
    t.up()
    t.goto(dian_mia[i])
    t.setheading(dian_sth[i])
    t.begin_fill()
    for m in range(5):
        t.fd(150 if i==0 else 50)
        t.right(144)
        t.down()
    t.end_fill()
t.hideturtle()
t.done()
