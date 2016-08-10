# -*- coding: utf-8 -*-
import math

def quadratic(a,b,c):
    delta = pow(b, 2) - 4*a*c
    if delta < 0:
        TypeError('no one result!')
    else:
        #x1 = (-b+math.sqrt(delta))/(4*a)
        #x2 = (-b-math.sqrt(delta))/(4*a)
        #return x1,x1
        return (-b+math.sqrt(delta))/(4*a),(-b-math.sqrt(delta))/(4*a)


while 1:
    a = float(input('请输入 a:'))
    b = float(input('请输入 b:'))
    c = float(input('请输入 c:'))
    print(quadratic(a,b,c))
