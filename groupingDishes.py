def groupingDishes(dishes):
    counts={}
    for i in range(len(dishes)):
        for j in range(1,len(dishes[i])): 
                if dishes[i][j] not in counts:
                    counts[dishes[i][j]]=[dishes[i][0]]
                else:
                     counts[dishes[i][j]].append(dishes[i][0])
    dictList=[]
    for i in sorted(counts):
        if len(counts[i])>=2:
            dictList.append([i]+sorted(counts[i]))
    
    return dictList
print(groupingDishes([["Salad","Tomato","Cucumber","Salad","Sauce"], 
 ["Pizza","Tomato","Sausage","Sauce","Dough"], 
 ["Quesadilla","Chicken","Cheese","Sauce"], 
 ["Sandwich","Salad","Bread","Tomato","Cheese"]]))
                




