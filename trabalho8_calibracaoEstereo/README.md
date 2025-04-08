# TRABALHO 8: Calibração Estéreo
### Aluno: Kawan Oliveira

# Calibração de Par Estéreo

Este projeto implementa um programa para calibrar um par de câmeras estéreo, utilizando parâmetros intrínsecos previamente calibrados e um conjunto de imagens das câmeras esquerda e direita. O programa tem como objetivo exibir os parâmetros extrínsecos (rotação e translação) entre as câmeras, bem como uma imagem contendo as linhas epipolares.

## Pré-requisitos

*   Um arquivo YAML contendo os parâmetros intrínsecos de cada câmera. Neste caso daqui:

    ```yaml
    %YAML:1.0
    M1: !!opencv-matrix
       rows: 3
       cols: 3
       dt: d
       data: [ 5.3480326845051309e+02, 0., 3.3568643204394891e+02, 0.,
           5.3480326845051309e+02, 2.4066183054066337e+02, 0., 0., 1. ]
    D1: !!opencv-matrix
       rows: 1
       cols: 5
       dt: d
       data: [ 2.9589439552724328e-01, -1.0354662043042675e+00, 0., 0., 0. ]
    M2: !!opencv-matrix
       rows: 3
       cols: 3
       dt: d
       data: [ 5.3480326845051309e+02, 0., 3.3455744527912015e+02, 0.,
           5.3480326845051309e+02, 2.4205324573376600e+02, 0., 0., 1. ]
    D2: !!opencv-matrix
       rows: 1
       cols: 5
       dt: d
       data: [ -1.6916358306948096e-01, -1.1214173641213163e-01, 0., 0., 0. ]
    ```


*   Pares de imagens da câmera esquerda e direita capturadas simultaneamente, mostrando um padrão de tabuleiro de xadrez. As imagens devem estar armazenadas em pastas separadas, por exemplo, `calibration_left` e `calibration_right`, com nomes de arquivo correspondentes (ex: `left01.jpg` e `right01.jpg`).

## Entrada

O programa requer os seguintes dados de entrada:

1.  **Arquivo de Parâmetros Intrínsecos:** Um arquivo YAML (como `intrinsics.yml`) contendo:
    *   **Matriz Intrínseca da Câmera Esquerda (M1 ou K_left):** Representada pela chave `M1` no YAML. Seus dados são:
        ```
        [ 5.3480326845051309e+02, 0., 3.3568643204394891e+02, 0.,
          5.3480326845051309e+02, 2.4066183054066337e+02, 0., 0., 1. ]
        ```
    *   **Coeficientes de Distorção da Câmera Esquerda (D1 ou dist_left):** Representados pela chave `D1` no YAML. Seus dados são:
        ```
        [ 2.9589439552724328e-01, -1.0354662043042675e+00, 0., 0., 0. ]
        ```
    *   **Matriz Intrínseca da Câmera Direita (M2 ou K_right):** Representada pela chave `M2` no YAML. Seus dados são:
        ```
        [ 5.3480326845051309e+02, 0., 3.3455744527912015e+02, 0.,
          5.3480326845051309e+02, 2.4205324573376600e+02, 0., 0., 1. ]
        ```
    *   **Coeficientes de Distorção da Câmera Direita (D2 ou dist_right):** Representados pela chave `D2` no YAML. Seus dados são:
        ```
        [ -1.6916358306948096e-01, -1.1214173641213163e-01, 0., 0., 0. ]
        ```
2.  **Imagens do Tabuleiro de Xadrez:** Pares de imagens das câmeras esquerda e direita contendo um tabuleiro de xadrez de tamanho conhecido. O tamanho do tabuleiro de xadrez precisa ser especificado no código (ex: `chessboard_size = (9, 6)` para um tabuleiro de 9x6 quadrados internos).

## Como Executar

1.  Salve os parâmetros intrínsecos fornecidos em um arquivo chamado `intrinsics.yml` no diretório do seu projeto.
2.  Organize seus pares de imagens do tabuleiro de xadrez nas pastas `calibration_left` e `calibration_right` dentro do diretório do projeto.
3.  Crie um arquivo Python (por exemplo, `stereo_calibration.py`) com o código baseado nos excertos fornecidos. O código deve incluir as funções `load_intrinsics`, `find_corners`, `calibrate_stereo` e uma função principal (`main`) para coordenar o processo.
4.  No script Python, defina o `chessboard_size` de acordo com o tabuleiro que você utilizou nas imagens.

5.  O programa irá primeiro carregar os parâmetros intrínsecos e as imagens. Em seguida, tentará encontrar os cantos do tabuleiro de xadrez em cada par de imagens. Se os cantos forem encontrados em ambas as imagens, a função `cv2.stereoCalibrate` será chamada para realizar a calibração estéreo.
6.  Se a calibração for bem-sucedida, o programa exibirá a **matriz de rotação (R)** e o **vetor de translação (T)** entre as câmeras. Além disso, janelas mostrarão as imagens esquerda e direita com as linhas epipolares sobrepostas.

## Saída

O programa produzirá as seguintes informações:

*   **Matriz de Rotação (R):** Uma matriz 3x3 que descreve a orientação relativa da câmera direita em relação à câmera esquerda.
*   **Vetor de Translação (T):** Um vetor 3x1 que descreve a posição relativa da origem da câmera direita em relação à origem da câmera esquerda.
*   **Imagens com Linhas Epipolares:** Janelas exibindo as imagens das câmeras esquerda e direita com as linhas epipolares desenhadas. As linhas epipolares representam os possíveis locais na imagem direita que correspondem a um ponto na imagem esquerda (e vice-versa), com base na geometria estéreo das câmeras.

## Considerações e Possíveis Problemas

*   **Falha na Detecção de Cantos:** A calibração estéreo depende da correta detecção dos cantos do tabuleiro de xadrez em ambos os pares de imagens. Se os cantos não forem encontrados em uma ou ambas as imagens, a calibração não poderá prosseguir. Certifique-se de que os tabuleiros de xadrez estejam claramente visíveis em todas as imagens e que o tamanho do tabuleiro especificado no código (`chessboard_size`) corresponda ao padrão utilizado.
*   **Qualidade das Imagens:** A qualidade das imagens (foco, iluminação, ausência de desfoque de movimento) é crucial para uma calibração precisa.
*   **Número de Pares de Imagens:** Um número suficiente de pares de imagens capturados de diferentes ângulos e posições do tabuleiro de xadrez geralmente leva a resultados de calibração mais robustos.
*   **Erro na `cv2.stereoCalibrate()`:** Conforme mencionado nos comentários do código, um erro na função `cv2.stereoCalibrate()` pode ocorrer se os pontos correspondentes não forem encontrados corretamente. Isso pode ser devido a problemas na detecção de cantos ou na qualidade dos dados de entrada.

