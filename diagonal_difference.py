def diagonaldifference(arr):
    diagonal1=0
    for i in range(len(arr)):
        diagonal1+=arr[i][i]
    
    diagonal2=0
    start=0
    end=0

    for j in range(len(arr)):
        diagonal2+=arr[start][end+3]
        start=start+1
        end=end-1
    
    if diagonal2>diagonal1:
        return diagonal2-diagonal1
    else:
        return diagonal1-diagonal2




