def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    for i in range((days)):
        temp=list(states)
        if 0!=states[1]:
            temp[0]=1
        else:
            temp[0]=0
        for i in range(1,len(states)-1):
            
            if states[i-1]==states[i+1]:
                temp[i]=0
            elif states[i-1]!=states[i+1]:
                temp[i]=1
        if 0!=states[len(states)-2]:
            temp[len(states)-1]=1
        else:
            temp[len(states)-1]=0
        states=temp
    return states
print(cellCompete([1,1,1,0,1,1,1,1],2))