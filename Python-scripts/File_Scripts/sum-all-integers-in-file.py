file = open("D:\\r@at\\fileexpl1.txt", 'r') # use double slash cause in windows reqd this
lines = file.readlines()
sum = 0 
for line in lines:
    for char in line:
        if char.isdigit() == True :
            sum += int(char)
print(f'total sum is: {sum}')            
