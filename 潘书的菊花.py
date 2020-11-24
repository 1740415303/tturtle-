#向前100px 画笔旋转90° 再向前100px，形成第二条边， 4次形成一个正方形
import turtle as t
t.speed(10)
t.pencolor('red')
t.fillcolor('yellow')
t.begin_fill()
for i in range(36):
    for j in range(4):
        t.fd(100)
        t.left(90)
    t.right(10)
t.end_fill()
t.mainloop()