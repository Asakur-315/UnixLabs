import multiprocessing as mp
import yaml
import random
from typing import List

MATRIX1_FILE = "./matrix1.yml"
MATRIX2_FILE = "./matrix2.yml"
RESULT_FILE = "./result.yml"


def print_matrix(matrix: List[List[int]]) -> None:

    r = "\n" + "\n".join(["\t".join([str(cell) for cell in row]) for row in matrix])
    print(r)


def matrix_reader(file_name: str) -> List[List[int]]:

    with open(file_name, "r") as file:
        return yaml.safe_load(file)


def matrix_writer(matrix: List[List[int]], file_name: str) -> None:

    with open(file_name, "w") as file:
        yaml.safe_dump(matrix, file)


def matrix_gen(n: int, m: int) -> List[List[int]]:

    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(random.randint(1, 100))

    return matrix

def worker(i: int, j: int, A: list, B: list, que: mp.Queue) -> None:
    """
    Обработчик перемножения элементов матрицы
    Запускается в отдельном процессе
    """

    buffer_list = []
    for k in range(len(A[0]) or len(B)):
        buffer_list.append(A[i][k] * B[k][j])

    result_dict = {}
    result_dict["result"] = sum(buffer_list)
    result_dict["i"] = i
    result_dict["j"] = j

    que.put(result_dict)


def new_matrix_input():
    """Генерация новой матрицы"""
    n = int(input("Введите кол-во строк в матрице -> "))
    m = int(input("Введите кол-во столбцов в матрице -> "))

    # Генерируем
    matrix1 = matrix_gen(n, m)
    matrix2 = matrix_gen(m, n)

    # Пишем в файлы
    matrix_writer(matrix1, MATRIX1_FILE)
    matrix_writer(matrix2, MATRIX2_FILE)
    return matrix1, matrix2


def old_matrix_input():
    """Чтение уже существующих матриц из файлов"""
    return matrix_reader(MATRIX1_FILE), matrix_reader(MATRIX2_FILE)
