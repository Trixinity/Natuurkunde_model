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

while t > 0:
    continue
    
vx = v*cos(hoek)
vy = v*sin(hoek) 

vxv = vx/v
vyv = vy/v

Fz = -m*g

v = sqrt(vx**2+vy**2)

Fw = k*v**2 
Fwx = -Fw*vxv
Fwy = -Fw*vyv

Ek = 0.5*m*v**2
Ez = m*g*x
Emech = Ek + Ez

W = Fw*v*dt
E = Emech - W

Fx = Fwx
Fy = Fz + Fwy

x = x + vx*dt
y = y + vy*dt

t = t + dt


df = pd.DataFrame({'x1':list1, 'y1': list2})
ax = df.plot(x='x1', y='y1', label='nvt')
plt.show()