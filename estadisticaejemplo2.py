# Los guiones bajos indican que son funciones "privadas", destinadas a
# ser llamadas por nuestra función mediana pero no por otras personas
# que utilicen nuestra librería de estadísticas.

num_friends = [1, 10, 2, 9, 5] 
def _median_odd(xs: list[float]) -> float:
    return sorted(xs)[len(xs) // 2]

#####################################################
def _median_even(xs: list[float]) -> float:
    sorted_xs = sorted(xs) #1,2,5,9,
    hi_midpoint = len(xs) // 2 
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2  
#####################################################        
def median(v: list[float]) -> float:
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

print(median(num_friends))
#assert median([1, 10, 2, 9, 5]) == 5
#assert median([1, 9, 2, 10]) == (2 + 9) / 2

# calculando rango de dispercion

def _rangodisp(xs:list[float])-> float:

    return [max(xs)-min(xs)]

print(_rangodisp(num_friends))

# sacando los cuartiles
def quantile(xs: list[float], p: float) -> float:
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]
print(quantile(num_friends, 0.10))
print(quantile(num_friends, 0.25)) 
print(quantile(num_friends, 0.75))
print(quantile(num_friends, 0.90)) 

# varianza  
from statistics import mean
from turtle import dot

def sum_of_squares(xs: list[float]) -> float:
    return sum(x ** 2 for x in xs)

def de_mean(xs: list[float]) -> list[float]:
    x_bar = mean(xs)
    return [x-x_bar for x in xs]

def variance(xs: list[float]) -> float:
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) /(n)


import math
def standard_deviation(xs: list[float]) -> float:
    return math.sqrt(variance(xs))
assert 9.02 < standard_deviation(num_friends) < 9.04

def covariance(xs: list[float], ys: list[float]) -> float:
    assert len(xs) == len(ys), "xs and ys must have same number of elements"
    return dot(de_mean(xs), de_mean(ys)) / (len(xs))


def correlation(xs: list[float], ys: list[float]) -> float:
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x * stdev_y
    else:
        return 0 # si no hay variación, la correlación es cero