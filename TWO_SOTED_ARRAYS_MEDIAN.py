def median(arr1, arr2):
    list3=arr1+arr2
    list3.sort()
    if len(list3)%2!=0:
       res=int(len(list3)/2 - 0.5)
       return list3[res]
    else:
        res=list3[round(len(list3)/2)-1]+list3[round(len(list3)/2)]
        return res/2
print(median([1],[2,3])) 