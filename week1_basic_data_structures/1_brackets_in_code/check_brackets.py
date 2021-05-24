# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["i", "c"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(i, next))
        elif next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            else:
                b = opening_brackets_stack.pop()
                if not are_matching(b.c, next):
                    return i + 1
    if not opening_brackets_stack:
        return 0
    else:
        return opening_brackets_stack[0].i + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == 0:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
