'''
1) Reduza uma imagem de uma escala k < 1 utilizando a técnica do vizinho mais próximo
    • Bônus: faça a redução utilizando a média dos vizinhos
'''

import cv2
import numpy as np

#* Importa a imagem pra dentro do programa:
img_0 = 'Lenna.png'
img1 = cv2.imread(img_0)

#* Cria uma nova imagem de zeros (imagem "vazia"):
newimage = np.zeros((img1.shape[0],img1.shape[1],3), dtype=np.uint8)

#* Pega a escala que o usuário deseja:
define_escala = float(input("Digite a escala K que você deseja: "))

#* Calcula as novas dimensões que a imagem precisará ter e guarda em variáveis:
nova_largura = int(img1.shape[1] * define_escala)
nova_altura = int(img1.shape[0] * define_escala)

#* Redimensiona a imagem com KNN (usa uma função do próprio OpenCV):
newimage = cv2.resize(img1, (nova_largura, nova_altura), interpolation=cv2.INTER_NEAREST)

#! Ao fazer os testes com apenas esse 1º redimensionamento, percebi que a imagem mostrava na tela sempre bem "pequenininha"

#* Redimensionando de volta pro tamanho original (pra que a imagem seja mostrada na tela do mesmo tamanho que a imagem inicial):
newimage = cv2.resize(newimage, (img1.shape[1], img1.shape[0]), interpolation=cv2.INTER_NEAREST)

#* Mostrando a imagem reduzida com KNN na tela:
cv2.imshow('Resultado da imagem reduzida com KNN', newimage)
cv2.waitKey(0)

#* Redimensiona a imagem com media dos vizinhos (usa uma função do próprio OpenCV):
newimage = cv2.resize(img1, (nova_largura, nova_altura), interpolation=cv2.INTER_LINEAR)

#* Redimensionando de volta pro tamanho original (pra que a imagem seja mostrada na tela do mesmo tamanho que a imagem inicial):
newimage = cv2.resize(newimage, (img1.shape[1], img1.shape[0]), interpolation=cv2.INTER_LINEAR)

#* Mostrando a imagem reduzida com media dos vizinhos na tela:
cv2.imshow('Resultado da imagem reduzida com media dos vizinhos', newimage)
cv2.waitKey(0)