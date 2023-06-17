#!/usr/bin/env python
# coding: utf-8

# In[9]:


#numerical integration by newton-cotes method by 4 point
from math import sqrt


def newt_int(f, a, b):

    h = (b - a) / 3
    res = (3*h/8) * (f(a + 0*h) + 3*f(a + 1*h) \
                     + 3*f(a + 2*h) + f(a + 3*h))
    return res


def f(x):
    return (x**2)*(math.exp(x))

a, b = 2, 3

print(newt_int(f, a, b))

