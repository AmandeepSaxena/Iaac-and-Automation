def CamelCase(strings, pattern) : 
    map = dict.fromkeys(strings,None)  
    for i in range(len(strings)) :  
        s = ""  
        l = len(strings[i])  
        for j in range(l) :  
            if (strings[i][j] >= 'A' and strings[i][j] <= 'Z') : 
                s += strings[i][j]  
                  
                if s not in map : 
                    map[s] = [strings[i]] 
                      
                elif map[s] is None : 
                    map[s] = [strings[i]] 
                      
                else : 
                    map[s].append(strings[i])  
  
    wordFound = False   
    for key,value in map.items() :  
        if (key == pattern) : 
            wordFound = True  
            for itt in value : 
                print(itt)   
    if (not wordFound) : 
        print("No match found")  
if __name__ == "__main__" :  
  
    strings = [ 
        "Hi", "Hello", "HelloWorld",  
        "HiTech", "HiGeek", "HiTechWorld",  
        "HiTechCity", "HiTechLab"
    ]   
    pattern = "HT"   
    CamelCase(strings, pattern);

'''
map {

     {H, Hello},

     {HI, HelloWorld},

}
'''    