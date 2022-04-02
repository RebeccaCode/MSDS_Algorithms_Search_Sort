import time
import unittest

from numpy import log10
from numpy.random import randint

from heaps import *
import copy


class TestHeaps(unittest.TestCase):

    def test_min_heapify_bubble_down(self):
        a = [118, 454, 896, 237, 876, 24, 189, 34, 89]
        b = randint(0, 999, 99)
        for x in [a, b]:
            sorted = heapify(x, min=True)
            self.assert_min_heap(sorted)

    def test_max_heapify_bubble_down(self):
        a = [118, 454, 896, 237, 876, 24, 189, 34, 89]
        b = randint(0, 999, 99)
        for x in [a, b]:
            sorted = heapify(x, min=False)
            self.assert_max_heap(sorted)

    def assert_min_heap(self, sorted):
        for i in range(len(sorted)):
            left = (2 * i) + 1
            right = left + 1

            if left < len(sorted):
                assert (sorted[i] <= sorted[left])

            if right < len(sorted):
                assert (sorted[i] <= sorted[right])

    def assert_max_heap(self, sorted):
        for i in range(len(sorted)):
            left = (2 * i) + 1
            right = left + 1

            if left < len(sorted):
                assert (sorted[i] >= sorted[left])

            if right < len(sorted):
                assert (sorted[i] >= sorted[right])

    def test_heapify_runtime(self):
        power = 1
        max_power = 8
        min_value = 0
        max_value = 10 ** max_power
        while power <= max_power:
            size = 10 ** power
            print(f'power is {power}')

            source_array = randint(min_value, max_value, size)

            run_start = time.time()
            test_array = copy.deepcopy(source_array)
            test_array.sort()
            run_end = time.time()
            runtime = run_end - run_start

            print(f'Execution of Python List sort with array size {size} took {runtime} milliseconds.')

            test_array = copy.deepcopy(source_array)
            run_start = time.time()
            sorted = heapify(test_array, min=True)
            run_end = time.time()
            runtime = run_end - run_start

            print(f'Execution of heapify(b, min=True) with array size {size} took {runtime} milliseconds.')
            self.assert_min_heap(sorted)

            test_array = copy.deepcopy(source_array)
            run_start = time.time()
            sorted = heapify(test_array, min=False)
            run_end = time.time()
            runtime = run_end - run_start

            print(f'Execution of heapify(b, min=False) with array size {size} took {runtime} milliseconds.')
            self.assert_max_heap(sorted)

            power = power + 1
