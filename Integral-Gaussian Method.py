#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def function(x):
    return np.sin(x) ** 2 / x


def gauss_two_point(a, b):
    return ((b - a) / 2) * (function(0.5 * ((b - a) * (np.sqrt(3) / 3) + (b + a))) + function((0.5 * ((b - a) * (-np.sqrt(3) / 3) + (b + a)))))


def gauss_three_point(a, b):
    return ((b - a) / 2) * ((5 / 9) * function(0.5 * ((b - a) * (- np.sqrt(3) / np.sqrt(5)) + (b + a))) + (8 / 9) * function((0.5 * ((b - a) * (0) + (b + a)))) + (5 / 9) * function((0.5 * ((b - a) * (np.sqrt(3) / np.sqrt(5)) + (b + a)))))

difference = gauss_three_point(1, 2) - gauss_two_point(1, 2)
print(f"The difference between those is: {difference}")

print(f"The answer in Two-Point_Gaussian method is: {gauss_two_point(1, 2)}")
print(f"The answer in Three-Point_Gaussian method is: {gauss_three_point(1, 2)}")

