def firstDuplicate(a):
    counts=set()
    for i in a:
        if i in counts:
            return i
        counts.add(i)
    return -1


##Lists won't execute in long run ,while sets an counts