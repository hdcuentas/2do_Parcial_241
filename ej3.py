import cv2
import numpy as np
from matplotlib import pyplot as plt
# Leer las imágenes
imagen1 = cv2.imread('parte1.jpg')
imagen2 = cv2.imread('parte2.jpg')

if imagen1.shape != imagen2.shape:
    imagen2 = cv2.resize(imagen2, (imagen1.shape[1], imagen1.shape[0]))

suma = cv2.addWeighted(imagen1, 0.5, imagen2, 0.5, 0)
resta = cv2.subtract(cv2.add(imagen1, imagen2), imagen1)
# Suma
plt.subplot(1, 2, 1)
plt.imshow(suma)
plt.title('Suma')
# plt.axis('off')

# Resta
plt.subplot(1, 2, 2)
plt.imshow(resta)
plt.title('Resta')
# plt.axis('off')

plt.show()