string = 'Python is not difficult'
#lets convert string into list with split
list = string.split("")
reverse = list[::-1]
#now join back to string using join, make sure to use space
str = " ".join(reverse)
print(f'Reverse order of words is: {str}')