# python3
from collections import namedtuple

P = namedtuple('P', ['elem', 'max'])


class MaxIntStack:
    def __init__(self): self.__s = []

    def __str__(self): return str(self.__s)

    def empty(self): return not self.__s

    def max(self): return self.__s[-1].max

    def top(self): return self.__s[-1].elem

    def push(self, i):
        new_max = max(i, self.__s[-1].max) if self.__s else i
        self.__s.append(P(i, new_max))

    def pop(self): return self.__s.pop().elem

    def __s__(self): return self.__s

    def reverse(self):
        s = MaxIntStack()
        while len(self.__s) > 0:
            s.push(self.pop())
        self.__s = s.__s__()


class MaxIntQueue:
    def __init__(self):
        self.__back = MaxIntStack()
        self.__front = MaxIntStack()

    def add(self, i):
        self.__back.push(i)

    def take(self):
        if self.__front.empty():
            self.__back.reverse()
            self.__front = self.__back
            self.__back = MaxIntStack()
        return self.__front.pop()

    def max(self):
        t_front = -1000 if self.__front.empty() else self.__front.max()
        t_back = -1000 if self.__back.empty() else self.__back.max()
        return max(t_front, t_back)


def max_sliding_window(seq, m):
    maxima = []
    miq = MaxIntQueue()
    # Build initial m - 1 elements
    for i in seq[:m - 1]:
        miq.add(i)
    for i in seq[m - 1:]:
        miq.add(i)
        maxima.append(miq.max())
        miq.take()
    return maxima


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
    print(*max_sliding_window(input_sequence, window_size))
