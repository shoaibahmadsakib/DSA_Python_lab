# Binary Search in python


def binarySearch(array):
    # Repeat until the pointers low and high meet each other
    x = int(input("enter the number of array"))
    high = len(array) - 1
    low = 0
    while low <= high:

        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1

array = [int(x) for x in input("Enter the elements for list:").split()]


result = binarySearch(array)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
