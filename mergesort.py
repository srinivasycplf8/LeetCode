def merge_sort(given_array):
    n=len(given_array)
    if n<2:
        return
    mid=n//2
    left=given_array[0:mid]
    right=given_array[mid:n]
    merge_sort(left)
    merge_sort(right)
    S=merge_two_sorted_arrays(left,right,given_array)   
    return S 


def merge_two_sorted_arrays(left_array,right_array,original_array):
    pointer_left_array=0
    pointer_right_array=0
    total=len(left_array)+len(right_array)
    for i in range(total):
        if pointer_left_array<len(left_array) and pointer_right_array<len(right_array):
            if left_array[pointer_left_array]<=right_array[pointer_right_array]:
                original_array[i]=left_array[pointer_left_array]
                pointer_left_array+=1
            else:
                original_array[i]=right_array[pointer_right_array]
                pointer_right_array+=1
        else:
            if pointer_left_array==len(left_array) and pointer_right_array!=len(right_array):
                original_array[i]=right_array[pointer_right_array]
                pointer_right_array+=1
            else:
                original_array[i]=left_array[pointer_left_array]
                pointer_left_array+=1
    return original_array

U=[1,4,8,9,7]
print(merge_sort(U))
