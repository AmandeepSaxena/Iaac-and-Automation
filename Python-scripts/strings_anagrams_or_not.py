def check_anagram(s1,s2):

#for sorting either we can use sorted() func or below ninja tech, I refered GFG
    x = [s1[i] for i in range(0,len(s1))]
    x.sort()
    y = [s1[i] for i in range(0,len(s1))]
    y.sort()
    if x==y: 
        print(f"Strings are anagrams")
    else:
        print("strings are not anagrams")

check_anagram("aman","manaman")        
