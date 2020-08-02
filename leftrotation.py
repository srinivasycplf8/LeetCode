arr=[1,2,3,4,5]

for i in range(0,4):
    arr.append(arr[0])
    arr=arr[1:6]

print(arr)