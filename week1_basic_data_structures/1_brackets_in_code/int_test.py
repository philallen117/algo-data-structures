# python -m int_test <list of testfile names>

from pathlib import Path
from argparse import ArgumentParser
from check_brackets import find_mismatch


def check(stem):
    with Path('./tests/{}.a'.format(stem)).open() as answer_file, \
            Path('./tests/{}'.format(stem)).open() as test_case_file:
        test_case = test_case_file.readline().strip()
        act = find_mismatch(test_case)
        answer = answer_file.readline().strip()
        exp = -1
        if answer == 'Success':
            exp = 0
        else:
            exp = int(answer)
        if exp == act:
            print('.')
        else:
            print('F act={} exp={}'.format(act, exp))


if __name__ == "__main__":
    ap = ArgumentParser()
    ap.add_argument(dest='stem', nargs='+')
    args = ap.parse_args()
    print(args.stem)
    for stem in args.stem:
        check(stem)
