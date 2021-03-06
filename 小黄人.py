import turtle as t
#画布
t.setup(800,800)
#轮廓
t.speed(0)
t.fillcolor('#ffff00')
t.begin_fill()
t.goto((0,150))
t.left(90)
t.circle(150,180)
t.fd(300)
t.circle(150,180)
t.fd(300)
t.end_fill()

#眼睛
t.width(4)
t.fillcolor('white')
t.begin_fill()
t.up()
t.goto((-70,150))
t.down()
t.circle(40)
t.up()
t.goto(-150,150)
t.down()
t.circle(40)
t.end_fill()
#眼球
t.width(1)
t.fillcolor('black')
t.begin_fill()
t.up()
t.goto(-100,150)
t.down()
t.circle(20)
t.end_fill()
t.fillcolor('black')
t.begin_fill()
t.up()
t.goto(-180,150)
t.down()
t.circle(20)
t.end_fill()

t.fillcolor('white')
t.begin_fill()
t.up()
t.goto((-100,150))
t.down()
t.circle(8)
t.up()
t.goto((-180,150))
t.down()
t.circle(8)
t.end_fill()
#眼罩
t.width(17)
t.up()
t.goto(0,150)
t.down()
t.left(90)
t.fd(70)

t.up()
t.goto((-300,150))
t.down()
t.right(180)
t.fd(70)

#笑脸
t.up()
t.pencolor('red')
t.width(2)
t.goto((-200,50))
t.down()
t.right(90)
t.circle(60,180)

#裤子
t.pencolor('black')
t.fillcolor('#0B4C5F')
t.begin_fill()
t.up()
t.goto(0,-160)
t.left(90)
t.down()
t.fd(300)
t.left(90)
t.circle(150,180)
t.end_fill()

t.pencolor('#0B4C5F')
t.fillcolor('#0B4C5F')
t.begin_fill()
t.up()
t.goto(-50,-160)
t.down()
t.fd(50)
t.left(90)
t.fd(200)
t.left(90)
t.fd(50)
t.left(90)
t.fd(200)
t.end_fill()

t.pencolor('black')
t.fillcolor()
t.up()
t.goto(0,-45)
t.begin_fill()
t.right(90)
t.down()
t.fd(15)
t.right(45)
t.fd(80)
t.right(90)
t.fd(15)
t.right(90)
t.fd(98)
t.end_fill()

t.fillcolor()
t.up()
t.goto(-300,-45)
t.begin_fill()
t.right(90)
t.down()
t.fd(98)
t.right(90)
t.fd(15)
t.right(90)
t.fd(81)
t.right(45)
t.fd(18)
t.end_fill()
#肚兜
t.pencolor('black')
t.up()
t.goto(-100,-145)
t.left(90)
t.down()
t.fd(100)
t.left(90)
t.fd(50)
t.circle(50,180)
t.fd(50)
# t.up()
# t.down()
# t.write('我是小黄人',align='right',font=('微软雅黑',16,'normal'))
t.mainloop()