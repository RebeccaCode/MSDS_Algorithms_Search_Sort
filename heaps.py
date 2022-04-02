def heapify(a, min=True):
    last_parent = (len(a) // 2) - 1
    for i in range(last_parent, -1, -1):
        a = bubble_down(a, start=i, min=min)
    return a


def bubble_down(a=[], start=0, min=True):
    left = (2 * start) + 1
    right = left + 1

    # if there is a right node, start comparisons against right node
    if right < len(a):
        if min:
            # if left is smallest child and parent > left, swap
            if a[left] <= a[right] and a[start] > a[left]:
                a[start], a[left] = a[left], a[start]
                a = bubble_down(a, left, min)
            # right is smallest child; if parent > right, swap
            elif a[start] > a[right]:
                a[start], a[right] = a[right], a[start]
                a = bubble_down(a, right, min)
        else:
            # if left is largest child and parent < left, swap
            if a[left] >= a[right] and a[start] < a[left]:
                a[start], a[left] = a[left], a[start]
                a = bubble_down(a, left, min)
            # right is largest child; if parent < right, swap
            elif a[start] < a[right]:
                a[start], a[right] = a[right], a[start]
                a = bubble_down(a, right, min)
    # comparison against left node only
    elif left < len(a):
        if min:
            if a[start] > a[left]:
                a[start], a[left] = a[left], a[start]
                a = bubble_down(a, left, min)
        else:
            if a[start] < a[left]:
                a[start], a[left] = a[left], a[start]
                a = bubble_down(a, left, min)
    return a
