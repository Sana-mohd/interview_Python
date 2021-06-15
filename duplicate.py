list=["a","b","c","a","a","b","z","c","i"]
i=0
new=[]
without_duplicate=[]
while i<len(list):
    count=0
    if list[i] not in new:
        new.append(list[i])
        j=0
        while j<len(list):
            if list[i]==list[j]:
                count+=1
            j+=1
        element=list[i]+"="
        d=element+count
        # without_duplicate.append(element)
        without_duplicate.append(d)
    i+=1
print(without_duplicate)