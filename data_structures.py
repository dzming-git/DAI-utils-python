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

from collections import deque

class AutoFIFO:
    def __init__(self, max_size=10):
        self.queue = deque()
        self.max_size = max_size

    def push(self, item):
        # 当队列达到最大长度时，自动从左端（即队列前端）弹出一个元素
        if len(self.queue) >= self.max_size:
            self.queue.popleft()  # FIFO的行为
        self.queue.append(item)

    def to_list(self) -> List:
        # 将deque转换成list
        return list(self.queue)

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.isFull():
            raise Exception("Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def __getitem__(self, index):
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")
        return self.queue[(self.front + index) % self.capacity]

    def getMiddleElement(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        middle_index = self.size // 2
        return self.__getitem__(middle_index)