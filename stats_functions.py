import math

stats_list = []

def mean(*args):
    if len(list(args)) == 1 and len(stats_list) > 0:
        return sum(stats_list)/len(stats_list)
    return sum(list(args))/len(list(args))

def std(*args):
    sq_err = 0
    mean_args = mean(*args)
    for arg in list(args):
        sq_err += (arg - mean_args) ** 2
    return math.sqrt(sq_err/len(list(args)))

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

#Recursive verison of normal cdf, just to prove its possible
def norm_cdf(t, x):
    if t == 0:
        return (((-1) ** t) * (x ** (2*t+1)))/((2*t+1) * (2 ** t) * (factorial(t)))
    return (((-1) ** t) * (x ** (2*t+1)))/((2*t+1) * (2 ** t) * (factorial(t))) + norm_cdf(t-1, x)

def norm_cdf2(t, x):
    out = 0
    for t in range(t):
        out += (((-1) ** t) * (x ** (2*t+1)))/((2*t+1) * (2 ** t) * (factorial(t)))
    return (1.0 / math.sqrt(2 * math.pi)) * out

