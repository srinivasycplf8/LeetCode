def rotateImage(a):
    rows=len(a)
    temp=[]
    t=0
    for i in range(rows):
        k=len(a)-1
        temp.append([])
        for  j in range(rows):
            temp[i].append(a[k][t])
            k=k-1
        t=t+1   
    return temp

def rotateImage(a):
    return list(zip(*reversed(a)))

print(rotateImage([[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]))