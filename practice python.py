def binarySearch(array, target):
    low = 0
    high = len(array)-1

    while low <= high:
        medium = ((low + high)//2)
        if target < array[medium]:
            high = medium
        elif target > array[medium]:
            low = medium
        elif target == array[medium]:
            return array.index(target)
            break
    return -1


array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
print(binarySearch(array, target))
