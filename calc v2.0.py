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
    m=sp.sympify(input('min x'),locals={"e":sp.E,"pi":sp.pi})
    M=sp.sympify(input("max x"),locals={"e":sp.E,"pi":sp.pi})
    pt=int(input("points"))
    x_val=np.linspace(float(m),float(M),pt)
    y_val=y(x_val)
    plt.figure()
    plt.plot(x_val,y_val)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.grid(True)
    plt.axis('equal')
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.show()

plot(y)

