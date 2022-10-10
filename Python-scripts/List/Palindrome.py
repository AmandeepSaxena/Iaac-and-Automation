'''
so concept here is to check the reverse of half of number and then match with starting half of original number
to get the last digit % 10
to get the second last digit / 10
1221% 10 = 1
122/20 = 2
reverse number = 1*10+2
after dividing the original number is 12 - so when org number < reverted number we can see we have reached the half of it

'''
def IsPalindrome(num):
    #edge case1 = negative numbers can't become palindrome: -123 minus ans 3 can't be same 
    if(num<0 or (num  % 10 == 0 and num !=0)):
        return False
    else:
        rev_num = 0
        while(num > rev_num):
            rev_num = (rev_num * 10) + num % 10
            num = num //10
    #edge case2: if odd number is there then middle number will be at same position so just get rid of it by /10    
        if num == rev_num or num == rev_num//10:
           return True  
val = IsPalindrome(12321)
print(val)