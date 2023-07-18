import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'ro')

A = [[random.randint(-10000, 10000) for i in range(20)] for i in range(20)]

def calcular_media_populacao(pop):
    soma = sum(individuo for individuo in pop)
    media = soma / len(pop)
    return media

def init():
    ax.set_xlim(-10000, 10000)
    ax.set_ylim(-10000, 10000)
    return ln,

def update(frame):

    print("frame:", frame)  # Printa o valor de 'frame'
    xdata.append(frame)
    ydata.append(calcular_media_populacao(A[frame]))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=range(len(A)), init_func=init, blit=True)
plt.show()
