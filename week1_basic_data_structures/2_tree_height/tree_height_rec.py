def height_rec(n, parfents):
    heights = [-1]*n
    for v in range(n):
        if heights[v] > 0 or parents[v] == -1:
            continue
        path = [v]
        pv = parents[v]


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


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(height_rec(n, parents))
