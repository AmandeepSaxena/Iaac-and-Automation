#problem description: https://leetcode.com/problems/break-a-palindrome
#using greedy optimizations we will divide the string and just work on first
#half of it


def breakPalindrome(palindrome):
    palindrome =  list(palindrome)
    strlen = len(palindrome)
    if strlen == "1":
        return ""
    for i in range(strlen//2):
        if palindrome[i] != 'a':
            palindrome[i] = 'a'
            return palindrome
    #if first letter of string is a and complete string is like aaaa then replace last of it with 'b'
    palindrome[strlen - 1] ='b'
    return palindrome    
print("".join(breakPalindrome('evnve')))