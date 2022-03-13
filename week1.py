def find_crossover_index_helper(x=[], y=[], left=0, right=1):
    # homework code has this assertion section.
    assert (len(x) == len(y))
    assert (left >= 0)
    assert (left <= right - 1)
    assert (right < len(x))
    # Here is the key property we would like to maintain.
    assert (x[left] > y[left])
    assert (x[right] < y[right])

    # arrays need to be of equal size; left needs to be <= right
    if len(x) != len(y) or left > right:
        return None
    elif left == right:
        return left

    mid = (right + left) // 2
    if y[mid] <= x[mid] and x[mid + 1] < y[mid + 1]:
        # this is the crossover point
        return mid
    elif y[mid] <= x[mid]:
        # y is still less than x, so search to the right of mid
        return find_crossover_index_helper(x, y, mid + 1, right)
    else:
        # y is larger than x, so search to the left of mid
        return find_crossover_index_helper(x, y, left, mid - 1)


def test_find_crossover_index_helper():
    x = [4, 6, 8, 10, 12]
    y = [3, 5, 8, 13, 21]
    expected_value = 2
    crossover_index = find_crossover_index_helper(x, y, 0, len(x) - 1)
    print(f'crossover index of {x} and {y} is {crossover_index}')
    assert (expected_value == crossover_index)


def integer_cube_root_helper(n, left, right):
    cube = lambda x: x * x * x  # anonymous function to cube a number
    assert (n >= 1)
    assert (left < right)
    assert (left >= 0)
    assert (right < n)
    assert (cube(left) < n), f'{left}, {right}'
    assert (cube(right) > n), f'{left}, {right}'

    if left >= right or n <= 0:
        return None

    mid = (left + right + 1) // 2

    if mid ** 3 <= n and (mid + 1) ** 3 > n:
        # this is the answer
        return mid
    elif (mid - 1) ** 3 <= n and mid ** 3 > n:
        # mid - 1 is the answer
        # this is only necessary because of the assertion the homework put in of left < right
        return mid - 1
    elif mid ** 3 > n:
        # mid is too large, look to the left of mid
        return integer_cube_root_helper(n, left, mid - 1)
    else:
        # mid is too small, look to the right of mid
        return integer_cube_root_helper(n, mid + 1, right)


def test_integer_cube_root_helper():
    n = 100
    expected_value = 4
    root = integer_cube_root_helper(n, 1, n - 1)
    print(f'integer cube root of {n} is {root}')
    assert (expected_value == root)

    n = 4
    expected_value = 1
    root = integer_cube_root_helper(n, 1, n - 1)
    print(f'integer cube root of {n} is {root}')
    assert (expected_value == root)


def two_way_merge(lst1=[], lst2=[]):
    # naming convention in the homework is yucky
    list1 = lst1
    list2 = lst2
    result = []

    assert (len(list1) > 0)
    assert (len(list2) > 0)

    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i = i + 1
        else:
            # list1[i] > list2[j]:
            result.append(list2[j])
            j = j + 1

    while i < len(list1):
        result.append(list1[i])
        i = i + 1

    while j < len(list2):
        result.append(list2[j])
        j = j + 1

    return result


def test_two_way_merge():
    a = [1, 2, 4, 6, 8, 10]
    b = [1, 2, 3, 5, 8, 13]
    expected_value = [1, 1, 2, 2, 3, 4, 5, 6, 8, 8, 10, 13]
    merged = two_way_merge(a, b)
    print(f'Merge of {a} and {b} is {merged}')
    assert (expected_value == merged)


def merge_sort(a=[]):
    if len(a) <= 1:
        return a
    elif len(a) == 2 and a[0] <= a[1]:
        return a
    elif len(a) == 2 and a[0] > a[1]:
        return [a[1], a[0]]

    mid = len(a) // 2
    left = merge_sort(a[0:mid])
    right = merge_sort(a[mid:len(a)])

    result = two_way_merge(left, right)

    return result


def test_merge_sort():
    a = [3, 6, 2, 1, 2, 3, 6, 1, 9]
    expected_value = [1, 1, 2, 2, 3, 3, 6, 6, 9]
    merged = merge_sort(a)
    print(f'merge_sort of {a} is {merged}')
    assert (expected_value == merged)

    a = [1957, 1958, 1966, 1978, 1981, 2012, 2016]
    expected_value = [1957, 1958, 1966, 1978, 1981, 2012, 2016]
    merged = merge_sort(a)
    print(f'merge_sort of {a} is {merged}')
    assert (expected_value == merged)

    a = [1957, 2016, 2012, 1981, 1978, 1966, 1958]
    expected_value = [1957, 1958, 1966, 1978, 1981, 2012, 2016]
    merged = merge_sort(a)
    print(f'merge_sort of {a} is {merged}')
    assert (expected_value == merged)


if __name__ == '__main__':
    test_find_crossover_index_helper()
    test_integer_cube_root_helper()
    test_two_way_merge()
    test_merge_sort()
