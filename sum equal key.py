newDict={"x":100,"y":-54,"z":247}
my_dict={"x":100,"k":5,"z":9}
key=list(newDict.keys())
key1=list(my_dict.keys())
i=0
sum=0
while i<len(newDict):
    if key[i]==key1[i]:
        sum=newDict[key[i]]+my_dict[key[i]]
        print(sum)
    i+=1