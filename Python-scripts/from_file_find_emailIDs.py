import re
string = open('D:\\r@at\\fileexpl1.txt','r').read()
'''
\w matches any aplhanumeric chars inlcuding underscore equivalent to [a-zA-Z0-9_]
+ - as many times as possible
{2,4} - try minimum 2 times max 4 times
'''
match = re.findall(r'[\w.+%]+@[\w.-]+\.[a-zA-Z0-9]{2,4}',string)
print(match)