# python -m test_network <list of testfile names>

from pathlib import Path
from argparse import ArgumentParser
from process_packages import process_requests, Buffer, Request


def check(stem):
    requests = []
    exp_responses = []
    buffer_size = 0
    with Path('./tests/{}.a'.format(stem)).open() as answer_file, \
            Path('./tests/{}'.format(stem)).open() as test_case_file:
        buffer_size, n_requests = map(int, test_case_file.readline().split())
        for _ in range(n_requests):
            arrived_at, time_to_process = map(int, test_case_file.readline().split())
            requests.append(Request(arrived_at, time_to_process))
        for _ in range(n_requests):
            exp_responses.append(int(answer_file.readline()))

    b = Buffer(buffer_size)
    responses = process_requests(requests, b)
    i_responses = list(map(lambda r: -1 if r.dropped else r.started_at, responses))
    if exp_responses == i_responses:
        print('.')
    else:
        print('F act={} exp={}'.format(i_responses, exp_responses))


if __name__ == "__main__":
    ap = ArgumentParser()
    ap.add_argument(dest='stem', nargs='+')
    args = ap.parse_args()
    for stem in args.stem:
        check(stem)
