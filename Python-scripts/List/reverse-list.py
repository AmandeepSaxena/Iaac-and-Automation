# reversing list using slicing tenchinique
def rev_list(olist):
    list =[]
    list = olist[::-1]
    return(list)

olist = list(input('Enter numbers in a list: '))
print(rev_list(olist))