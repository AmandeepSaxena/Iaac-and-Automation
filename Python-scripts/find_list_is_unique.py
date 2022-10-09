list = [1,2,3,3]
seen = []
ctr =0 
for i in list:
    if i in seen:
        print(f'not unique')
        ctr = 0
    else:
        seen.append(i)
        ctr += 1
if ctr > 0:
    print(f'Unique')
    