def matchingStrings(strings,queries):
    count={}
    for i in strings:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    res=[]
    for i in queries:
        if i in count:
            res.append(count[i])
        else:
            res.append(0)

    return res

        