reverse = 0
number = int(input("Enter number to reverse: "))
while (number>0): 
    remainder = number % 10
    reverse = (reverse * 10 ) + remainder
    number = number // 10 

print(f'reverse of number is {reverse}')
