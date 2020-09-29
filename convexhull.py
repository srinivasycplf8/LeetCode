import math
from math import atan2,pi

def polar_angle(po,pivot):
    y1=po[1]
    y2=pivot[1]
    x1=po[0]
    x2=pivot[0]
    y_span=(y1)-(y2)
    x_span=(x1)-(x2)
    if x_span==0:
        return (math.pi)/2
    
    return math.atan2(y_span,x_span)


def merge_sort(given_length,given_array,pivot):
    n=len(given_array)
    if n<2:
        return 0
    mid=n//2
    left=given_array[0:mid]
    right=given_array[mid:n]
    merge_sort(given_length,left,pivot)
    merge_sort(given_length,right,pivot)
    S=merge_two_sorted_arrays(left,right,given_array,pivot)
    if len(S)==int(given_length):
        return S
    return S

def merge_two_sorted_arrays(left_array,right_array,original_array,pivot):
    pointer_left_array=0
    pointer_right_array=0
    total=len(left_array)+len(right_array)
    for i in range(total):
        if pointer_left_array<len(left_array) and pointer_right_array<len(right_array):
            if polar_angle(left_array[pointer_left_array],pivot)<=polar_angle(right_array[pointer_right_array],pivot):
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

def orientation(pa,pb,pk):
    xa = pa[0]-pb[0]
    ya = pa[1]-pb[1]
    xb = pk[0]-pa[0]
    yb = pk[1]-pa[1]
    result = xa*yb - xb*ya
    if result==0:
        return 0
    return result

def Graham_scan(x):
    stack=[]
    if len(x)<3:
        return
    stack.append(x[0])
    stack.append(x[1])
    stack.append(x[2])

    for k in range(4,len(x)):
        pk=x[k]
        while stack!=[]:
            pa=stack[-1]
            pb=stack[-2]
            result=orientation(pa,pb,pk)
            if result<=0:
                stack.pop()        
            else:
                break
        stack.append(pk)
                
    return stack


def convex_hull(p):
    minimum_element=p[0][1]
    minimum_index=0
    for i in range(len(p)):
        if p[i][1]<minimum_element:
            minimum_element=p[i][1]
            minimum_index=i
    
    pivot=p[minimum_index]
    p.remove(pivot)
    x=merge_sort(len(p),p,pivot)
    x.insert(0,pivot)
    y=Graham_scan(x)
    return y
def envelope(x):
    minimum_x=float('inf')
    minimum_index=0
    maximum_index=0
    for i in range(len(x)):
        if x[i][0]<minimum_x:
            minimum_x=x[i][0]
            minimum_index=i
    maximum_x=-float('inf')
    for i in range(len(x)):
        if x[i][0]>maximum_x:
            maximum_x=x[i][0]
            maximum_index=i
    upper_convex=0
    lower_convex=0
    if minimum_index<=maximum_index:
        upper_convex=maximum_index-minimum_index+1
        new_list=x[maximum_index:len(x)]+x[0:minimum_index+1]
        lower_convex=len(new_list)
    if minimum_index>=maximum_index:
        lower_convex=minimum_index-maximum_index+1
        new_list=x[minimum_index:len(x)]+x[0:maximum_index+1]
        upper_convex=len(new_list)
    return upper_convex,lower_convex

#x=convex_hull([[-3,-10],[-1,-8],[-0.5,1],[0.5,-1], [0.5,2], [0,5],[ 1,5]])
#y=convex_hull([[-3.4,2.15],[3.74,7.94],[-1.94,1.82],[0.82,-2.16],[0.43,9.54],[0.62,-7.27],[1.06,6.12],[-4.99,-3.86],[-0.22,-0.66],[-3.55,-6.51]])
n=int(input())
new=[]
for i in range(n):
    co_ordinates=input()
    input_cordinates=list(map(float,co_ordinates.split(" ")))
    input_cordinates[1]=-input_cordinates[1]
    new.append(input_cordinates)

x=convex_hull(new)
y=envelope(x)
print(y[0],"",y[1])
    

