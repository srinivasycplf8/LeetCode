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
        return S
    return S
    


def merge_two_sorted_arrays(left_array,right_array,original_array):
    pointer_left_array=0
    pointer_right_array=0
    total=len(left_array)+len(right_array)
    for i in range(total):
        if pointer_left_array<len(left_array) and pointer_right_array<len(right_array):
            if left_array[pointer_left_array][1]<=right_array[pointer_right_array][1]:
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

interval=int(input())
x=[]
for i in range(interval):
    interval_input=input()
    interval_input=interval_input.split(" ")
    intervals=[int(interval_input[0]),int(interval_input[1]),int(interval_input[2])]
    x.append(intervals)


'''def binary_search(A,k,a,b):

    m = (a+b)//2

    

    if b>=2 :

        if A[m][1]<=A[k][0]<=A[m+1][1]:
            return m

        if A[m][1]>=A[k][0]:
            return binary_search(A,k,a,m)
        if A[k][0]>A[m+1][1]:
            return binary_search(A,k,m+1,b)    
        
    if b==1:
        if A[m][1]<=A[k][0]:
            return m
        else:
            return 0'''



'''private int latestCompatible(int i){
		int low = 0, high = i - 1;

		while (low <= high){		//Iterative binary search
			int mid = (low + high) / 2;		//integer division (floor)
			if (jobs[mid][2] <= jobs[i][1]) {
				if (jobs[mid + 1][2] <= jobs[i][1])
					low = mid + 1;
				else
					return mid;
			}
			else
				high = mid - 1;
		}
		return 0;	//No compatible job was found. Return 0 so that value of placeholder job in jobs[0] can be used
	}'''
def binary_search(A,k):
    low=1
    high=k-1
    if high==1:
        mid = (low+high)//2
        if A[mid][1]<=A[k][0]:
            return mid
        else:
            return 0
    while low<=high:
        mid = (low+high)//2
        if A[mid][1]<=A[k][0]:
            if A[mid+1][1]<=A[k][0]:
                low=mid+1
            else:
                return mid
        else:
            high=mid-1
    
    return 0 
def weight_interval(interval,A):

    y = merge_sort(interval,A)
    y.insert(0,0)
    F = [0]*(interval+1)
    F[0] = 0
    pre=[0]*(interval+1)
    for k in range(1,len(y)):
        if k>1:
            pre[k]=binary_search(y,k)
        F[k]=max((y[k][2]+F[pre[k]]),F[k-1])

    print(max(F))
    #print(F[-1])


    


weight_interval(interval,x)
