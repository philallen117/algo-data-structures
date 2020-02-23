# python3
from collections import namedtuple

P = namedtuple('P', ['elem', 'max'])


class MaxIntStack:
    def __init__(self): self.__s = []

    def __str__(self): return str(self.__s)

    def empty(self): return len(self.__s) == 0

    def max(self): return (self.__s[-1:][0]).max

    def top(self): return (self.__s[-1:][0]).elem

    def push(self, i):
        this_max = i if len(self.__s) == 0 else max(i, (self.__s[-1:][0]).max)
        self.__s.append(P(i, this_max))

    def pop(self): return self.__s.pop().elem

    def __s__(self): return self.__s

    def reverse(self):
        s = MaxIntStack()
        while len(self.__s) > 0:
            s.push(self.pop())
        self.__s__ = s.__s__


class MaxIntQueue:
    def __init__(self):
        self.__back = []
        self.__front = []

    def add(self, i):
        self.__back.push(i)

    def take(self):
        if len(self.__front) == 0:
            self.__front = self.__back.reverse()
        return self.__front.pop()


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))
