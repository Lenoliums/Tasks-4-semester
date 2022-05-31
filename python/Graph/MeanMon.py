data = np.genfromtxt("stockholm_tmp.dat", dtype=float)

Mon_Mean = [0]*12
for i in range(0, 12):
    Mon_Mean[i]=np.mean((data[data[:, 1] == i+1])[:,3])

print(Mon_Mean)

plt.bar([i for i in range(1,13)], Mon_Mean)
plt.show()