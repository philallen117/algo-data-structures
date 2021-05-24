class Recurse(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


def recurse(*args, **kwargs):
    raise Recurse(*args, **kwargs)


def tail_recursive(f):
    def decorated(*args, **kwargs):
        while True:
            try:
                return f(*args, **kwargs)
            except Recurse as r:
                args = r.args
                kwargs = r.kwargs
                continue
    return decorated


@tail_recursive
def factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        recurse(n-1, acc=acc * n)


if __name__ == '__main__':
    print("Example: factorial")
    template = "factorial {} is {}"
    for i in range(1, 17):
        print(template.format(i, factorial(i)))
    print(template.format(1999, factoril(1999)))
