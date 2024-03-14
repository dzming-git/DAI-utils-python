from typing import List, Tuple, Union

def is_rectangular_matrix(matrix: List[List[Union[int, float]]]) -> Tuple[bool, Union[str, Tuple[int, int]]]:
    """
    检查一个由列表构成的二维数组是否为矩形矩阵。

    参数:
        matrix (List[List[Union[int, float]]]): 需要检查的二维列表。

    返回:
        Tuple[bool, Union[str, Tuple[int, int]]]: 
        如果输入是矩形矩阵，返回(True, (行数, 列数))。
        如果输入不是矩形矩阵，返回(False, "不是矩形矩阵")。

    示例:
        >>> is_rectangular_matrix([[1, 2, 3], [4, 5, 6]])
        (True, (2, 3))
        >>> is_rectangular_matrix([[1, 2], [3, 4, 5]])
        (False, (-1, -1))
    """
    if not all(len(row) == len(matrix[0]) for row in matrix):
        return (False, (-1, -1))
    else:
        return (True, (len(matrix), len(matrix[0])))

# 示例使用
print(is_rectangular_matrix([[1, 2, 3], [4, 5, 6]]))  # 应返回(True, (2, 3))
print(is_rectangular_matrix([[1, 2], [4, 5, 6]]))  # 应返回(False, (-1, -1))
