#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Newton-Refeson Method
import sympy as sp

x = sp.symbols("x")
eps = float(input("how accurate?\n"))
x_i = float(input("give me a random x\n"))

def f(x):
    return 3*sp.exp(x)-(1/x)
m = sp.diff(f(x),x)

while True:
    x_new = ((-f(x_i))/(m.subs(x,x_i)))+x_i
    if abs(f(x_new))<=eps:
        print(f"root is {x_new}")
        break
    else:
        x_i = x_new

