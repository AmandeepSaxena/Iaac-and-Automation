class Node:

    #function to initialize the node object
    def __init__(self,data):
        self.data = data  #Assign data
        self.next = None  #Initialize
        # next as null
#linked list class 

class LinkedList:

    #function to initialize the linked list
    #list object
    def __init__ (self):
        self.head = None 

    #to print linked list data
    def printlist(self): 
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


#code execution starts here
if __name__ == '__main__':

    #start with empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    #three nodes have been created
    llist.head.next = second
    second.next = third

    #call printing func
    llist.printlist()