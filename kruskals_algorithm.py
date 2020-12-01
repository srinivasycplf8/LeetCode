def merge_sort(given_length,given_array):
    n=len(given_array)
    if n<2:
        return
    mid=n//2
    left=given_array[0:mid]
    right=given_array[mid:n]
    merge_sort(given_length,left)
    merge_sort(given_length,right)
    S=merge_two_sorted_arrays(left,right,given_array)
    if len(S)==int(given_length):
        return S
    return S
    


def merge_two_sorted_arrays(left_array,right_array,original_array):
    pointer_left_array=0
    pointer_right_array=0
    total=len(left_array)+len(right_array)
    for i in range(total):
        if pointer_left_array<len(left_array) and pointer_right_array<len(right_array):
            if left_array[pointer_left_array][2]<=right_array[pointer_right_array][2]:
                original_array[i]=left_array[pointer_left_array]
                pointer_left_array+=1
            else:
                original_array[i]=right_array[pointer_right_array]
                pointer_right_array+=1
        else:
            if pointer_left_array==len(left_array) and pointer_right_array!=len(right_array):
                original_array[i]=right_array[pointer_right_array]
                pointer_right_array+=1
            else:
                original_array[i]=left_array[pointer_left_array]
                pointer_left_array+=1
            
    return original_array




class Node:
    def __init__(self,value):
        self.data=value
        self.parent=None
        self.height=0

class Disjoint :

    def __init__(self,vertices) :
        self.edge_list=[]
        self.i=0

    def make_set(self,x):
        value=Node(x)
        value.height=1
        value.parent=value
        self.edge_list.insert(self.i,value)
        self.i+=1

    def find(self,x):


        y=None

        for i in range(len(self.edge_list)):

            if x == self.edge_list[i].data:
               y = self.edge_list[i]
               break

        while y.parent!=y:
            y=y.parent
        
        return y
    
    def union(self,x,y):

        rx = self.find(x)
        ry = self.find(y)

        if rx==ry : 
            return
        
        elif (rx.height<ry.height):
            rx.parent=ry
        
        else : 

            ry.parent = rx
            rx.height +=1

        
'''for j in range(10):
    y.make_set(j+10)

for j in y.edge_list:
    print(j.data)'''





vert_edge=input()
vert_edge=vert_edge.split(" ")
vertices=int(vert_edge[0])
edges=int(vert_edge[1])
x=[]
for i in range(edges):
    adj_edge=input()
    adj_edge=adj_edge.split(" ")
    input_edges=[int(adj_edge[0]),int(adj_edge[1]),int(adj_edge[2])]
    x.append(input_edges)



def krushkal(graph,vertices,edges):
    #sort edges
    sorted_edges=merge_sort(edges,graph)
    print(sorted_edges)
    mst=[]
    cost=0
    y=Disjoint(vertices)
    for v in range(1,vertices+1):
        y.make_set(v)
    
    for edge in range(len(sorted_edges)):
        ru = y.find(sorted_edges[edge][0])
        rv = y.find(sorted_edges[edge][1])


        if ru!=rv:
            mst.append([sorted_edges[edge][0],sorted_edges[edge][1]])
            cost+=sorted_edges[edge][2]
            print(sorted_edges[edge])
            y.union(ru.data,rv.data)

    return cost

print(krushkal(x,vertices,edges))
