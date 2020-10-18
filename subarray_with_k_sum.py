def sub_array_with_k_sum(nums,k):
    counts={0:1}
    total=0
    counter=0
    for i in nums:
        total=i+total
        if total-k in counts:
            counter+=counts[total-k]
        
        if total in counts:
            counts[total]+=1
        else:
            counts[total]=1
    
    return counter

print(sub_array_with_k_sum([3,4,7,2,-3,1,4,2,1],7))



