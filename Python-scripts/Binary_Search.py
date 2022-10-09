#Searchin algorithms- Binary Search
def binarySearch(array,value):
    start = 0
    end = len(array) - 1
    middle = (start+end)//2
    print(start,end,middle)
    while not(array[middle] == value):
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = (start+end)//2
    return middle        

custArray = [4,5,7,9,18,47,9,27,57,16,6]
value = binarySearch(custArray,18)
if value: 
    print(f'Number found: {custArray[value]} at index: {value + 1}')