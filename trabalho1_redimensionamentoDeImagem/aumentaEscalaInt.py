import cv2
import numpy as np
import matplotlib.pyplot as plt

#* Importa a imagem pra dentro do programa:
img_0 = 'Lenna.png'
img1 = cv2.imread(img_0)

#* Pega a escala que o usuário deseja:
define_escala = int(input("Digite a escala K que você deseja: "))

#* Cria duas novas imagens de zeros (imagens "vazias"), sendo uma pra interpolação 0 e a outra pra interpolação 1:
newimage_zero = np.zeros((img1.shape[0] * define_escala, img1.shape[1] * define_escala, 3), dtype=np.uint8)
newimage_um = np.zeros((img1.shape[0] * define_escala, img1.shape[1] * define_escala, 3), dtype=np.uint8)

#* Calcula a interpolação de ordem 0:
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        newimage_zero[i * define_escala:(i + 1) * define_escala, j * define_escala:(j + 1) * define_escala] = img1[i, j]

#* Preenchendo os quadrados vazios na interpolação de ordem 0
newimage_zero = cv2.resize(newimage_zero, (img1.shape[1] * define_escala, img1.shape[0] * define_escala), interpolation=cv2.INTER_NEAREST)

#* Calcula a interpolação de ordem 1:
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        for desloc_i in range(define_escala):
            for desloc_j in range(define_escala):
                newimage_um[i * define_escala + desloc_i, j * define_escala + desloc_j] = img1[i, j] * (1 - desloc_i / define_escala) * (1 - desloc_j / define_escala)

#* Preenchendo os quadrados vazios na interpolação de ordem 1
newimage_um = cv2.resize(newimage_um, (img1.shape[1] * define_escala, img1.shape[0] * define_escala), interpolation=cv2.INTER_LINEAR)

#* Mostrando as imagens interpoladas:
#! Cria um plot
plt.figure(figsize=(12, 6))

#! Coloca a imagem original no plot 1
plt.subplot(1, 3, 1)
plt.title('Imagem Original')
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.axis('off')

#! Coloca a imagem interpolada 0 no plot 2
plt.subplot(1, 3, 2)
plt.title('Interpolação Ordem Zero')
plt.imshow(cv2.cvtColor(newimage_zero, cv2.COLOR_BGR2RGB))
plt.axis('off')

#! Coloca a imagem interpolada 1 no plot 3
plt.subplot(1, 3, 3)
plt.title('Interpolação Ordem Um')
plt.imshow(cv2.cvtColor(newimage_um, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()