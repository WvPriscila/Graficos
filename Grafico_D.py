import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random




A = [[random.randint(-100, 100) for i in range(20)] for i in range(20)]


fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'ro')


def calcular_media_populacao(pop):
    soma = sum(individuo for individuo in pop)
    media = soma / len(pop)
    print("média: ", media)

    return media


def limites():
    ax.set_xlim(-600, 600)
    ax.set_ylim(-600, 600)
    return ln,


def Atualização(frame):
    print("frame:", frame)  # Printa o valor de 'frame'
    print(xdata)
    xdata.append(frame)
    ydata.append(calcular_media_populacao(A[frame]))
    ln.set_data(xdata, ydata)
    return ln,


ani = FuncAnimation(fig, Atualização, frames=range(len(A)), init_func=limites, blit=True)
plt.show()
