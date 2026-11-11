import numpy as np
import matplotlib.pyplot as plt
g=9.8
u=int(input("Enter initial velocity:"))
theta=int(input("Enter angle of projection:"))
angle=np.radians(theta)
t=0
dt=0.001
x=0
y=0
X=[x]
Y=[y]
vx=u*np.cos(angle)
vy=u*np.sin(angle)
while y>=0:
    x=x+vx*dt
    y=y+vy*dt
    vy=vy-g*dt
    if y<0:
        break
    X.append(x)
    Y.append(y)
plt.figure()
plt.plot(X,Y)
plt.xlabel("Horizontal displacement")
plt.ylabel("Vertical displacement")
plt.grid()
plt.show()
    
