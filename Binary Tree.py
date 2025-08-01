#Binary Trees


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val) #only will return the nodes value

#The node we will use
"""
            1
        2       3
      4   5   10
"""

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

# above we have built the tree
#root of the tree is A

#print(A)  #this prints 1 which is the value of this node

#Recursive Pre Order Traversal (DFS) Time - O(n) - Space - 0(n)
#space is n because its a recursive call stack

def preorder(node):
    if not node: # meaning if we have null, this is the base case
        return #we return nothing if we have null
    #node,left,right

    print(node)
    preorder(node.left)
    preorder(node.right)

#preorder(A)

"""
Call Stack

    
A   A

"""

#Recursive In Order Traversal (DFS) Time - O(n) - Space - 0(n)
#space is n because its a recursive call stack

def in_order(node):
    if not node: # meaning if we have null, this is the base case
        return #we return nothing if we have null
    #left,node,right

    in_order(node.left)
    print(node)
    in_order(node.right)

in_order(A)


#Recursive In Order Traversal (DFS) Time - O(n) - Space - 0(n)
#space is n because its a recursive call stack

def post_order(node):
    if not node: # meaning if we have null, this is the base case
        return #we return nothing if we have null
    #left,node,right

    post_order(node.left)
    post_order(node.right)
    print(node)

post_order(A)


#Iterative Pre Order Traversal (DFS) Time: O(n) Space O(n)
#Iterative means not recursive, instead using functions

def pre_order_iterative(node):
    stk = [node]  #at first the root will go onto the stack, stack is LIFO / FILO
    while stk: #while we have a stack we want to pop from it and process it
        node = stk.pop() #processing the node at the top of the stack
        print(node) #processed it
        if node.right: stk.append(node.right)  #if not null then add the right child to stack
        if node.left: stk.append(node.left) # add left after so we process the left first , so we go down the left side

#1 2 4 5 3 10, gives pre order same as recursive
pre_order_iterative(A)
#note the order WILL matter with the if statements, all ways are pre order

#Level Order Traversal (BFS) Time: O(n) , Space O(n)
#need a queue
from collections import deque

def level_order(node):  #node is the root of the tree
    q = deque() # so we created an object that is a queue
    q.append(node) # we append the root to the q

    while q: # while the q exists
        node = q.popleft() #pop from the left because FIFO
        print(node)
        if node.left: q.append(node.left)  #SO THE LEFT GETS PROCESSED FIRST, THEN THE RIGHT WILL
        if node.right: q.append(node.right)

level_order(A)

#Check if a value exists (DFS) in a binary tree: O(n) , Space O(n)  can be done with BFS too

def search(node,target):
    if not node: #means if Null eg we have no node
        return False # we cant find it

    if node.val == target: #if node value you are on is == to the target
        return True #then return true

    #must find it on left or right
    return search(node.left, target) or search(node.right, target)

#Note Python does short-circuit evaluation so if a value if found in left sub tree then right sub tree is not processed
#only continues if condition not met

"""
        1
    2       3
  4  5    10
so we go from node 1 then search left or right, we do left first
so we look at 2 and 2 is not 5 so look at its left first then right
4 is not it but its left & right will return null
so we now look at the call for 5
5 is true 
so 2.left or 2.right will equal True as left returned False & right returned True 
so then 1.left which is 2 will return True to 1 so then we ignore 1.right
as Python is short circuit evaluation

"""

#Binary Search Trees we will look at now
"""Eg
        5
    1       8
 -1   3   7   9

"""
#BST bcos left to right subtrees are small to high

#setting up the BST
A2 = TreeNode(5)
B2 = TreeNode(1)
C2 = TreeNode(8)
D2 = TreeNode(-1)
E2 = TreeNode(3)
F2 = TreeNode(7)
G2 = TreeNode(9)

A2.left, A2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2
print("----------------------------------------------------")
print(A2)

#Can use same inorder traversal method for BST
print("----------------------------------------------------")
in_order(A2)  #so left, node, right

print("----------------------------------------------------")

#Searching BST in T-O(logn) Space - O(log n) assuming roughly balanced else its O(n)
def search_bst(node,target):
    if not node:
        return False
    if node.val == target:
        return True

    if target < node.val: return search_bst(node.left, target)
    else: return search_bst(node.right,target)

print(search_bst(A2,4))
#BST MUCH FASTER AS WE HALF SO LESS TIME & SPACE USED