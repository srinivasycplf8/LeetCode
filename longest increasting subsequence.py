def LIS(nums):
    L=[0]*len(nums)

    for k in range(0,len(nums)):
        L[k]=1
        for j in range(0,k):
            if (nums[j]<nums[k] and L[j]+1>L[k]):
                L[k]=L[j]+1
    
    return max(L)

print(LIS([7,7,7,7,7,7,7]))
