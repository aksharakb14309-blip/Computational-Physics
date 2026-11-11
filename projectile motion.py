import numpy as np
import matplotlib.pyplot as plt
u=int(input("Enter initial velocity:"))
g=9.8
theta=int(input("Enter angle:"))
angle=np.radians(theta)
t=np.linspace(0,1.4428,100)
sy=u*t*np.sin(angle)-0.5*g*t**2
sx=u*t*np.cos(angle)
plt.figure()
plt.plot(sx,sy)
plt.xlabel("Horizontal displacement")
plt.ylabel("Vertical displacement")
plt.title("Projectile motion")
plt.grid()
plt.show()
