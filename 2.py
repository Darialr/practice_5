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
t.circle(r)
t.penup()

t.color('red')
t.goto(x, y)
t.pendown()
t.dot()

t.penup()
t.setposition(xc - 30, yc - r - 10)
if (xc - x)**2 + (yc - y)**2 == r**2:
    t.write('точка на окружности')
elif (xc - x)**2 + (yc - y)**2 <= r**2:
    t.write('точка внутри окружности')
elif (xc - x)**2 + (yc - y)**2 >= r**2:
    t.write('точка вне окружности')

t.done()
