def merge(left_array,right_array):
    result = []
    while len(left_array) and len(right_array):
        if left_array[0] > right_array[0]:
            result.append(left_array.pop(0))
        else:
            result.append(right_array.pop(0))
    result = result + left_array if len(left_array) else result + right_array
    return result


def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    left_array = array[0:mid]
    right_array = array[mid:]

    return merge(merge_sort(left_array),merge_sort(right_array))


if __name__ == '__main__':
    arr = [41, 3, 52, 26, 38, 57, 9, 1]
    print(merge_sort(arr))
