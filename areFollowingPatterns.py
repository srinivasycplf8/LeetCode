def areFollowingPatterns(strings, patterns):
    new=[]
    if len(strings)!=len(patterns):
        return False
    if len(set(strings))!=len(set(patterns)):
        return False
    for i in range(len(strings)-1):
        if patterns[i]!=patterns[i+1]:
            if strings[i]!=strings[i+1]:
                new.append("yes")
        if patterns[i]==patterns[i+1]:
            if strings[i]==strings[i+1]:
                new.append("yes")   
                
    if len(new)==len(strings)-1:
        return True     
    else:
        return False
        

