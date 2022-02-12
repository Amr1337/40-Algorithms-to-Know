import random
from itertools import permutations
from time import perf_counter
from collections import Counter

from matplotlib import pyplot as plt


def greedy_algorithm(cities, start=None):
    C = start or first(cities)
    tour = [C]
    unvisited = set(cities - {C})
    while unvisited:
        C = nearest_neighbor(C, unvisited)
        tour.append(C)
        unvisited.remove(C)
    return tour


def distance_tour(aTour):
    return sum(distance_points(aTour[i - 1], aTour[i])
               for i in range(len(aTour)))


def first(collection): return next(iter(collection))


def nearest_neighbor(A, cities):
    return min(cities, key=lambda C: distance_points(C, A))


aCity = complex


def generate_cities(number_of_cities):
    seed = 111
    width = 500
    height = 300
    random.seed((number_of_cities, seed))
    return frozenset(aCity(random.randint(1, width), random.randint(1,
                                                                    height))
                     for c in range(number_of_cities))


def distance_points(first, second): return abs(first - second)


def visualize_tour(tour, style='bo-'):
    if len(tour) > 1000: plt.figure(figsize=(15, 10))
    start = tour[0:1]
    visualize_segment(tour + start, style)
    visualize_segment(start, 'rD')


def visualize_segment(segment, style='bo-'):
    plt.plot([X(c) for c in segment], [Y(c) for c in segment], style,
             clip_on=False)
    plt.axis('scaled')
    plt.axis('off')


def X(city): "X axis"; return city.real


def Y(city): "Y axis"; return city.imag


def tsp(algorithm, cities):
    t0 = perf_counter()
    tour = algorithm(cities)
    t1 = perf_counter()
    assert Counter(tour) == Counter(cities)  # Every city appears exactly once in tour
    visualize_tour(tour)
    print("{}: {} cities --> tour length {:.0f} (in {:.3f} sec)".format(name(algorithm), len(tour), distance_tour(tour),

                                                                        t1 - t0))


def name(algorithm): return algorithm.__name__.replace('_tsp', '')


tsp(greedy_algorithm, generate_cities(2000))  # greedy_algorithm: 1988 cities --> tour length 15755 (in 0.497 sec)

# a graph of the tour, .show() is good if you're using normal python session instead of magic functions as %inline
plt.show()
