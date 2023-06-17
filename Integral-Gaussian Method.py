#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np

def function(x):
    return ((np.sin(x) ** 2) / (x ** 2 - 2 ** x) )


def gauss_two_point(a, b):
    answer = ((b-a) / 2) * (function(0.5 * ((b - a) * (np.sqrt(3) / 3) + (b + a))) + function(0.5 * ((b - a) * (-np.sqrt(3) / 3) + (b + a))))
    return answer


def gauss_three_point(a, b):
    answer = ((b-a) / 2) * ((5 / 9) * function(0.5 * ((b - a) * (np.sqrt(3) / np.sqrt(5)) + (b + a))) + (5 / 9) * function(0.5 * ((b - a) * (-np.sqrt(3) / np.sqrt(5)) + (b + a))) + (8 / 9) * function(0))
    return answer


print(f"The answer in Two-Point_Gaussian method is: {gauss_two_point(4, 5)}")
print(f"The answer in Three-Point_Gaussian method is: {gauss_three_point(4, 5)}")

difference = gauss_three_point(4, 5) - gauss_two_point(4, 5) 

print(f"The difference between those is: {difference}")

