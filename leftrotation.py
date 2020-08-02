def leftrotate(a,d):
    initial_length=len(a)
    i=0
    if d>len(a):
        d=d%len(a)
    a=a[d:len(a)]+a[0:d]
    return a