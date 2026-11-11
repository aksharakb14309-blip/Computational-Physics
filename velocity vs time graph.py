import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,10,11)
u=int(input("Enter the initial velocity:"))
a=int(input("Enter the acceleration:"))
v=u+a*t
plt.figure()
plt.plot(t,v)
plt.xlabel("time(s)")
plt.ylabel("velocity(m/s)")
plt.title("velocity-time graph")
plt.grid()
plt.show()

