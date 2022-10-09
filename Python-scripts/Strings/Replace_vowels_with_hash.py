string = 'Python got some Vowels'
k = '#'
vowels = 'aeiouAEIOU'
for char in vowels:
    string = string.replace(char, k)
print(string)