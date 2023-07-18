import matplotlib.pyplot as plt
from math import *



def atualizar_grafico(x, y):
    plt.cla()  # Limpa o gráfico atual
    plt.plot(x, y, 'b-')  # Plota os dados no gráfico
    plt.xlabel('x')
    plt.ylabel('y = x^2')
    plt.title('Gráfico de y = x^2')
    plt.grid(True)
    plt.pause(0.1)  # Pausa para permitir a atualização da janela do gráfico

# Configuração inicial
x = []
y = []

# Loop principal
for i in range(-101, 101):
    x.append(i)
    y.append(-sin(i)/cos(i))
    atualizar_grafico(x, y)

# Manter a janela do gráfico aberta
plt.show()
