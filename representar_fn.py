"""
Código para representar gráficamente función principal y cotas
"""
import numpy as np
import matplotlib.pyplot as plt

# Generar valores de n
n = np.linspace(1, 6, 100)  # Desde 1 hasta 6 con 100 puntos
y = np.log2(n)

# Constantes para las cotas
K1 = 1
K2 = 2

# Representar la función principal y las cotas
plt.plot(n, y, label="f(n) = log(n^log(17))", color='blue')
plt.plot(n, y, label="f(n) = log(17^log(n))", color='red')
plt.plot(n, K1*y, '--', label="k1 * log(n)", color='red')
plt.plot(n, K2*y, '--', label="k2 * log(n)", color='green')

# Personalizar el gráfico
plt.title("Representación gráfica de Θ(log n) para la búsqueda binaria")
plt.xlabel("n")
plt.ylabel("Tiempo de ejecución (unidades arbitrarias)")
plt.legend()
plt.grid(True)
plt.show()
