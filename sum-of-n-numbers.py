def return_sum():
    amount_of_numbers = int (input("How many numbers : "))
    sum = 0
    while amount_of_numbers !=0:
        num = int(input ("Enter a number to add: "))
        sum += num
        amount_of_numbers -=1
    print(f'total sum is: {sum}')
    return sum    
return_sum () 