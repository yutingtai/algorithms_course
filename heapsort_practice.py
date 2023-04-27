import math


# def parent(i):
#     return i // 2 - 1 if i % 2 == 0 else i // 2
#
#
# def left_child(i):
#     return 2 * i + 1
#
#
# def right_child(i):
#     return 2 * i + 2
#
#
# def flip(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]
#
#
# def heapify(arr, i):
#     parent_value = arr[i]
#     left_child_value = arr[left_child(i)] if len(arr) - 1 >= left_child(i) else -math.inf
#     right_child_value = arr[right_child(i)] if len(arr) - 1 >= right_child(i) else -math.inf
#     if left_child_value > right_child_value and left_child_value > parent_value:
#         flip(arr, left_child(i), i)
#         heapify(arr, left_child(i))
#
#     elif right_child_value > left_child_value and right_child_value > parent_value:
#         flip(arr, right_child(i), i)
#         heapify(arr, right_child(i))
#
#     return arr
#
#
# def make_heap(arr):
#     for i in range(parent(len(arr) - 1), -1, -1):
#         heapify(arr, i)
#     return arr
#
#
# def remove_max(arr):
#     max_value = arr[0]
#     flip(arr, 0, -1)
#     del arr[-1]
#     if len(arr) > 0:
#         heapify(arr, 0)
#     return max_value
#
#
# def heap_sort(arr):
#     cp_array = arr.copy()
#     heap_array = make_heap(cp_array)
#     s = []
#     while len(heap_array) > 0:
#         s.append(remove_max(heap_array))
#     return s


def parent(i):
    return i // 2 - 1 if i % 2 == 0 else i // 2


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def flip(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heapify(arr, i):
    parent_value = arr[i]
    left_child_value = arr[left_child(i)] if len(arr) - 1 >= left_child(i) else -math.inf
    right_child_value = arr[right_child(i)] if len(arr) - 1 >= right_child(i) else -math.inf
    if left_child_value > parent_value and left_child_value > right_child_value:
        flip(arr, i, left_child(i))
        heapify(arr, left_child(i))
    elif right_child_value > parent_value and right_child_value > left_child_value:
        flip(arr, i, right_child(i))
        heapify(arr, right_child(i))
    return arr


def make_heap(arr):
    for i in range(parent(len(arr) - 1), -1, -1):
        heapify(arr, i)
    return arr


def remove_max(arr):
    max_value = arr[0]
    flip(arr, 0, -1)
    del arr[-1]
    if len(arr) > 0:
        heapify(arr, 0)
    return max_value


def heap_sort(arr):
    s = []
    cp_arr = arr.copy()
    heap_array = make_heap(cp_arr)
    while len(heap_array) > 0:
        s.append(remove_max(heap_array))
    return s


def main():
    arr = [41, 3, 52, 26, 38, 57, 9, 1]
    print(make_heap(arr))
    print(heap_sort(arr))


if __name__ == '__main__':
    main()
