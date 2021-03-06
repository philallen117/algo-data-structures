# python3
import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []

    def empty(self):
        return not self.__stack

    def push(self, a):
        self.__stack.append(a)

    def pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def max(self):
        assert(len(self.__stack))
        return max(self.__stack)


def test():
    s = StackWithMax()
    s.push(1)
    assert(not s.empty())
    s.push(5)
    assert(5 == s.max())
    s.push(3)
    assert(5 == s.max())
    s.push(6)
    assert(6 == s.max())
    s.pop()
    assert(5 == s.max())
    s.pop()
    s.pop()
    assert(1 == s.max())


if __name__ == '__main__':
    stack = StackWithMax()
    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max())
        else:
            assert(0)
