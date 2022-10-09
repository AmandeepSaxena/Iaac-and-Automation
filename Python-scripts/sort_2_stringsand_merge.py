import string
str1="aman"
str2="deeps"
sorted(str1)
sorted(str2)
merged = []
i, j = 0,0
while i < len(str1) and j < len(str2):
    if str1[i] < str2[j]:
        merged.append(str1[i])
        i += 1
    else:
        merged.append(str2[j])
        j += 1
    
merged = merged + merged[i:] + merged[j:]

print("".join(merged))