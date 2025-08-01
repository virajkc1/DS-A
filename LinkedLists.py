#Singly Linked Lists

#the class takes 2 values in, value is the value that the node holds
# next is the next node its joined to & by default we set to none

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

#to join the nodes up

Head.next = A #defining the attributes, we set each next to a Node
A.next = B
B.next = C
#Note - C.next will be None as its at the end so you dont have to worry about it


#print(Head) #node object called Head is converted into a string & its given explicit rule to only return the string value hence you dont get the memory location
#if you remove __str__ function then if u printed the Head, you would only get the Head memory location
#print(repr(Head)) #or printing this with str function will show u the memory location instead
#note that the memory location is default when an object is printed unless a string representation function of the object is used


#Traverse the list - O(n)
curr = Head #curr is the variable name given to a pointer & set it to traverse from the Head
#curr will store the Head object hence curr is an object

while curr: #this checks if the current node exists or not, if it doesnt then curr = None
    print(curr) #this prints the current node ( its value) #value is the only thing that is returned from that function remmeber
    curr = curr.next #you have a current node, it contains the memory address of next node, so curr assigns itself to that node


#Displaying Linked List - T O(n) - Traversing through it

def display(head):  #takes the head of the list
    curr = head
    elements = [] #dynamic array with the elements =, (node values)
    while curr:
        elements.append(str(curr.value)) #adds the current value to the string
        curr = curr.next #moves to the next element
    print(" -> ".join(elements)) #join connects a list of strings into 1 string but the arrow is the string that sticks between them

#Eg
#["a","b","c"]  with .join(elements)
#the result is "abc"
#& with the " -> "
#this will make
# "a -> b -> c"

display(Head) #passes Head through the function & makes it pretty

#Search for node value - O(n)
def search(head, val):
    curr = head # so define the current node at the head
    while curr: #while current node exists
        if val ==  curr.value: #if value u searching through is == to current node value
            return True #return true
        curr = curr.next # else move to the next node
    return False #if you have searched through all the nodes values then value not there so return False

#to search for it
print(search(Head, 0))  # can check, this

#the reason return True or return False, not shown on console is because the caller ( caller is the search(Head, 0) bit), holds that value only unless instructed to print to console

#--------------------------------------------------------------------------------

# Doubly Linked List

class DoublyNode: #only 1 item so the head and tail are the same thing
    def __init__(self, val,next=None,prev=None):
# so the constructor has both next & prev values set to None
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

head = tail = DoublyNode(1) #
#the above is a bit complex
#basically you make 1 node object right now
#and you define the head & tail variables at that node

# print(head) #both have same values
# print(tail)

#Displaying a doubly linked list - O(n) time
def display_2(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" <-> ".join(elements))

display_2(head) #just 1 node right now


#Want a function that adds a new head

#At this point we just have 1 node, defined as head & tail
#now want to add a new head so we have a separate head node & tail node

#this is O(1) time
def insert_at_beginning(head,tail,val): #pass thru the existing head & tail node(its the same node) then the value of the new node
    new_node = DoublyNode(val,next=head) #call the the new node function & look at the variables it needed, val & the new head will join next to the old head so define that, tail is None as we just adding a new head in so
    #note the order will be ( new head <-> old head <-> tail
    head.prev = new_node #assigns the old heads previous to the new_node (before it was None)
    return new_node, tail #returns the new_node (value as str represenation) & the old tail node separately as they are now separate

head, tail = insert_at_beginning(head, tail, 3) #pass thru old head, old tail & new node value
# head & tail given same node at start but  now head is = to new head & tail is new tail

#you actually dont need tail in return or new variable assignment on l120, think why?

display_2(head)

def insert_at_end(head,tail,val): #pass thru the existing head & tail node(its the same node) then the value of the new node
    new_node = DoublyNode(val,prev=tail) #new tail has previous set to old tail & its next is None

    tail.next = new_node #existing tail next is now your new node
    return head, new_node

head, tail = insert_at_end(head, tail, 2) #pass thru old head, old tail & new node value
# head & tail given same node at start but  now head is = to new head & tail is new tail

#you actually dont need tail in return or new variable assignment on l120, think why?

display_2(head) #note we input the head so the display function reads thru & displays  all the nodes