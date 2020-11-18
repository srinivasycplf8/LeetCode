def first_duplicate(a):
    counts={}
    for i in range(0,len(a)):
        if a[i] in counts and counts[a[i]]<2:
            counts[a[i]]+=1
            return a[i]
        else:
            counts[a[i]]=1
    return -1

print(first_duplicate([2, 4, 3, 5, 1]))