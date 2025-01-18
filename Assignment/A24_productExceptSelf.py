# prod just before it
import numpy

nums = [5, 1, 5, 2, 5]

print([numpy.prod([nums[j] for j in range(len(nums)) if j != i]) for i in range(len(nums))])


def prod(n):
    prod = 1
    for i in n:
        prod *= i
    return prod
