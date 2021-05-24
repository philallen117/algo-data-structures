# python3

# import sys
# import threading


def compute_height(n, parents):
    heights = [0]*n
    for v in range(n):
        if heights[v] > 0 or parents[v] == -1:
            continue
        path = [v]
        pv = parents[v]
        while heights[pv] == 0 and pv != -1:
            path.append(pv)
            pv = parents[pv]
        h = 0 if pv == -1 else heights[pv]
        while len(path) > 0:
            pv = path.pop()
            h += 1
            heights[pv] = h
    return max(heights)


def compute_height_naive(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


if __name__ == '__main__':
    # In Python, the default limit on recursion depth is rather low,
    # so raise it here for this problem. Note that to take advantage
    # of bigger stack, we have to launch the computation in a new thread.
    # sys.setrecursionlimit(10**7)  # max depth of recursion
    # threading.stack_size(2**27)   # new thread will get stack of such size
    # threading.Thread(target=main).start()
    main()
