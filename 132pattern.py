def find132pattern(num):
    min_num=num[0]
    for j in range(0,len(num)-2):
        min_num=min(min_num,num[j])
        for k in range(j+1,len(num)-1):
            if min_num<num[k]<num[j]:
                return True
    
    return False


        

print(find132pattern([3,1,4,2]))
