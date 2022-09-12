
# Linear Search in Python
def linearSearch(array):
    x = int(input("Enter the search number:"))
    n = len(array)

    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1

array = list(map(int,input("Enter an array: ").split()))


result = linearSearch(array)
if (result == -1):
    print("Element not found")
else:
    print("Element found at position: ", result+1)


