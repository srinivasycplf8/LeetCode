def first_duplicate(a):
    L=[0]*len(a)
    for k in range(len(a)):
        L[k]=1
        for j in range(0,k):
            if a[j]==a[k] and L[k]<2:
                L[k]+=1
                return a[k]

    return -1

print(first_duplicate([2, 4, 3, 5, 1]))