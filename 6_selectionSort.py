def selectionSort(nums):
    for i in range(5):
        minpos = i

        for j in range(i, 6):
            if nums[j] < nums[minpos]:
                minpos = j

        # put min at the correct position
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

nums = list(map(int, input("enter array list").split()))
selectionSort(nums)
print(nums)
