import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as pl

def func(x,p):
    A,k,theta = p
    return A*np.sin(2*np.pi*k*x+theta)

def residuals(p,y,x):
    return y-func(x,p)

x = np.linspace(0, -2*np.pi, 100)
A, k, theta = 10, 0.34, np.pi/6

y0 = func(x, [A, k, theta])
y1 = y0 + 2 * np.random.randn(len(x)) 
p0 = [11, 0.2, 0]
plsq = leastsq(residuals, p0, args=(y1, x))
print("真实参数:", [A, k, theta])
print("拟合参数", plsq[0])

pl.plot(x, y0, label="RealData")
pl.plot(x, y1, label="Data with noise") 
pl.plot(x, func(x, plsq[0]), label="Fitting Data") 
pl.legend()
pl.show()