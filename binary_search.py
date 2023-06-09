def binary_search(arr, number):
    first = 0
    last = len(arr) - 1
    while first < last:
        mid = (first + last) // 2
        if arr[mid] < number:
            first = mid + 1
        elif arr[mid] > number:
            last = mid - 1
        elif arr[mid] == number:
            return mid
        else:
            return -1
    return mid


def binary_search_recursive(arr, number, first, last):
    if first > last:
        return -1

    while first < last:
        mid = (first + last) // 2
        if arr[mid] > number:
            last = mid - 1
            return binary_search_recursive(arr, number, first, last)
        elif arr[mid] < number:
            first = mid + 1
            return binary_search_recursive(arr, number, first, last)
        elif arr[mid] == number:
            return mid
    return mid


if __name__ == '__main__':
    arr = [5, 2, 1, 7, 3, 6, 11, 12, 15, 13 , 18]
    arr.sort()
    print(binary_search(arr, 13))
    print(binary_search_recursive(arr, 13, 0, len(arr) - 1))
