import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-15, 15, 100)
y1 = np.arctan(-0.0012*(x**3) + 0.4*x*x+ 0.616*x + 6120) + 0.65*np.sin(0.24*x + 1.23) - 0.27*np.cos(0.21*x - 0.17) - (np.sin(0.34*x + 0.16))/(1 + 0.03*(x - 370.5)*(x - 370.5))


fig, ax = plt.subplots()
ax.plot(x, y1, color="blue", label="Temperature(t)")
ax.set_xlabel("t")
ax.set_ylabel("Temperature")
ax.grid()
ax.legend()

plt.show()
