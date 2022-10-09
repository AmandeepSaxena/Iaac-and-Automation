str = input("Enter string to reverse: ")
reverse = ''
i = len(str) - 1
while i >= 0:
    reverse = reverse + str[i]
    i = i - 1 
print(f'reverse is {reverse}')

'''
2nd solution
str = input("Enter string to reverse: ")
#using slicing [begining:end:increment/decrement of step]
reverseStr = str[::-1]
print(f'reverse if {reverseStr}')

3rd Solution
reverseStr = reversed(str)
ouput = ''.join(reverseStr)

'''

