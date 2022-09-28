list = list(input('Enter numbers in a list: '))

s = len(list)
rev = [None]*s
for i in list:
    s = s-1
    rev[s] = i
print(rev)

