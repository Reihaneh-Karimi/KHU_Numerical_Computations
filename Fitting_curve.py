#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math as m
import sympy as sp
chart=pd.read_excel('data.xlsx') ## Reihaneh you have to make an excel like I created for you
print(chart)
A=len(chart['x'])
B=sum(chart['x'])
C=sum(chart['x']**2)
D=sum(chart['y'])
E=sum(chart['x']**3)
F=sum(chart['x']*chart['y'])
G=sum(chart['x']**4)
H=sum(chart['x']**2*chart['y'])
M1=np.array([[A,B,C],
            [B,C,F],
            [C,E,G]])
M2=np.array([D,F,H])
acofficents=(np.linalg.solve(M1,M2))
print(acofficents)
a0=acofficents[0]
a1=acofficents[1]
a2=acofficents[2]
x=sp.symbols('x')
def fitt(x):
    y=a2*x**2+a1*x+a0 
    return y
Z=[]
P=[]
J=[]
X=np.append(Z,chart['x'])
Y=np.append(P,chart['y'])
    
for i in X:
    Z.append(fitt(i))
    
N=(np.subtract(Z,Y))
def g(x):
    return x**2
for i in N:
   J.append(g(i))
   
K=m.sqrt(sum(J))

plt.show()
plt.subplot(1,2,1)
plt.scatter(X,Y,color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('points')
plt.subplot(1,2,2)
plt.plot(X,Z,color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fitting curve')

print('curve equation is:(y= %0.2f x**2 + %0.2f x + %0.2f)'%(a2,a1,a0))
print('Ksquare is: %0.2f'%K)


# In[ ]:




