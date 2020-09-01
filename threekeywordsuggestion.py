def threekey(repository,query):
    for i in repository:
        if  i.startswith(query,0,5):
            print(i)

print(threekey(["mi","mouse","mousepad","mou"],"mouse"))