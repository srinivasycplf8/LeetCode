#commit ammend
def search_from_middle(s,left,right):

    storage={}

    while (left>=0 and right<len(s) and s[left]==s[right]):
        left=left-1
        right=right+1
    storage["length"]=right-left-1
    storage["left"]=left+1
    storage["right"]=right-1

    return storage

def palindromic_long_String(s):

    longest=[0,0,0]

    for i in range(len(s)):
        #this case for "racEcar"
        storage1=search_from_middle(s,i,i)
        #this case for cvpabbapko
        storage2=search_from_middle(s,i,i+1)
        if storage1["length"]>storage2["length"]:
            if storage1["length"]>longest[0]:
                longest[0]=storage1["length"]
                longest[1]=storage1["left"]
                longest[2]=storage1["right"]
                
        else:
            if storage2["length"]>longest[0]:
                longest[0]=storage2["length"]
                longest[1]=storage2["left"]
                longest[2]=storage2["right"]
      
    return s[longest[1]:longest[2]+1]

x = input()

print(len(palindromic_long_String(x)))
