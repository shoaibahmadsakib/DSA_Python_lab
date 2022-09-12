def selectionSort(nums):
    size =len(nums)
    for i in range(size):
        minpos = i

        for j in range(i,size ):
            if nums[j] < nums[minpos]:
                minpos = j

        # put min at the correct position
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

nums = list(map(int , input("enter: ").split()))
selectionSort(nums)
print(nums)
