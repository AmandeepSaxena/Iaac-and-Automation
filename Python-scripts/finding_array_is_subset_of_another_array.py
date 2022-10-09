def findsubs():
    x = [4,5,6,7,3,2,34,9,56,32,15,46]
    y = [3,4,5,9,1]
    X = x.sort()
    print(X)
    i,k = 0,0
    for i in range(0, len(X)):
        k = binarySearch(X,0,len(X),y[i])
        print(k)
        if (k == -1):
            print("Sub array not exists")
            return False

    print("Sub array exists")
    return True

def binarySearch(array,left,right,value):
    i =0
    while (left<=right):
        mid = (left + right )//2
        if(array[mid] == value):
            print(array[mid])
            return mid
        if (value < array[mid]):
            right = mid -1
        else:
            left = mid + 1
    return -1        

findsubs ()
