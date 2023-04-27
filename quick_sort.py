import random
import timeit


def partition(arr, first, last):
    pivot = arr[first]
    j = last - 1
    for i in range(first + 1, last):
        if arr[i] > pivot:
            while j > i:
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    j -= 1
                    break
                j -= 1
        if j <= i:
            arr[j - 1], arr[first] = arr[first], arr[j - 1]
            break

    return j - 1


def quick_sort(arr, first, last):
    if first == last:
        return
    if last - first == 1:
        return
    if last - first == 2:
        if arr[last - 1] < arr[first]:
            arr[last - 1], arr[first] = arr[first], arr[last - 1]
    if last > 0:
        pivot_index = partition(arr, first, last)
        quick_sort(arr, first, pivot_index)
        quick_sort(arr, pivot_index + 1, last)


# def partition_2(arr, first, last):
#     pivot = arr[first]
#     j = last - 1
#     for i in range(first + 1, last):
#         if arr[i] > pivot:
#             while j > i:
#                 if pivot > arr[j]:
#                     arr[i], arr[j] = arr[j], arr[i]
#                     j -= 1
#                 break
#             j -= 1
#
#         if j <= i:
#             arr[first], arr[j - 1] = arr[j - 1], arr[first]
#             break
#     return j - 1
#
#
# def quick_sort_2(arr, first, last):
#     if first > last:
#         return
#     if first == last:
#         return
#     if last - first == 2:
#         if arr[last - 1] < arr[first]:
#             arr[last - 1], arr[first] = arr[first], arr[last - 1]
#     if last > 0:
#         pivot_index = partition(arr,first,last)
#         quick_sort(arr,first,pivot_index)
#         quick_sort(arr,pivot_index+1,last)


def sort_random_numbers():
    items = [random.randint(0, 1000000) for i in range(10000)]
    quick_sort(items, 0, len(items))


def main():
    # t = timeit.timeit("sort_random_numbers()", setup="from __main__ import sort_random_numbers", number=100)
    # print(t)
    arr = [1, 4, 6, 7, 8, 4, 5, 2, 3, 17, 13, 29, 23]
    quick_sort(arr, 0, len(arr))
    print(arr)


if __name__ == '__main__':
    main()
