from base_command import Command
import numpy as np
import copy

class StatsObject:
    def __init__(self):
        self.mean = 0
        self.median = 0
        self.pop_std = 0
        self.sam_std = 0
        self.min = 0
        self.max = 0
        self.q1 = 0
        self.q3 = 0
    def apply(self, data):
        try:
            self.mean = np.mean(data)
            self.median = np.median(data)
            self.pop_std = np.std(data)
            self.sam_std = np.std(data, ddof=1)
            self.min = min(data)
            self.max = max(data)
            self.q1 = np.quantile(data, 1)
            self.q3 = np.quantile(data, 3)
        except:
            print("Data is not of type float, double or int!")
    def __str__(self):
        return f"Done!"