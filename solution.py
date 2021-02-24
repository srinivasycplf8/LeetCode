#Programaing Assigenement 1 - Problem - 2

import time
start = time.time()
def merge_sort(given_length,given_array):
    n=len(given_array)
    if n<2:
        return 0
    mid=n//2
    left=given_array[0:mid]
    right=given_array[mid:n]
    a=merge_sort(given_length,left)
    b=merge_sort(given_length,right)
    S=merge_two_sorted_arrays(left,right,given_array)
    return S
    


def merge_two_sorted_arrays(left_array,right_array,original_array):
    pointer_left_array=0
    pointer_right_array=0
    total=len(left_array)+len(right_array)
    counter=0
    for i in range(total):
        if pointer_left_array<len(left_array) and pointer_right_array<len(right_array):
            if left_array[pointer_left_array]<=right_array[pointer_right_array]:
                original_array[i]=left_array[pointer_left_array]
                pointer_left_array+=1
            else:
                original_array[i]=right_array[pointer_right_array]
                pointer_right_array+=1
                counter+=1
        else:
            if pointer_left_array==len(left_array) and pointer_right_array!=len(right_array):
                original_array[i]=right_array[pointer_right_array]
                pointer_right_array+=1
                counter+=len(left_array)-pointer_left_array

            else:
                original_array[i]=left_array[pointer_left_array]
                pointer_left_array+=1
    return original_array

x=merge_sort(4,[9,6,8,4,44,2,3,1,22])
print(x)
time.sleep(1)

# program body ends

# end time
end = time.time()

# total time taken
print(f"Runtime of the program is {end - start}")