import numpy as np
from scipy.sparse import csr_matrix

dimensiones = (1000, 1000)
# Generar valores aleatorios enteros para las matrices dispersas
valores_matriz1 = np.random.randint(1, 10, size=dimensiones)
valores_matriz2 = np.random.randint(1, 10, size=dimensiones)

matriz_dispersa1 = csr_matrix(valores_matriz1)
matriz_dispersa2 = csr_matrix(valores_matriz2)
# print("Matriz dispersa 1:")
# print(matriz_dispersa1)
# print("\nMatriz dispersa 2:")
# print(matriz_dispersa2)
resultado_multiplicacion = matriz_dispersa1.dot(matriz_dispersa2)
print("\nResultado de la multiplicación:")
print(resultado_multiplicacion)