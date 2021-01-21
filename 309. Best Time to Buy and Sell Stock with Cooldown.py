def diagonal_sort(mat):
    row=len(mat)
    col = len(mat[0])
    new=[]
    value=[]

    for i in range(row):
      
        for j in range(col):
            min_element=mat[i][j]
            row_min_index=i
            col_min_index=j
            k=j
            row_index=i
            while k<3 and row_index<2:
                row_index+=1
                k+=1
                if mat[row_index][k]<min_element:
                    min_element= mat[row_index][k]
                    row_min_index=row_index
                    col_min_index=k
            print(row_min_index,col_min_index,min_element)
            new.append(min_element)
            mat[row_min_index][col_min_index]=float('inf')

        value.append([])
        value[0].append(new)
        new=[]


    x=[]

    for i in range(row):
        for j in range(col):
            if mat[i][j]!=float('inf'):
                x.append(mat[i][j])
    
    x.reverse()
    k=0
    for i in range(len(value)):
        if value[i]==[]:
            break
        for j in range(len(value[0])):
            if float(value[i][j])==float('inf'):
                value[i][j]=x[k]
                k+=1


    print(value)
    




    

diagonal_sort([[3,3,1,1],[2,2,1,2],[1,1,1,2]])


