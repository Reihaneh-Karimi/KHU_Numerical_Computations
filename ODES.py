#!/usr/bin/env python
# coding: utf-8

# In[1]:


def main():
    def y_prime(x, y, p):
        return p
    
    def p_prime(x, y, p):
        return -y + 0.1 * (1 - y ** 2) * p
    
    def runge_kutta(x_0, y_0, p_0, x, h):
        n = int((x - x_0) / h)
        y = y_0
        p = p_0

        for num in range(1, n + 1):
            k_1 = h * y_prime(x_0, y, p)
            l_1 = h * p_prime(x_0, y, p)
            k_2 = h * y_prime(x_0 + 0.5 * h, y + k_1 / 2, p + l_1 / 2)
            l_2 = h * p_prime(x_0 + 0.5 * h, y + k_1 / 2, p + l_1 / 2)
            k_3 = h * y_prime(x_0 + 0.5 * h, y + k_2 / 2, p + l_2 / 2)
            l_3 = h * p_prime(x_0 + 0.5 * h, y + k_2 / 2, p + l_2 / 2)
            k_4 = h * y_prime(x_0 + h, y + k_3, p + l_3)
            l_4 = h * p_prime(x_0 + h, y + k_3, p + l_3)

            y = y + (1 / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
            p = p + (1 / 6) * (l_1 + 2 * l_2 + 2 * l_3 + l_4)
            x_0 += h

        return y, p
    

    print(f"The values will be: {runge_kutta(0, 1, 0, 0.2, 0.2)}")



if __name__ == "__main__":
    main()
    


# In[ ]:




