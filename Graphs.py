#Arrays of Edges (Directed) [start, end]

n=8  #number of nodes
#
A = [[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]] #these are the edges
#assume its start to end

# print(A) #array of edges

#Convert Array of Edges to Adjacency Matrix
M = []
for i in range(n):  #you want it to have n columns
    M.append([0] * n) #this makes each column have 8 rows from 0 to 7
    #you end up having a 7 by 7 matrix
#
#
print(M) #this makes the matrix
#
for u, v in A: #this means for every starting vertex(u) and ending vertex(v) in array of edges
    M[u][v] = 1 #the matrix will set it to 1,at row u & column v
#     #at row u and column v is 1 so means u is pointing to 1
#
#     #FOR UNDIRECTED - SPECIFY OPPOSITE CONNECTION TOO
#     M[v][u] = 1 #This type of array is called a symmetric matrix

# print(M)  #THIS makes adjacency matrix



#Convert Array of Edges -> Adjacency List
from collections import defaultdict
#
D = defaultdict(list)
print(D)
for u,v in A:  #u is the start, v is the end
    D[u].append(v) #the dictionary will add v (end node)
    #the dictionary should have a key of u, each of the values (end nodes) should be counted)
    #LOOK INTO THIS FURTHER

    #If undirected then each v would be joined to u so, add this line below
    #D[v].append(u)


print(D)
print(D[3]) #SAYS what it is connected to easily


#-----------------DFS With Recursion - O(V+E) Time complexity where V is nodes & E is the edges
# def dfs_recursive(node):
#     print(node) #this is how we will represent processing the node
#     for nei_node in D[node]:  # so at the specified source node (starting node)   - check if any list values associated to it - if so it has neighbouring nodes
#         if nei_node not in seen:   #if the neigh node exists AND isnt in the seen set
#             seen.add(nei_node)  # add neighbour node to the seen set
#             dfs_recursive(nei_node) # then we do the dfs on that node
#
# #
# #
# #
# source = 0 #start search at 0
# seen = set() #we have a set called seen
# seen.add(source) #we add the first node we are on to the seen list
# dfs_recursive(source) #we are starting at the source
# #


#Iterative DFS with Stack - T: O(V + E)

source = 0
seen = set()
seen.add(source)  #add the first node
stack = [source] # add the first node to the stack

while stack:
    node = stack.pop()  #pop from the stack (the last element)
    print(node) #this will print out the node (process it )
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            stack.append(nei_node)

    #if adds everything to the stack then prints - look at the order compared to DFS recursive

#BFS (Queue) - O(V + E)

source = 0 #define source node
from collections import deque

seen = set() #create a seen set
seen.add(source)
q = deque()
q.append(source) #added our first node to the queue

while q:
    node = q.popleft()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            q.append(nei_node)



#-------------------------------------------------------------------------------------------------


"""
Graphs In Practice
you can store graphs in memory via objects in classes

eg like Trees & Linked List
"""
class Node:
    def __init__(self, value):  #defined its value only for now, by default it has no neighbours
        self.value = value
        self.neighbours = []

    def __str__(self):  #how it prints itself
        return f'Node({self.value})'   #it will return its value if  printed

    def display(self):  #function that gets a variable called connections
        connections = [node.value for node in self.neighbours]  # each of the node values for a list of each of its neighbours, says that node is connected to its list of neighbours (connections)
        return f"{self.value} is connected to {connections}"

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")

A.neighbours.append(B)
B.neighbours.append(A)

C.neighbours.append(D)
D.neighbours.append(C)

B.display()
