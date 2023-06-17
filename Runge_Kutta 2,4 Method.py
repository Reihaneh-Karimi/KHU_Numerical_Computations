#!/usr/bin/env python
# coding: utf-8

# In[4]:


#runge_kutta_second-runge_kutta_fourth
def main():
    def dxdy(x, y):
        return x + y


    def runge_kutta_second(x_0, y_0, x, h):
        n = int((x - x_0) / h)
        y = y_0

        for num in range(1, n + 1):
            k_1 = h * dxdy(x_0, y)
            k_2 = h * dxdy(x_0 + h, y + k_1)

            y = y + (0.5) * (k_1 + k_2)
            x_0 += h

        return y


    def runge_kutta_fourth(x_0, y_0, x, h):
        n = int((x - x_0) / h)
        y = y_0

        for num in range(1, n + 1):
            k_1 = h * dxdy(x_0, y)
            k_2 = h * dxdy(x_0 + 0.5 * h, y + k_1 / 2 )
            k_3 = h * dxdy(x_0 + 0.5 * h, y + k_2 / 2 )
            k_4 = h * dxdy(x_0 + h, y + k_3)

            y = y + (1 / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
            x_0 += h

        return y


    print(f'The value will be 4th: {runge_kutta_fourth(0, 1, 0.1, 0.1)}')
    print(f'The value will be 2th: {runge_kutta_second(0, 1, 0.1, 0.1)}')



if __name__ == "__main__":
    main()
    

