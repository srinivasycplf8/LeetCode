s="ababbcbakab"
words=["ab"]
for i in words:
    for k in range(len(s)):
        t=k
        if i==s[t:k+len(i)]:
            t=t+len(i)
            print("yes")
            pass
        else:
            break
