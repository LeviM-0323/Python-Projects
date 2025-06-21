'''
The Golden Ratio (sometimes referred to as the golden spiral or golden number) is a mathmatical constant derived from the formula
(1 + √5) / 2 and equal to approximately 1.61803398875. It is often referred to as phi using the greek symbol Φ. The golden ratio 
is related to the Fibonacci sequence as when plotting squares with lenghts equal to that of the fibonacci sequence numbers (eg. 1,1,2,3,5,8...) 
the ratio of the length to width of the outermost rectangle is equal to phi. The squares also form in such a way that a 90-degree arc
can evenly be drawn through all the squares infinitely outward. The code below is not my creation for the most part, it is taken from 
https://github.com/Pirraio/Golden-Spiral with only minor alterations and they should be given the credit. I just wished to analyze and 
understand this code to further investigate the mathmatical phenomenon as I am deeply interested.
'''

import turtle as t
from math import sqrt

phi = (1 + sqrt(5)) / 2 # Actual Golden ratio (aka. 1.618...)
width = 350
height = phi * width
altura = width

t.title('Golden Spiral Visualization')
t.speed(5)
t.color('black', 'white')
t.width(3)
t.penup()
t.setpos((phi*-width)/2, -width/2)
t.pendown()

for i in range(2):
    t.forward(height)
    t.left(90)
    t.forward(altura)
    t.left(90)

t.forward(altura)
t.left(90)

novoLado = altura
for j in range(10):
    t.forward(novoLado)
    t.backward(((height-altura)**(j+1))/width**j)
    t.right(90)
    novoLado = ((height-altura)**(j+1))/width**j

t.penup()
t.setpos((phi*-width)/2, -width/2)
t.pendown()
t.setheading(90)

arco_90 = altura
for k in range(10):
    t.circle(-arco_90, 90)
    arco_90 = ((height-altura)**(k+1))//width**k

t.hideturtle()
t.mainloop()