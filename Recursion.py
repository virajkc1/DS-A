#Fibonacci Sequence
# F(0) = 0
# F(1) = 1
# n > 1, F(n) = F(n-1) + F(n-2)

#make a recursive function

#Time is O(2^n) - Space of O(n) as if F(4) then you hold values of F( 3, 2, 1, 0)
def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)

#print(F(4))
#return F(3) + F(2)
#F(3) breaks down to F(2) + F(1)
#F(2) is F(1) + F(0) = 1
#F(3) = 1 + F(1) = 2

#ALREADY CALCULATED F(2) BUT
#F(2) = F(1) + F(0) = 1
#F(4) = 2 + 1
#=3

#print(F(100)) this would have to call the function F 2**100 times

#Linked Lists are recursive eg example of Single Linked List (double is recursive too)


class singlyNode: #you need a class that makes a node
    def __init__(self, val, next=None): #this is the constructor to make the node
        self.value = val #sets a value = to the value passed in
        self.next = next

    def __str__(self): #this function is used to return a string
        return str(self.value) #returns conversion of self.value into a string

Head = singlyNode(1) #we have defined all our Class Node objects here with there values
A = singlyNode(3)
B = singlyNode(4)
C = singlyNode(7)
#Nodes are 1->3->4->7

Head.next = A #defining the attributes, we set each next to a Node
A.next = B
B.next = C

#Linked Lists
#Time complexity (O(n) where n is the number of nodes in the linked list, Space (O(n))
def reverse(node):
    if not node:  #if we call None (no node)
        #at end of list
        return

    #if we have nodes
    reverse(node.next)
    print(node)

reverse(Head)
"""
So first we have our linked list 1->3->4->7->None
pass thru the head first 
if the head node doesnt not exist then we would return it BUT head exists
so 
we call the reverse onto the next node (3)
3 exists so we call 4, 4 exists so we pass thru 7

Call Stack
Top - Happens first                                   reverse(None) return(None)   
                                            reverse(7)  reverse(7)  reverse(7)  print(7)  
                                reverse(4)  reverse(4)  reverse(4)  reverse(4)  reverse(4)  print(4)  
                    reverse(3)  reverse(3)  reverse(3)  reverse(3)  reverse(3)  reverse(3)  reverse(3)  print(3)  
        reverse(1)  reverse(1)  reverse(1)  reverse(1)  reverse(1)  reverse(1)  reverse(1)  reverse(1)  reverse(1)  print(1) 
        
Bottom processed last - FILO

you return none, then that function call is over so we would print node B (7) then 
"""
