import matplotlib
import matplotlib.pyplot as plt
import numpy as np
cos = np.cos
sin = np.sin
sqrt = np.sqrt

# Variablen bij start
m = 0.026
g = 9.81
k = 0.15
hoek = 20
x = 0
y = 0.300
vx = 0
vy = 0
Cr = 0.010
alpha = np.deg2rad(hoek)

# Tijdinstellingen
t = 0
dt = 0.01

# Tabellen/lists
xlist = []
ylist = []
vxlist = []
vylist = []
axlist = []
aylist = []
tlist = []

while vx >= 0:
	if y >= 0:
		Fz = m*g
		Fn = Fz*cos(alpha)
		
		# Snelheid
		v = sqrt(vx**2+vy**2)
		vx = v*cos(alpha)
		vy = v*sin(alpha)
		
		# Luchtweerstand
		Fl = k*v**2
		Flx = Fl*cos(alpha)
		Fly = Fl*sin(alpha)
		
		# Rolweerstand
		Fwr = Cr*Fn
		Fwrx = Fwr*cos(alpha)
		Fwry = Fwr*sin(alpha)
		
		# Resultante kracht
		Fres = Fz*sin(alpha)
		Fresx = Fres*cos(alpha)-Flx-Fwrx
		Fresy = -Fres*sin(alpha)+Fly+Fwry
		
		# Versnelling
		ax = Fresx/m
		ay = Fresy/m
		
	elif y <= 0:
		# Beredeneringen
		vy = 0
		Fn = Fz
		v = vx
		v = 0
		
		# Weerstanden
		Fl = k*v**2
		Fr = Fz*Cr
		Fres = -Fl-Fr
		
		# Versnelling
		ax = Fres/m
		ay = Fresy/m
		
# Energie en Arbeid
	Ek = 0.5*m*v**2
	Ez = m*g*x
	Emech = Ek + Ez
	W = Fl*v*dt
	E = Emech - W

# Nieuwe waardes
	vx += ax*dt
	vy += ay*dt
	x += vx*dt
	y -= vy*dt
	t += dt
	
# Lijst van waardes
	axlist.append(float(ax))
	aylist.append(float(ay))
	vxlist.append(float(vx))
	vylist.append(float(vy))
	xlist.append(float(x))
	ylist.append(float(y))
	tlist.append(float(t))

# Grafieken
plt.plot(tlist,ylist,"r")
plt.xlabel("t")
plt.ylabel("y")
plt.show()
plt.plot(tlist,xlist,"b")
plt.xlabel("t")
plt.ylabel("x")
plt.show()
plt.plot(tlist,vxlist,"g")
plt.xlabel("t")
plt.ylabel("vx")
plt.show()
plt.plot(tlist,vylist,"g")
plt.xlabel("t")
plt.ylabel("vy")
plt.show()
plt.plot(tlist,axlist,"r")
plt.xlabel("t")
plt.ylabel("ax")
plt.show()
plt.plot(tlist,aylist,"b")
plt.xlabel("t")
plt.ylabel("ay")
plt.show()