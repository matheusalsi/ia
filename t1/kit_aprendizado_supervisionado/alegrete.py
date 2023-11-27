import numpy as np


def compute_mse(b, w, data):
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    y_real = data[:, 1]
    y_predict = np.array([])
    
    for x in data[:, 0]:
        linear_reg = w*x + b
        y_predict = np.append(y_predict, [linear_reg])

    print(y_predict)
    MSE = np.square(np.subtract(y_predict,y_real)).mean()
    return float(MSE)


def step_gradient(b, w, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """
    y_real = data[:, 1]
    y_predict = np.array([])
    
    for x in data[:, 0]:
        linear_reg = w*x + b
        y_predict = np.append(y_predict, [linear_reg])

    b_derivative = np.multiply(np.subtract(y_predict,y_real), 2).mean()
    w_derivative = np.multiply(np.subtract(y_predict,y_real), 2*data[:, 0]).mean()

    b = b - (alpha * b_derivative)
    w = w - (alpha * w_derivative)

    return float(b), float(w)


def fit(data, b, w, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """
    y_real = data[:, 1]
    list_b = []
    list_w = []

    for i in range(num_iterations):
        b, w = step_gradient(b , w, data, alpha)
        list_b.append(b)
        list_w.append(w)

    return list_b, list_w