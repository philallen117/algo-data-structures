# python3

def parent(i): return (i - 1) // 2

def left(i): return 2 * i + 1

def right(i): return 2 * (i + 1)

def build_heap(data):
    """Build a heap from ``data`` inplace
    Returns a sequence of swaps performed by the algorithm.
    """
    n = len(data)  # elements 0 .. n-1
    swaps = []
    def swap(i, j):
        t = data[i]
        data[i] = data[j]
        data[j] = t
        swaps.append((i,j))
    def sift_down(i):
        # 3-way comparison to restore heap property to i
        new_i = i
        l = left(i); r = right(i)
        if l < n and data[l] < data[new_i]: new_i = l
        if r < n and data[r] < data[new_i]: new_i = r
        if not i == new_i:
            # i did not satsify heap property, swap and carry on down
            swap(i, new_i)
            sift_down(new_i)
    # starting from end, parent of n-1 is first that may break heap condition
    for i in range(parent(n - 1), -1, -1):
        sift_down(i)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

def deb1():
    data = [0, 1, 0]
    swaps = build_heap(data)
    print(swaps)
    print(data)

if __name__ == "__main__":
    deb1()
    # main()
