import cv2
import numpy as np

# Função para carregar os parâmetros intrínsecos de calibração das câmeras
def load_intrinsics(file_path):
    # cv2.FileStorage é usado para ler arquivos como YAML (um tipo de arquivo de configuração)
    fs = cv2.FileStorage(file_path, cv2.FILE_STORAGE_READ)
    
    # Lê as matrizes e coeficientes de distorção de um arquivo YAML.
    K_left = fs.getNode("M1").mat()  # Matriz intrínseca da câmera esquerda
    dist_left = fs.getNode("D1").mat()  # Coeficientes de distorção da câmera esquerda
    K_right = fs.getNode("M2").mat()  # Matriz intrínseca da câmera direita
    dist_right = fs.getNode("D2").mat()  # Coeficientes de distorção da câmera direita
    
    fs.release()  # Fecha o arquivo após a leitura
    return K_left, dist_left, K_right, dist_right  # Retorna as variáveis com os dados lidos

# Função para encontrar os cantos do tabuleiro de xadrez nas imagens
def find_corners(image_left, image_right, chessboard_size):
    # Vamos transformar as imagens coloridas em imagens em preto e branco (escala de cinza).
    gray_left = cv2.cvtColor(image_left, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(image_right, cv2.COLOR_BGR2GRAY)
    
    # Agora, tentamos encontrar os cantos do tabuleiro de xadrez nas duas imagens.
    # O tabuleiro de xadrez deve ter um número fixo de quadrados, dado em "chessboard_size" (exemplo: 9x6).
    ret_left, corners_left = cv2.findChessboardCorners(gray_left, chessboard_size)
    ret_right, corners_right = cv2.findChessboardCorners(gray_right, chessboard_size)
    
    # Se conseguimos encontrar os cantos em ambas as imagens...
    if ret_left and ret_right:
        # Refinar os cantos encontrados para uma maior precisão.
        # Isso é chamado de refinamento subpixel, ou seja, vamos tentar encontrar os pontos com mais exatidão.
        cv2.cornerSubPix(gray_left, corners_left, (11, 11), (-1, -1), 
                         criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1))
        cv2.cornerSubPix(gray_right, corners_right, (11, 11), (-1, -1), 
                         criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1))
        
        # Agora, desenhamos os cantos encontrados nas imagens para mostrar onde foram localizados.
        cv2.drawChessboardCorners(image_left, chessboard_size, corners_left, ret_left)
        cv2.drawChessboardCorners(image_right, chessboard_size, corners_right, ret_right)
        
        # Exibimos as imagens com os cantos desenhados para que possamos ver os resultados.
        cv2.imshow("Imagem da Esquerda com Cantos", image_left)
        cv2.imshow("Imagem da Direita com Cantos", image_right)
        cv2.waitKey(0)  # Espera até pressionar qualquer tecla para fechar as janelas
        cv2.destroyAllWindows()  # Fecha as janelas de exibição das imagens

        return [corners_left], [corners_right]  # Retorna os cantos encontrados para a calibração (listas de listas)
    else:
        # Se os cantos não forem encontrados em uma das imagens, retorna listas vazias
        print("Cantos não encontrados em uma ou ambas as imagens.")
        return [], []  # Retorna listas vazias

# Função para realizar a calibração do par estéreo (as duas câmeras)
def calibrate_stereo(K_left, dist_left, K_right, dist_right, image_left, image_right, chessboard_size):
    # Primeiro, tentamos encontrar os cantos nas imagens.
    corners_left, corners_right = find_corners(image_left, image_right, chessboard_size)
    
    # Se não conseguimos encontrar os cantos em ambas as imagens, não podemos continuar com a calibração.
    if len(corners_left) == 0 or len(corners_right) == 0:
        print("Não foi possível encontrar os cantos do tabuleiro de xadrez.")
        return None, None, None, None  # Retorna None (não há calibração)

    # Obter o tamanho das imagens. Isso é necessário para a calibração.
    image_size = (image_left.shape[1], image_left.shape[0])  # Largura e altura da imagem (formato: (largura, altura))

    # A calibração estéreo tenta encontrar os parâmetros que mapeiam um ponto 3D em uma imagem 2D.
    # Precisamos dos pontos de cada câmera, suas matrizes intrínsecas, distorções e as dimensões das imagens.
    ret, camera_matrix_left, dist_coeffs_left, camera_matrix_right, dist_coeffs_right, R, T, E, F = \
        cv2.stereoCalibrate(corners_left, corners_right, None, K_left, dist_left, K_right, dist_right, 
                            image_size, criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1), flags=0)
    
    if not ret:  # Se a calibração não foi bem-sucedida
        print("Falha na calibração estéreo.")
        return None, None, None, None  # Retorna None em caso de falha

    # Retorna a matriz de rotação (R) e o vetor de translação (T), que nos ajudam a entender a posição relativa das câmeras
    return R, T, corners_left, corners_right

# Função principal do programa
def main():
    # Definir o caminho para o arquivo com os parâmetros intrínsecos (as calibrações das câmeras)
    intrinsics_file = 'intrinsics.yml'  # Caminho para o arquivo YAML com as calibrações

    # Carregar os parâmetros de calibração da câmera
    K_left, dist_left, K_right, dist_right = load_intrinsics(intrinsics_file)

    # Imprimir as matrizes e coeficientes das câmeras para verificar se foram carregados corretamente
    print("Matriz intrínseca da câmera esquerda (K_left):")
    print(K_left)
    print("Matriz intrínseca da câmera direita (K_right):")
    print(K_right)
    print("Coeficientes de distorção da câmera esquerda (dist_left):")
    print(dist_left)
    print("Coeficientes de distorção da câmera direita (dist_right):")
    print(dist_right)

    # Definir o tamanho do tabuleiro de xadrez (exemplo: 9 quadrados de largura e 6 de altura)
    chessboard_size = (9, 6)

    # Carregar as imagens das câmeras (as fotos tiradas com as câmeras)
    image_left = cv2.imread('calibration_left/left01.jpg')
    image_right = cv2.imread('calibration_right/right01.jpg')

    # Verificar se as imagens foram carregadas corretamente
    if image_left is None or image_right is None:
        print("Erro ao carregar as imagens.")
        return  # Se as imagens não foram carregadas, não podemos continuar

    # Calibrar o par estéreo usando as imagens e os parâmetros das câmeras
    R, T, corners_left, corners_right = calibrate_stereo(K_left, dist_left, K_right, dist_right, 
                                                           image_left, image_right, chessboard_size)
    
    # Se a calibração for bem-sucedida, imprimimos as matrizes de rotação (R) e translação (T)
    if R is not None and T is not None:
        print("Matriz de rotação (R):")
        print(R)
        print("Vetor de translação (T):")
        print(T)
        
        # Exibir as imagens com as linhas epipolares
        cv2.imshow('Esquerda - Linhas Epipolares', image_left)
        cv2.imshow('Direita - Linhas Epipolares', image_right)
        cv2.waitKey(0)  # Espera até pressionar qualquer tecla para fechar as janelas
        cv2.destroyAllWindows()  # Fecha as janelas

# Quando o programa for executado, chama a função principal
if __name__ == "__main__":
    main()


# Erro que estou encontrando no stereocalibrate:

# A função `cv2.stereoCalibrate()` tenta calibrar um sistema de câmeras estéreo (duas câmeras). Ela precisa de:
# - Pontos correspondentes nas imagens das duas câmeras (por exemplo, os cantos do tabuleiro de xadrez).
# - Matrizes intrínsecas das câmeras (as informações sobre como as câmeras capturam as imagens).
# - Coeficientes de distorção (para corrigir distorções causadas pelas lentes).

# O erro ocorre quando a função não encontra os pontos correspondentes em ambas as imagens. 
# Isso pode ser causado por diversos fatores, que confesso que não sei como resolver :(

# O erro específico ocorre porque os pontos correspondentes (corners_left e corners_right) 
# não estão sendo encontrados corretamente, o que faz com que a calibração não seja possível. 