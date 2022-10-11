import re
import string
str = open("E:\\test\\test.txt","r").read()
'''
\w match any alphanumeric char both uppercase and lower case and 0-9
.%+- - match any of these chars
[]  match anything contained in these brackets
+ as many times as possible
\. match the symbol, here it's full stop
{2,4} match atlease 2 times but no more than 4 times
refer: https://www.enjoyalgorithms.com/blog/regular-expressions-in-ml
'''
match = re.findall('[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,4}', str)
print(match)
