import numpy as np


class World(object):
    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.states = [np.full((height, width), 0)]
        self.current_day = 0

    def next_day(self):
        if self.current_day == len(self.states) - 1:
            current_day = self.states[-1]
            u = np.pad(current_day, ((1, 0), (0, 0)))[:-1, :]
            d = np.pad(current_day, ((0, 1), (0, 0)))[1:, :]
            l = np.pad(current_day, ((0, 0), (1, 0)))[:, :-1]
            r = np.pad(current_day, ((0, 0), (0, 1)))[:, 1:]
            ul = np.pad(current_day, ((1, 0), (1, 0)))[:-1, :-1]
            ur = np.pad(current_day, ((1, 0), (0, 1)))[:-1, 1:]
            dl = np.pad(current_day, ((0, 1), (1, 0)))[1:, :-1]
            dr = np.pad(current_day, ((0, 1), (0, 1)))[1:, 1:]

            n = u + d + l + r + ul + ur + dl + dr

            self.states.append(
                current_day * ((n == 2) | (n == 3)) + (1 - current_day) * (n == 3)
            )

        self.current_day += 1
        return self.states[self.current_day]

    def previous_day(self):
        self.current_day = max(0, self.current_day - 1)
        return self.states[self.current_day]
