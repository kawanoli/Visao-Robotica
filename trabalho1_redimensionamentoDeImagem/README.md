# Aprendizados obtidos:
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
