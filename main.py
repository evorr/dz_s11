#  f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
from sympy import symbols, sin, cos
from scipy.optimize import fsolve
import numpy
import matplotlib.pyplot as plt

# Находим корни квадратного уравнения:

def f(x):
    return -12 * x ** 4 * numpy.sin(numpy.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30


funcrange = [-10, 10]
leftnum = min(funcrange)
rightnum = max(funcrange)


def solution():
    global leftnum, rightnum
    temp = leftnum
    rightnum = rightnum
    roots = []
    interval = []
    while temp < rightnum:
        if f(temp) >= 0 and f(temp + 1) <= 0:
            w = fsolve(f, temp)
            roots.append(*w)
        if f(temp) <= 0 and f(temp + 1) >= 0:
            w = fsolve(f, temp)
            roots.append(*w)
        if f(temp) > f(temp + 1) < f(temp + 2):
            interval.append(temp + 1)
        temp += 1
    roots = [round(i, 2) for i in roots]
    print(f'Корни уравнения для заданного интервала: {roots}')
    return roots


solution()


# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает

def func_interval(left, right):
    array = []
    temp = left
    while left < right:
        array.append([f(left), left])
        left += 0.1
    if array[0][0] > 0:
        print(f'f > 0 в промежутке {temp, right}')
        return max(array)
    else:
        print(f'f < 0 в промежутке {temp, right}')
        return min(array)


for i in solution():
    func_interval(i, i+1)


# Построить график
x = [x for x in range(-30, 30)]
y = [(-12 * x ** 4 * sin(cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30) for
     x in range(-30, 30)]

plt.plot(x, y)
plt.grid()
plt.show()



# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

def maxima_and_minima():
    roots = solution()

    if len(roots) < 2:
        print('На заданном интервале нет вершин')
    else:
        top = []
        for i in range(len(roots) - 1):
            top.append(func_interval(roots[i], roots[i + 1]))
        for j in top:
            j = [round(i, 2) for i in j]
            print(f'Координаты вершин функции: [{j[1]}, {j[0]}]')
        if len(top) < 2:
            print('error')
        else:
            for i in range(len(top) - 1):
                if top[i][0] > top[i + 1][0]:
                    print('Функция убывает')
                else:
                    print('Функция возрастает')


maxima_and_minima()