import numpy


def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return n * factorial(n-1)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)


def reverse(arr):
    if len(arr) < 2:
        return arr
    return [arr[-1]] + reverse(arr[0:-1])


# def multiply_matrix(A, B, n):
#     if n == 1:
#         result = A[0][0] * B[0][0]
#         return
#
#     else:
#

if __name__ == '__main__':
    print(factorial(5))
    print(fib(5))
    arr = [5, 2, 1, 7, 3, 6, 11, 12, 15, 13]
    arr.sort()
    print(reverse(arr))

    # A = [[1, 2], [3, 4]]
    # B = [[5, 6], [7, 8]]
    # print(len(A))
    # print(len(B))
    # print(numpy.array(A))
    # print(numpy.array(B))
