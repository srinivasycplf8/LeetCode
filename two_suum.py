def twosum(nums,target):

    counts = {}

    for i in range(len(nums)):
        difference=target-nums[i]
        if difference not in counts:
            counts[nums[i]]=difference
        else:
            return nums.index(difference),i

print(twosum([3,5,8],11))
