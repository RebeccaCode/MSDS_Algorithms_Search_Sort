def coalesce(x, default=-1):
    if x is None:
        x = default
    return x


def binary_left(a, i):
    # account for 0-index array
    x = i + 1
    left = (x * 2) - 1
    if left > len(a) - 1:
        left = None
    return left


def binary_right(a, i):
    # account for 0-index array
    x = i + 1
    right = ((x * 2) + 1) - 1
    if right > len(a) - 1:
        right = None
    return right


def binary_parent(a, i):
    # account for 0-index array
    x = i + 1

    if x == 1:
        parent = None
    elif x % 2 == 0:
        parent = int((x / 2) - 1)
    else:
        parent = int(((x - 1) / 2) - 1)

    return parent


def array_swap(a=[], i=0, j=0):
    x = a[j]
    a[j] = a[i]
    a[i] = x
    return a


def min_parent_child(a, child, parent):
    swap_occurred = False
    if parent is None or parent < 0:
        pass
    elif child is None or child < 0 or child > len(a) - 1:
        pass
    elif a[parent] > a[child]:
        a = array_swap(a, child, parent)
        swap_occurred = True
    else:
        pass
    return a, swap_occurred


def max_parent_child(a, child, parent):
    swap_occurred = False
    if parent is None or parent < 0:
        pass
    elif child is None or child < 0 or child > len(a) - 1:
        pass
    elif a[parent] < a[child]:
        a = array_swap(a, child, parent)
        swap_occurred = True
    else:
        pass
    return a, swap_occurred


def min_heapify(a=[], start=0, end=0):
    if start >= end:
        return a

    parent = start
    while parent < end:
        left = binary_left(a, parent)
        right = binary_right(a, parent)
        for x in [left, right]:
            a, swap_occurred = min_parent_child(a, child=x, parent=parent)
            if swap_occurred:
                parent_parent = coalesce(binary_parent(a, parent), -1)
                if parent_parent >= 0 and a[parent_parent] > a[parent]:
                    a = min_heapify(a, start=0, end=parent)

        if left == end or right == end:
            break

        parent = parent + 1

    return a


def max_heapify(a=[], start=0, end=0):
    if start >= end:
        return a

    parent = start
    while parent < end:
        left = binary_left(a, parent)
        right = binary_right(a, parent)
        for x in [left, right]:
            a, swap_occurred = max_parent_child(a, child=x, parent=parent)
            if swap_occurred:
                parent_parent = coalesce(binary_parent(a, parent), -1)
                if parent_parent >= 0 and a[parent_parent] < a[parent]:
                    a = max_heapify(a, start=0, end=parent)

        if left == end or right == end:
            break

        parent = parent + 1

    return a
