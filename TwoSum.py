class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts={}
        
        nums.sort()
        for i in nums:
            difference=target-i
            if difference not in counts:
                counts[i]=1
            else:
                starting=nums.index(difference)
                return nums.index(difference),nums.index(i,starting+1)