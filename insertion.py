def insertion_sort_from_the_beginning_ascending(A):
    for i in range(1, len(A)):
        for j in range(i):
            if A[i] < A[j]:
                A[j], A[i] = A[i], A[j]
    return A


def insertion_sort_from_the_beginning_descending(A):
    for i in range(1, len(A)):
        for j in range(i):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    return A


def insertion_sort_from_the_end(A):
    for i in range(1, len(A)):
        ting_push_down(A, i)

    return A


def ting_push_down(A, i):
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
        A[j], A[j + 1] = A[j + 1], A[j]
        j -= 1


def insertion_sort_from_the_end2(A):
    for i in range(1, len(A)):
        push_down(A, i)
    return A


def push_down(A, i):
    while i - 1 >= 0 and A[i] < A[i - 1]:
        A[i], A[i - 1] = A[i - 1], A[i]
        i = i - 1


def searching_the_element(array, element):
    target = 0
    for i in range(len(array)):
        if array[i] == element:
            target = i
        else:
            target = None
    return target


def binary_integer_addition(A, B, n):
    C = []
    for i in range(n)[::-1]:
        total = A[i] + B[i]
        if total == 0:
            C.insert(0, 0)
        elif total == 1:
            C.insert(0, 1)
        elif total == 2:
            C.insert(0, 0)
    return C


def main():
    print(insertion_sort_from_the_beginning_ascending([31, 41, 59, 26, 41, 58]))
    print(insertion_sort_from_the_beginning_ascending([2, 5, 4, 3, 1, 7, 12, 9]))
    print(insertion_sort_from_the_beginning_descending([2, 5, 4, 3, 1, 7, 12, 9]))
    print(insertion_sort_from_the_end([2, 7, 5, 1, 3]))
    print(insertion_sort_from_the_end([2, 5, 4, 3, 1, 7, 12, 9]))
    print(searching_the_element([2, 4, 6, 7, 12, 54], 54))
    print(binary_integer_addition([1, 0, 1, 1, 0], [1, 1, 1, 1, 1], 5))


if __name__ == '__main__':
    main()
