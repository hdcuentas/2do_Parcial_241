import numpy as np
from scipy.sparse import csr_matrix
from multiprocessing import Pool, cpu_count

# Función para multiplicar una fila por la segunda matriz dispersa
def multiplicar_fila(args):
    fila, matriz_b = args
    return fila.dot(matriz_b).toarray().ravel()

# Dimensiones de las matrices dispersas
dimensiones = (1000, 1000)
valores_matriz1 = np.random.randint(1, 10, size=dimensiones)
valores_matriz2 = np.random.randint(1, 10, size=dimensiones)
matriz_dispersa1 = csr_matrix(valores_matriz1)
matriz_dispersa2 = csr_matrix(valores_matriz2)

# Argumentos para el pool de procesos
argumentos = [
    (matriz_dispersa1.getrow(i), matriz_dispersa2)
    for i in range(matriz_dispersa1.shape[0])
]
# Crear un pool de procesos y realizar la multiplicación en paralelo
with Pool(cpu_count()) as pool:
    resultado_paralelo = pool.map(multiplicar_fila, argumentos)
# Convertir la lista de resultados a una matriz dispersa
resultado_multiplicacion = csr_matrix(np.vstack(resultado_paralelo))
print("\nResultado de la multiplicación paralela:")
print(resultado_multiplicacion)