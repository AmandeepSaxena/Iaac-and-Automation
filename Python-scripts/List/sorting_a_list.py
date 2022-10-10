list = [4,0,9,3,9,7,1,0,5]
i,j = 0,0
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print(list) 