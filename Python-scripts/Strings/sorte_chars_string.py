#sort chars followed by integers
from unicodedata import digit


str = 'mynameis7890934'
alpha = []
digits = []
newstr = str.split()
i = 0
for ch in str:
    if ch.isalpha():
        alpha.append(ch)
    else:
        digits.append(ch)
newstr = "".join(sorted(alpha)+sorted(digits))
print(f'Sorted string: {newstr}')