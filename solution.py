#Programaing Assigenement 1 - Problem - 2


def merge_sort(given_length,given_array):
    n=len(given_array)
    if n<2:
        return
    mid=n//2
    left=given_array[0:mid]
    right=given_array[mid:n]
    merge_sort(given_length,left)
    merge_sort(given_length,right)
    S=merge_two_sorted_arrays(left,right,given_array)
    if len(S)==int(given_length):
        S=' '.join(map(str,S)) 
        return S
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

input_length=input()
input_array=input()
input_array=list(map(int,input_array.split(" ")))
x=merge_sort(input_length,input_array)
print(x)