import time
start = time.time()

def sorteds_s(A):
    initialize=[None]*45
    for i in range(len(A)):
        initialize[A[i]]=A[i]
    
    
    a=[]
    for i in range(len(initialize)):
        if initialize[i]!=None:
            a.append(initialize[i])
            
    return a

print(sorteds_s([9,6,8,4,44,2,3,1,22]))
time.sleep(1)

# program body ends

# end time
end = time.time()

# total time taken
print(f"Runtime of the program is {end - start}")