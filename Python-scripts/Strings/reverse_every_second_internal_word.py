str = 'one two three four five six'
list=[]
l1 = str.split()
i = 0
while i < len(l1):
    if i%2==0:
        list.append(l1[i])
    else:
        list.append(l1[i][::-1])
    i = i + 1

print(list)
