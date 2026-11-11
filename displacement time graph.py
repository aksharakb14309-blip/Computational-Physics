import numpy as np
import matplotlib.pyplot as plt
u=int(input("Enter initial velocity:"))
a=int(input("Enter acceleration:"))
t=np.linspace(0,100,101)
s=u*t+0.5*a*t**2
plt.figure()
plt.plot(t,s)
plt.xlabel("time(s)")
plt.ylabel("displacement(m)")
plt.title("displacement-time graph")
plt.grid()
plt.show()
