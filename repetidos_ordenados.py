"""
Funcion que devuelve una lista ordenada por frecuencia.
"""

import collections


def frequency_sort(items):
    """
    input: List[int]
    output: List[int]
    """
    counts = collections.Counter(items)
    print(counts)
    return sorted(items, key=lambda x: counts[x] * len(items) - items.index(x), reverse=True)


print(frequency_sort([8, 2, 6, 2, 6, 4, 4, 4, 6, 8, 4]))
print(frequency_sort([17, 99, 42]))
print(frequency_sort([1, 2, 2, 1]))
