
import matplotlib.pyplot as plt
from   math              import *



def atualizar_grafico(x, y):
    plt.cla()  # Limpa o gráfico atual
    plt.scatter(x, y, color='#FF69B4')  # Plota os pontos no gráfico
    plt.xlabel('Geração')
    plt.ylabel('Média da população')
    plt.title('Alg. Genético')
    plt.grid(True)
    plt.pause(0.1)  # Pausa para permitir a atualização da janela do gráfico

# Configuração inicial
x = []
y = []

# Loop principal
for i in range(-2, 26):
    x.append(i)
    y.append( (sin(i ** i)-cos(i**i))**2 )
    atualizar_grafico(x, y)

# Manter a janela do gráfico aberta
plt.show()

