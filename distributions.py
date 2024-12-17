import math

class Distribution:
    def __init__(self, pre):
        self.precision = pre
    def pdf(self, x):
        pass
    def cdf(self, x):
        pass 

class NormalDistribution(Distribution):
    def __init__(self, pre, mean, std):
        super().__init__(pre)
        self.mean = mean
        self.std = std
    def _factorial(x):
        out = 1
        for i in range(1, x+1):
            out *= i
        return out
    def rescale(self, x_val):
        return (x_val - self.mean) / self.std
    def pdf(self, x):
        scaled_x = self.rescale(x)
        return (1.0 / math.sqrt(2 * math.pi)) * math.exp((scaled_x ** 2) / 2.0)
    def cdf(self, x):
        scaled_x = self.rescale(x)
        out = 0
        for t in range(self.precision):
            out += (((-1) ** t) * (scaled_x ** (2*t+1)))/((2*t+1) * (2 ** t) * (self._factorial(t)))
        return (1.0 / math.sqrt(2 * math.pi)) * out
    def __add__(self, other):
        precise = self.precision if self.precision > other.precision else other.precision
        return NormalDistribution(precise, self.mean + other.mean, math.sqrt((self.std ** 2) + (other.std ** 2)))
    def __sub__(self, other):
        precise = self.precision if self.precision > other.precision else other.precision
        return NormalDistribution(precise, self.mean - other.mean, math.sqrt((self.std ** 2) + (other.std ** 2)))
    def __eq__(self, other):
        return self.mean == other.mean and self.std == other.std
    

    