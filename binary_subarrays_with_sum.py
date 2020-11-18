def num_sub_array(A):
    left_pointer=0
    right_pointer=0
    count=0
    for i  in range(len(A)):
        if right_pointer>=len(A):
            break
        if A[left_pointer]+A[right_pointer]==2:
            count+=1
            left_pointer+=1
            right_pointer+=1
        
        right_pointer+=1

    print(count)

num_sub_array([1,0,1,0,1])