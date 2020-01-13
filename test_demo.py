from demo import *
import random


def test_Max():
    a = []
    for i in range(10):
        a.append(random.randint(10, 100))

    m = Max(a)
    for x in a:
        assert(m >= x)
