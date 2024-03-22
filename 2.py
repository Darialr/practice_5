import turtle as t

xc = int(input('Введите координату центра окружности по оси X: '))
yc = int(input('Введите координату центра окружности по оси Y: '))
r = int(input('Введите радиус окружности: '))
x = int(input('Введите координату точки по оси X: '))
y = int(input('Введите координату точки по оси Y: '))

t.color('black')
t.penup()
t.setposition(xc, yc)
t.forward(r)
t.left(90)
t.pendown()
t.circle(200)
t.penup()

t.color('red')
t.goto(x,y)
t.pendown()
t.dot()

if

t.done()
