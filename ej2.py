import cv2
import numpy as np
from scipy.sparse import csr_matrix
from matplotlib import pyplot as plt
# Leer las imágenes en escala de grises
imagen1 = cv2.imread('parte1.jpg', 0)
imagen2 = cv2.imread('parte2.jpg', 0)
# Asegurarse de que ambas imágenes tengan el mismo tamaño, si no, redimensionarlas
if imagen1.shape != imagen2.shape:
    imagen2 = cv2.resize(imagen2, (imagen1.shape[1], imagen1.shape[0]))
# Combinar las imágenes en una sola matriz
mezcla = cv2.addWeighted(imagen1, 0.5, imagen2, 0.5, 0);
# Convertir la matriz combinada en una matriz dispersa
sparse_matrix_combinada = csr_matrix(mezcla)
# Mostrar la estructura de la matriz dispersa combinada
print("Matriz Dispersa Combinada:")
print(sparse_matrix_combinada)
plt.show()