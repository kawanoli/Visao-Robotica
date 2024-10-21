'''
Bônus 3: Aumente de uma escala k ≥ 1 real utilizando interpolação de ordem 1
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

#* Importa a imagem pra dentro do programa:
img_0 = 'Lenna.png'
img1 = cv2.imread(img_0)

#* Pega a escala que o usuário deseja:
define_escala = float(input("Digite a escala K que você deseja (por exemplo, 1.5 para 150%): "))

#* Cria duas novas imagens de zeros (imagens "vazias"), sendo uma pra interpoação 0 e a outra pra interpolação 1:
newimage_zero = np.zeros((int(img1.shape[0] * define_escala), int(img1.shape[1] * define_escala), 3), dtype=np.uint8)
newimage_um = np.zeros((int(img1.shape[0] * define_escala), int(img1.shape[1] * define_escala), 3), dtype=np.uint8)

#* Calcula a interpolação de ordem 0:
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        newimage_zero[int(i * define_escala), int(j * define_escala)] = img1[i, j]

#* Calcula a interpolação de ordem 1:
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        for desloc_i in range(int(define_escala)):
            for desloc_j in range(int(define_escala)):
                #! Calcular as posições interpoladas
                new_i = int(i * define_escala + desloc_i)
                new_j = int(j * define_escala + desloc_j)

                #! Atribui o valor interpolado
                newimage_um[new_i, new_j] = img1[i, j] * (1 - (desloc_i / define_escala)) * (1 - (desloc_j / define_escala))

#* Mostrando as imagens interpoladas
plt.figure(figsize=(12, 6))

#* Coloca a imagem original no plot 1
plt.subplot(1, 3, 1)
plt.title('Imagem Original')
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.axis('off')

#* Coloca a imagem interpolada 0 no plot 2
plt.subplot(1, 3, 2)
plt.title('Interpolação Ordem Zero')
plt.imshow(cv2.cvtColor(newimage_zero, cv2.COLOR_BGR2RGB))
plt.axis('off')

#* Coloca a imagem interpolada 1 no plot 3
plt.subplot(1, 3, 3)
plt.title('Interpolação Ordem Um')
plt.imshow(cv2.cvtColor(newimage_um, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
