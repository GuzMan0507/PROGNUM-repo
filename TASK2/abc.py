#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
a= float(input("Value of a:"))
b=float(input("Value of b:"))
c=float(input("Value of c:"))
D= (b**2)- (4*a*c)

if D>0:
    x1=(-b + math.sqrt(D)) / (2*a)
    x2=(-b - math.sqrt(D)) / (2*a)
    print(f"The equation has two solutions: x1= {x1} and x2= {x2}")
elif D==0:
    x= -b /(2*a)
    print(f"The equation has one solution: x= {x}")
else:
    print(f" The equation has no real solutions")

