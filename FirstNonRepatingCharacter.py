def firstNotRepeatingCharacter(s):
    minimum=1000000
    for i in set(s):
        if s.count(i)==1:
            minimum=min(minimum,s.index(i))
            
    if minimum==1000000:
        return "_"
    
    return s[minimum]

def firstNotRepeatingCharacter(s):
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_'