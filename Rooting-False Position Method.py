#!/usr/bin/env python
# coding: utf-8

# In[3]:


#False Position Method
a = 0.25
b = 0.75
eps = 0.002
n = 0
# n is number of iteration
import math
def f(x):
    return 3*x - math.exp(x)
if f(a) * f(b)> 0.0:
    print("in this limits equation has not any root")
c = (a * f(b) - b * f(a))/(f(b) - f(a))    
while eps <= abs(f(c)):
    n = n + 1
    c = (a * f(b) - b * f(a))/(f(b) - f(a))
    if f(a) * f(c) >0.0:
        a = c
    else :
        b = c
print("the root is: %0.3f" %c)
print("iteration is:" ,n)

