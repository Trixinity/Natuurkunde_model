import math
cos = math.cos
sin = math.sin
sqrt = math.sqrt

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

list1 = [0]
list2 = [0]

m = 0.026
g = 9.81
k = 0.05
hoek = 20
v = 0.01

x = 0
y = 0.259

t = 0
dt = 0.01

vx = v*cos(hoek)

while vx >= 0:
    if y >= 0:
       vx = v*cos(hoek)
       vy = v*sin(hoek) 

       vxv = vx/v
       vyv = vy/v

       Fz = -m*g

       v = sqrt(vx**2+vy**2)

       Fl = k*v**2 
       Flx = -Fl*vxv
       Fly = -Fl*vyv

       Fx = Flx
       Fy = Fz

       ax = Fx/m
       ay = Fy/m

       x = x + vx*dt
       y = y + vy*dt

       Ek = 0.5*m*v**2
       Ez = m*g*x
       Emech = Ek + Ez

       W = Fl*v*dt
       E = Emech - W

       t = t + dt

    else:
       Fy = 0
           
list.append

df = pd.DataFrame({'x1':list1, 'y1': list2})
ax = df.plot(x='x1', y='y1', label='nvt')
plt.show()