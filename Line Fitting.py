#fitting by ka square (liner fitting)
import numpy as np
import math as m
x =[1,3,4,6,8,9,11,14]
y =[1,2,4,4,5,7,8,9]
z = [1,9,16,36,64,81,121,196]
xy = [1,6,16,24,40,63,88,126]
a=sum(x)
b=sum(y)
c=sum(z)
d=sum(xy)
m=len(x)
a1=(d - (a*b))/((m*c)-(a**2))
a0=((b*c)-(a*d))/((m*c)-(a**2))
print(f" the function of fitting is: y={a1}*x +{a0}")


