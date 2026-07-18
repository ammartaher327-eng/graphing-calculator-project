import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


x=sp.symbols('x')
while True:
    f=input('choose f(x)')
    try:
        f=sp.sympify(f,locals={"e":sp.E,"pi":sp.pi})
        break
    except sp.SympifyError:
        print("invalid")




y=sp.lambdify(x,f,'numpy')

print("your function is",f)

def plot(y):
    x_val=np.linspace(-10,10,100)
    y_val=y(x_val)
    plt.figure()
    plt.plot(x_val,y_val)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.grid(True)
    plt.show()

plot(y)

