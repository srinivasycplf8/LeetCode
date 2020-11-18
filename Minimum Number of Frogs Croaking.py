def minNumberOfFrogs(croakoffrogs):
    counts={'c':1,'r':2,'o':3,'a':4,'k':5}
    for i in range(len(croakoffrogs)):
        if croakoffrogs[i] in counts:
            if i<len(croakoffrogs)-1:
                if counts[croakoffrogs[i]]+1==counts[croakoffrogs[i+1]]:
                    print("true")

        else:
            return "hel"

minNumberOfFrogs("croakcrook")
