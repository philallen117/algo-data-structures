# python -m int_test <list of testfile names>

from pathlib import Path
from argparse import ArgumentParser
from tree_height import compute_height


def check(stem):
    with Path('./tests/{}.a'.format(stem)).open() as answer_file, \
            Path('./tests/{}'.format(stem)).open() as test_case_file:
        exp = int(answer_file.readline().strip())
        n = int(test_case_file.readline().strip())
        parents = list(map(int, test_case_file.readline().split()))
        act = compute_height(n, parents)
        if exp == act:
            print('.')
        else:
            print('F act={} exp={}'.format(act, exp))


if __name__ == "__main__":
    ap = ArgumentParser()
    ap.add_argument(dest='stem', nargs='+')
    args = ap.parse_args()
    for stem in args.stem:
        check(stem)
