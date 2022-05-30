import matplotlib.pyplot as plt
import numpy as np
def temperature(x):
	y1 = np.arctan(-0.0012 * (x ** 3) + 0.4 * x * x + 0.616 * x + 6120) + 0.65 * np.sin(0.24 * x + 1.23) - 0.27 * np.cos(0.21 * x - 0.17) - (np.sin(0.34 * x + 0.16)) / (1 + 0.03 * (x - 370.5) * (x - 370.5))
	return(y1)

x = np.linspace(0, 2000, 1000)
a = 0
b = 2020
while ((b-a) >= 0.0001):
    mid = (a + b) / 2
    if (temperature(mid) == 0.0):
        break
    else:
	    if temperature(a) * temperature(mid) < 0.0:
		    b = mid
	    elif temperature(b) * temperature(mid) < 0.0:
		    a = mid
print(mid)
fig, ax = plt.subplots()
ax.plot(x, temperature(x), color="blue")

plt.title("Average Earth Temperature")
plt.plot(mid, 0, 'ro')
ax.set_xlabel("years")
ax.set_ylabel("Temperature")
ax.grid()

plt.show()

