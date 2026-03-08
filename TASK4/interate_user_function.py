#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, tan, exp, pi
from scipy.integrate import quad

function = input(f"Input a function: ")
a = float(input(f"Input the lower bound a: "))
b = float(eval(input(f"Input the upper bound b: ")))
N = 10000
try:
    f = lambda x: eval(function)
    result =quad(f, a, b)[0]
    print(f"The quad integration gives: {result}")
except NameError as e:
        print(f"Unknown function or variable in expression: {e}")
except SyntaxError:
    print("Syntax error in the expression")
except Exception as e:
    print(f"An error occurried during quad integration: {e}")

try:
    f = lambda x: eval(function)
    x = np.random.uniform(a, b, 10000)
    y = f(x)
    integral = (b-a)/N * np.sum(y)
    print(f"Monte Carlo integration gives: {integral}")
except NameError as e:
        print(f"Unknown function or variable in expression: {e}")
except SyntaxError:
    print("Syntax error in the expression")
except Exception as e:
    print(f"An error occurried during Monte Carlo integration: {e}")

