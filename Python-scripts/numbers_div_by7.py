def divby7(list):
    print(f"Entered numbers are: {list}")
    for i in range(len(list)):
        if list[i] %7 == 0:
            print(f'{list[i]} is divisible by 7')
        else:
            print(f'{list[i]} is not divisible by 7')
list = []
num = input(f'Enter list to check the divisiblity: ')
print(num)
#now you have to convert this input in list
for i in range(len(num)):
    list.append(i)
print(divby7(list))

