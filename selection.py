import math


def find_the_min_in_array(A, i) -> (int, int):
    min_value = math.inf
    index_of_min = 0
    for j in range(i, len(A)):
        if A[j] < min_value:
            min_value = A[j]
            index_of_min = j
    return min_value, index_of_min


def selection_sorted(A):
    i = 0
    for times in range(len(A) - 1):
        min_value, index_of_min = find_the_min_in_array(A, i)
        A[times], A[index_of_min] = min_value, A[times]
        i += 1
    return A


if __name__ == '__main__':
    print(selection_sorted([3, 2, 1, 5, 9, 7, 8, 11, 10]))
    print(selection_sorted([7, 1, 6, 5, 7, 8, 9, 9, 14, 16, 16, 14, 13, 12]))
    print(selection_sorted([3, 1, 7, 3, 5, 2, 1, 7, 8, 9, 8, 16, 15, 22, 76, 56, 64]))
