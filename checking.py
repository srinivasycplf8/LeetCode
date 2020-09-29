#Programaing Assigenement 1 - Problem - 2


def merge_sort(given_length,given_array):
    n=len(given_array)
    if n<2:
        return given_array
    mid=n//2
    left=given_array[0:mid]
    right=given_array[mid:n]
    x=merge_sort(given_length,left)
    y=merge_sort(given_length,right)
    S = merge_two_sorted_arrays(x,y)
    return S
    


def merge_two_sorted_arrays(left_array,right_array):
    pointer_left_array=0
    pointer_right_array=0
    original_array=[]
    total=len(left_array)+len(right_array)
    for i in range(total):
        if pointer_left_array<len(left_array) and pointer_right_array<len(right_array):
            if left_array[pointer_left_array]<=right_array[pointer_right_array]:
                original_array.append(left_array[pointer_left_array])
                pointer_left_array+=1
            else:
                original_array.append(right_array[pointer_right_array])
                pointer_right_array+=1
        else:
            if pointer_left_array==len(left_array) and pointer_right_array!=len(right_array):
                original_array.append(right_array[pointer_right_array])
                pointer_right_array+=1
            else:
                original_array.append(left_array[pointer_left_array])
                pointer_left_array+=1
            
    return original_array

x=merge_sort(8,[1,3,2,5,4,22,33,123,21,100,-2,-4,52,102])
print(x)

