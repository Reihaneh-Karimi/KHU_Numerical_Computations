#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Bisection Method
a =int(input('please enter number as First limit: '))
b =int(input('plese enter number as Second limit: '))
eps =float(input('please enter  telorance of root: '))
# n is number of iteration
n=0
c= None
import math
def f(x):
    return x + math.cos(x)
if f(a) * f(b)> 0.0:
    print("choose another a & b")
else :    
    while eps <= (b-a):
        n = n + 1
        c = (a+b)/2
        if f(a) * f(c)> 0:
            a = c
        else:
            b = c
        if n/2==0:
            print(c)
print("the root is: "+str(c))
print("iteration is: " +str(n))

