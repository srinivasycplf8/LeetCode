def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1

        #the reason j helps to see whether it has previous value

        #check the conditions when j >=0 and check wether swapping is necessary

        while j>=0 and key<arr[j]:
            #so if the conditon satisifies then  replace with the elenment

            # don;t wortty the element which we are swaaping

            #the key will have the original valueee

            arr[j+1]=arr[j]
            #the reason j-=1 it will check all the elemnents which we swapped "i mean all the left values of ittt"
            j-=1
         
        arr[j+1]=key
    
    return arr
print(insertionsort([12, 11, 13, 5, 6]))
