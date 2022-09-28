from asyncore import read
import random
lines = open("D:\\r@at\\fileexpl1.txt").read().splitlines()
myline = random.choice(lines)
print(myline)