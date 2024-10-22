# Trabalho 1 de Visão Robótica - Redimensionamento de imagens

## Aprendizados obtidos:
Além de treinar a criação de uma imagem em branco, e o recebimento de uma imagem com o imread,
eu aprendi algumas nuances da linguagem que eu não havia prestado atenção até então.
Percebi que assim como no JS, você precisa converter o tipo de dado recebido de um input do
usuário (o que me deu uma dor de cabeça inicial quando eu tentei fazer tudo sem a mínima pesquisa 
pro trabalho). Percebi também que a imagem final ficava sempre bem pequenininha inicialmente, então
pensei: "o que será que acontece se eu jogar denovo pro tamanho inicial?"; inicialmente eu pensei 
que ia cagar tudo os pixels, mas surpreendentemente funcionou da forma na qual planejei.

Acima de tudo, aprendi também enquanto pesquisava como fazer o **KNN**, que a **OpenCV** tem funções
próprias pra realizar esses redimensionamentos, o que evitou muita quebra de cabeça minha pra
redimensionar; ao tentar fazer o bônus, descobri também a função pra fazer a média dos vizinhos.
Neste trabalho, testei o **INTER_NEAREST** e o **INTER_LINEAR**, mas pesquisando apenas por cima na 
documentação da **OpenCV**, descobri que aparentemente existem outros métodos também, a qual não
fui a fundo pra saber quais são e como funcionam até o momento.

## Assuntos aprendidos nesse trabalho:
### Vizinho mais próximo (interpolação de ordem zero):
   - Para cada pixel na imagem destino. d, devemos procurar qual o pixel p da imagem
    original que irá dar a cor do pixel na imagem destino (d = p)

    Documentação sobre KNN da OpenCV:
    https://docs.opencv.org/4.x/d5/d26/tutorial_py_knn_understanding.html

### Interpolação:
   - Para cada pixel na imagem destino, o pixel correspondente na imagem original,
    juntamente com seus vizinhos, irão determinar a cor do pixel da imagem destino
   - No exemplo mais simples, podemos simplesmente fazer a média de p e seus
    vizinhos *d = media(p + N8(*p*))*
   - Obs: a média pode ser ponderada, dando mais peso a p ou de acordo com a
    proximidade de cada vizinho do ponto p (sem arredondar pra inteiro)

---

- O Código de kNearestNeighbour está totalmente funcional, assim como o de aumentaEscalaInt.
- O código pra aumentar escala do tipo float ainda não está 100% funcional; ainda deixa alguns buracos vazios.

---

## Aumento de escala de imagem com K nearest neighbour e vizinho mais próximo:
> arquivo kNearestNeighbour.py

### Descrição do Código:
Aqui, eu estou mixando no mesmo código tanto a redução com KNN tanto a redução com média dos vizinhos.

Esse código tem como objetivo reduzir uma imagem utilizando duas técnicas de redimensionamento: o vizinho mais próximo (KNN) e a média dos vizinhos.


| ![image](https://github.com/user-attachments/assets/4bdf2461-4cd5-42b6-95d4-c747c74fab41) | ![image](https://github.com/user-attachments/assets/32a41557-ff17-41ec-9429-6b69ebb454c3) |
|:--:|:--:|
> Imagens reduzida para 0.1


### Como funciona o código?

1. **Importação de bibliotecas e carregamento da imagem**:
   - O código utiliza as bibliotecas `cv2` (OpenCV) para manipulação de imagens e `numpy` para operações numéricas.
   - A imagem "Lenna.png" é lida e armazenada na variável `img1`.
   - Uma nova imagem vazia, `newimage`, é criada com as mesmas dimensões da imagem original, utilizando zeros como pixel inicial.

2. **Definição da escala**:
   - O usuário é solicitado a inserir um valor de escala `k`, que deve ser menor que 1 para reduzir a imagem.
   - As novas dimensões da imagem são calculadas multiplicando a largura e a altura originais pelo fator de escala.

3. **Redimensionamento com KNN**:
   - A imagem é redimensionada para as novas dimensões usando a função própria do OpenCV para interpolação por vizinho mais próximo (`cv2.INTER_NEAREST`).
   - Em seguida, a imagem reduzida é redimensionada de volta ao tamanho original para exibição.
   - A imagem reduzida pela técnica KNN é exibida em uma janela.

4. **Redimensionamento com Média dos Vizinhos**:
   - A imagem original é redimensionada novamente para as novas dimensões, sobrescrevendo a newimage com uma nova newimage gerada da mesma forma que a primeira, mas agora utilizando a interpolação linear (`cv2.INTER_LINEAR`), que calcula a média dos valores dos pixels vizinhos.
   - Novamente, a imagem é redimensionada de volta ao tamanho original para exibição.
   - A imagem reduzida pela média dos vizinhos é exibida em uma nova janela.

### Considerações
- Tentei fazer ambas as reduções no mesmo código, de forma a deixar o trabalho com menos arquivos .py
- Ao fazer os testes com apenas esse 1º redimensionamento, percebi que a imagem mostrava na tela sempre bem "pequenininha"; devido a isso, decidi sempre redimensionar de volta pro tamanho original pra facilitar a visualização da imagem.
- Acima de tudo, aprendi também enquanto pesquisava como fazer o KNN, que a OpenCV tem funções próprias pra realizar esses redimensionamentos, o que evitou muita quebra de cabeça minha pra redimensionar; ao tentar fazer o bônus, descobri também a função pra fazer a média dos vizinhos.

## Aumento de escala de imagem com K nearest neighbour e vizinho mais próximo:

### Considerações iniciais:
- Percebi inicialmente que se usasse só as funções prontas do OpenCV, eu não iria obter o resultado que gostaria.
- A primeira execução do programa, estava me retornando o aumento da forma certa, porém sem preencher os quadrados, então precisei pensar em uma forma de completar o código.
- Decidi então complementar o que faltava no código com as funções nativas do OpenCV

![image](https://github.com/user-attachments/assets/6a0fe06b-4d32-4567-973c-f0a44ff4ab96)
> Primeira versão e execução do código; o mesmo, não preenchia todo o espaço criado, gerando essa sensação de imagem escurecida

### Como funciona o código?

1. Importação de bibliotecas e carregamento da imagem
- **cv2**: Biblioteca OpenCV, utilizada para operações de processamento de imagem.
- **numpy**: Biblioteca para manipulação de arrays multidimensionais.
- **matplotlib.pyplot**: Biblioteca para criação de gráficos e visualização de dados.
- A variável img_0 contém o caminho da imagem que será carregada.
- cv2.imread carrega a imagem e armazena em img1. A imagem é representada como um array NumPy.

2. Definição da escala de interpolação
- O usuário insere um fator de escala, que determinará o quanto a imagem será ampliada.
- Duas novas imagens vazias são criadas com dimensões aumentadas, utilizando np.zeros. Ambas as imagens têm 3 canais (RGB) e são inicializadas com zeros (preto).

### 5. Interpolação de Ordem Zero (Interpolação por KNN)
- Um loop percorre cada pixel da imagem original. Para cada pixel, um bloco de pixels correspondente na nova imagem (newimage_zero) é preenchido com o valor do pixel original.

### 6. Preenchimento e redimensionamento da imagem interpolada de Ordem 0
- O `cv2.resize` é utilizado para garantir que a nova imagem tenha as dimensões corretas, utilizando a interpolação de vizinho mais próximo (KNN).

### 7. Interpolação de Ordem 1 (interpolação bilinear)
- Este bloco utiliza dois loops aninhados para interpolar os pixels. Para cada pixel na imagem original, cada pixel do bloco correspondente na nova imagem é calculado usando uma combinação dos valores dos pixels adjacentes, resultando em uma transição mais suave.

### 8. Preenchimento e redimensionamento da imagem interpolada de ordem 1
- A função cv2.resize é usada novamente, mas desta vez com a interpolação linear, que proporciona uma suavidade maior na transição entre os pixels.

### 9. Visualização das imagens
- Utilizando Matplotlib, o código cria uma figura com três subplots: a imagem original, a imagem interpolada de ordem zero e a imagem interpolada de ordem um.
- As imagens são convertidas do formato BGR (utilizado pelo OpenCV) para RGB (utilizado pelo Matplotlib) para correta exibição.

![image](https://github.com/user-attachments/assets/363196b8-b6eb-4572-ba8e-7dd6a1e9891f)
> Perceba, que a interpolação de ordem 1, ainda deixou a imagem um pouco escurecida, devido à escolha de qual seria o pixel representativo

### Considerações Finais
- Desta forma, consegui solucionar o problema que faltava, que era "pintar" os quadrados que sobravam.
- Sendo assim, consegui também refatorar o código para fazer o aumento, só que com uma escala float.
- O código está redundante de forma que ele funciona com K=2 e quaisquer K inteiro.
