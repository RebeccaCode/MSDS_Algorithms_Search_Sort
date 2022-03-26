import time
import unittest

from numpy import log10
from numpy.random import randint

from heaps import *
import copy

class TestHeaps(unittest.TestCase):

    def test_coalesce(self):
        default = -1

        x = 3
        c = coalesce(x, default)
        assert (c == x)

        x = None
        c = coalesce(x, default)
        assert (c == default)

    def test_binary_left(self):
        a = [1, 2, 3, 4, 6, 7]
        i = 2
        left = binary_left(a, i)
        assert (left == 5)

        i = 0
        left = binary_left(a, i)
        assert (left == 1)

        i = 5
        left = binary_left(a, i)
        assert (left is None)

    def test_binary_right(self):
        a = [1, 2, 3, 4, 6, 7]
        i = 1
        right = binary_right(a, i)
        assert (right == 4)

        i = 0
        right = binary_right(a, i)
        assert (right == 2)

        i = 2
        right = binary_right(a, i)
        assert (right is None)

        i = 5
        right = binary_right(a, i)
        assert (right is None)

    def test_binary_parent(self):
        a = [1, 2, 3, 4, 6, 7]
        i = 1
        parent = binary_parent(a, i)
        assert (parent == 0)

        i = 0
        parent = binary_parent(a, i)
        assert (parent is None)

        i = 2
        parent = binary_parent(a, i)
        assert (parent == 0)

        i = 5
        parent = binary_parent(a, i)
        assert (parent == 2)

    def test_array_swap(self):
        a = [1, 2, 3, 4, 6, 7]
        swap_1 = [7, 2, 3, 4, 6, 1]
        swapped = array_swap(a, 0, len(a) - 1)
        assert (swapped == swap_1)

    def test_min_parent_child(self):
        a = [118, 454, 896, 237, 876, 24, 189, 34, 89]
        parent = 0
        child = 2
        swapped, swap_occurred = min_parent_child(a, child=child, parent=parent)
        assert (swap_occurred is False)
        assert (swapped == a)

        a_1 = [118, 237, 896, 454, 876, 24, 189, 34, 89]
        parent = 1
        child = 3
        swapped, swap_occurred = min_parent_child(a, child=child, parent=parent)
        assert (swap_occurred is True)
        assert (swapped == a_1)

    def test_min_heapify(self):
        a = [118, 454, 896, 237, 876, 24, 189, 34, 89]
        sorted = min_heapify(a, 0, len(a) - 1)
        end = len(a) - 1
        for i in range(end):
            left = binary_left(sorted, i)
            right = binary_right(sorted, i)

            if left and left > 0:
                assert (sorted[i] <= sorted[left])

            if right and right > 1:
                assert (sorted[i] <= sorted[right])

            if (left and left == end) or (right and right == end):
                break

    def test_max_heapify(self):
        a = [118, 454, 896, 237, 876, 24, 189, 34, 89]
        sorted = max_heapify(a, 0, len(a) - 1)
        end = len(a) - 1
        for i in range(end):
            left = binary_left(sorted, i)
            right = binary_right(sorted, i)

            if left and left > 0:
                assert (sorted[i] >= sorted[left])

            if right and right > 1:
                assert (sorted[i] >= sorted[right])

            if (left and left == end) or (right and right == end):
                break

    def test_min_heapify_runtime(self):
        min_value = 0
        max_value = 10 ** 3
        power = 1
        max_power = 3
        while power <= max_power:
            size = 10 ** power

            a = randint(min_value, max_value, size)

            a_start = time.time()
            min_a = min_heapify(a, 0, len(a) - 1)
            a_end = time.time()
            runtime = a_end - a_start

            print(f'Execution of min_heapify with array size {size} took {runtime} milliseconds.')

            assert (runtime <= size * log10(size))

            power = power + 1

    def test_max_heapify_runtime(self):
        min_value = 0
        max_value = 10 ** 3
        power = 1
        max_power = 4
        while power <= max_power:
            size = 10 ** power

            a = randint(min_value, max_value, size)

            a_start = time.time()
            b = copy.deepcopy(a)
            b.sort()
            a_end = time.time()
            runtime = a_end - a_start

            print(f'Execution of Python List sort with array size {size} took {runtime} milliseconds.')

            a_start = time.time()
            max_a = max_heapify(a, 0, len(a) - 1)
            a_end = time.time()
            runtime = a_end - a_start

            print(f'Execution of max_heapify with array size {size} took {runtime} milliseconds.')

            assert (runtime <= size * log10(size))

            power = power + 1
