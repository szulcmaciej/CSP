import itertools


def subsets(iterable):
    l = list(iterable)
    return frozenset(frozenset(x) for x in  (itertools.chain.from_iterable(itertools.combinations(l,n) for n in range(len(l)+1))))
