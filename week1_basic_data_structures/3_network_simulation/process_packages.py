# python3

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "process_time"])
Response = namedtuple("Response", ["dropped", "started_at", "finished_at"])


class BoundedDeque:
    def __init__(self, size):
        self.size = size
        self.len = 0
        self.q = deque()

    def empty(self):
        return self.len == 0

    def full(self):
        return self.len == self.size

    def add(self, elem):
        if self.len == self.size:
            raise IndexError("Added to full BoundedDeq")
        self.len += 1
        self.q.appendleft(elem)

    def peek_last(self):
        if self.len == 0:
            raise IndexError("Peeked empty BoundedDeq")
        r = self.q.popleft()
        self.q.appendleft(r)
        return r

    def take(self):
        if self.len == 0:
            raise IndexError("Took empty BoundedDeq")
        self.len -= 1
        return self.q.pop()

    def drop_until(self, pred) -> None:
        # leaves first passing element in queue
        while True:
            try:
                nxt = self.take()
            except IndexError:
                break
            if pred(nxt):
                # put it back
                self.q.append(nxt)
                self.len += 1
                break


class Buffer:
    def __init__(self, size):
        self.size = size
        self.q = BoundedDeque(size)
        self.finish_time = []

    def process(self, req: Request) -> Response:
        arrival_time = req.arrived_at
        self.q.drop_until(lambda resp: resp.finished_at > arrival_time)
        r = None
        if self.q.full():
            # dropped, not added
            r = Response(True, None, None)
        elif self.q.empty():
            r = Response(False, arrival_time, arrival_time + req.process_time)
            self.q.add(r)
        else:
            last = self.q.peek_last()
            r = Response(False,
                         last.finished_at,
                         last.finished_at + req.process_time)
            self.q.add(r)
        return r


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))
    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)
    for response in responses:
        print(response.started_at if not response.dropped else -1)


if __name__ == "__main__":
    main()
