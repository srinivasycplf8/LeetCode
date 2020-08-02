def hourglassSum(arr):
    rows=len(arr)
    columns=len(arr[0])
    hour_sum=0
    #-9 * 7 =-63
    min_sum=-63

    for i in range(0,rows-2):
        for j in range(0,columns-2):
            hour_sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            min_sum=max(hour_sum,min_sum)

    return min_sum

