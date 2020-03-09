from datasette import hookimpl
import math


class StdevFunc:
    # Based on https://stackoverflow.com/a/24423341
    def __init__(self):
        self.M = 0.0
        self.S = 0.0
        self.k = 1

    def step(self, value):
        if value is None:
            return
        value = float(value)
        tM = self.M
        self.M += (value - tM) / self.k
        self.S += (value - tM) * (value - self.M)
        self.k += 1

    def finalize(self):
        if self.k < 3:
            return None
        return math.sqrt(self.S / (self.k-2))


@hookimpl
def prepare_connection(conn):
    conn.create_aggregate("stdev", 1, StdevFunc)
