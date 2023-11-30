import heapq


class SeatManager(object):

    def __init__(self, n):
        self.seat = list(range(1, n + 1))

    def reserve(self):
        return heapq.heappop(self.seat)

    def unreserve(self, seatNumber):
        heapq.heappush(self.seat, seatNumber)
