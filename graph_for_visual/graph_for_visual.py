import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("(C0.5).dat")
a1= data[:, 0]
b1= data[:, 1]

data = np.loadtxt("(C0.9).dat")
a2= data[:, 0]
b2= data[:, 1]

data = np.loadtxt("(C1.1).dat")
a3= data[:, 0]
b3= data[:, 1]

data = np.loadtxt("(results).dat")
a4= data[:, 0]
b4= data[:, 1]

data = np.loadtxt("(N80).dat")
a5= data[:, 0]
b5= data[:, 1]

data = np.loadtxt("(N320).dat")
a6= data[:, 0]
b6= data[:, 1]

data = np.loadtxt("(t0).dat")
a7= data[:, 0]
b7= data[:, 1]

data = np.loadtxt("(t0.2).dat")
a8= data[:, 0]
b8= data[:, 1]

data = np.loadtxt("(t0.4).dat")
a9= data[:, 0]
b9= data[:, 1]

data = np.loadtxt("(t0.6).dat")
a10= data[:, 0]
b10= data[:, 1]

data = np.loadtxt("(t0.8).dat")
a11= data[:, 0]
b11= data[:, 1]

fig = plt.figure()

#fig, ax = plt.subplots()

ax1 = plt.subplot2grid((3,1), (0, 0))
ax2 = plt.subplot2grid((3,1), (1, 0))
ax3 = plt.subplot2grid((3,1), (2, 0))

plt.tight_layout()

ax1.plot(a1,b1, color='r', linewidth=0.8, marker='o', markersize=2)  #зависимость от С
ax1.plot(a2,b2, color='g', linewidth=0.8, marker='o', markersize=2)
ax1.plot(a3,b3, color='b', linewidth=0.8, marker='o', markersize=2)
ax1.plot(a4,b4, color='black', linewidth=0.8)#Ua

ax1.plot(a1, b1, color='r', linewidth=0.8, label = 'c = 0.5')
ax1.plot(a2, b2, color='g', linewidth=0.8, label = 'c = 0.9')
ax1.plot(a3, b3, color='b', linewidth=0.8, label = 'c = 1.1')
ax1.plot(a4, b4, color='black', linewidth=0.8, label = 'u0')
ax1.legend(loc='upper left', prop={'size': 7}, frameon=False, ncol = 2)

ax1.set_xlim(0,1)
ax1.set_ylim(-1,2.1)

#ax1.set_xlabel('x')
ax1.set_ylabel('$U_{a}$')


ax2.plot(a5,b5, color='purple', linewidth=0.8, marker='o', markersize=2) #зависимость от N
ax2.plot(a6,b6, color='coral', linewidth=0.8, marker='o', markersize=2)
ax2.plot(a2,b2, color='g', linewidth=0.8, marker='o', markersize=2)
ax2.plot(a4,b4, color='black', linewidth=0.8) #Ua

ax2.plot(a2, b2, color='g', linewidth=0.8, label = 'N=160')
ax2.plot(a5, b5, color='purple', linewidth=0.8, label = 'N=80')
ax2.plot(a6, b6, color='coral', linewidth=0.8, label = 'N=320')
ax2.legend(loc='upper left', prop={'size': 8}, frameon=False)

ax2.set_xlim(0,1)
ax2.set_ylim(0,1)


ax2.set_xlabel('x')
ax2.set_ylabel('$U_{a}$')


ax3.plot(a7,b7, color='indianred', linewidth=0.8, marker='o', markersize=2) #зависимость от t
ax3.plot(a8,b8, color='palevioletred', linewidth=0.8, marker='o', markersize=2)
ax3.plot(a9,b9, color='coral', linewidth=0.8, marker='o', markersize=2)
ax3.plot(a11,b11, color='palegreen', linewidth=0.8, marker='o', markersize=2)

ax3.plot(a7, b7, color='indianred', linewidth=0.7, label = 't=0')
ax3.plot(a8, b8, color='palevioletred', linewidth=0.7, label = 't=0.2')
ax3.plot(a9, b9, color='coral', linewidth=0.7, label = 't=0.4')
ax3.plot(a11, b11, color='mediumseagreen', linewidth=0.7, label = 't=0.8')
ax3.legend(loc='upper left', prop={'size': 8}, frameon=False, ncol = 3)

ax3.set_xlim(0,1)
ax3.set_ylim(0,1)

ax3.set_xlabel('x')
ax3.set_ylabel('$U_{a}$')

plt.tight_layout()
plt.savefig("graph.png", dpi=500)
plt.show()

