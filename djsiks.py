class PriorityQueue:
    def __init__(self,vertices):
        self.PQ=[0]*vertices
        self.n=0

    def empty(self):
        if self.n==0:
            return True
        else:
            return False

    def bubble_up(self,key):
        parent=key//2
        if self.PQ[parent][1]>self.PQ[key][1]:
            self.PQ[parent],self.PQ[key]=self.PQ[key],self.PQ[parent]
            self.bubble_up(parent)
    
    def insert(self,vertex,value):
        x=self.n
        self.n+=1
        self.PQ[x]=[vertex,value]
        self.bubble_up(x)

    def find_min(self):
        return self.PQ[0]

    
    def shift_down(self,index):
        left_child=2*index+1
        right_child=2*index+2
        if left_child>self.n:
            return
        if self.PQ[left_child][1]>self.PQ[right_child][1]:
            a=right_child
        else:
            a=left_child
        
        if self.PQ[index][1]>self.PQ[a][1]:
            self.PQ[index],self.PQ[a]=self.PQ[a],self.PQ[index]
            self.shift_down(a)

        
    def delete_min(self):
        self.PQ[0]=self.PQ[-1]
        self.n-=1
        if self.n==1:
            self.PQ.pop()
            return
        self.shift_down(0)
        self.PQ.pop()
    
    def decrease_key(self,vertice,new_distance):
        index=0
        for i in range(len(self.PQ)):
            if self.PQ[i][0]==vertice:
                index=i
                break
        
        self.PQ[index][1]=new_distance

        self.bubble_up(index)

'''x=PriorityQueue(5)
print(x.empty())
x.insert(0,4)
x.insert(1,2)
x.insert(2,5)
x.insert(3,1)
x.insert(4,3)
print(x.PQ)
print(x.find_min())
print(x.delete_min())
print(x.PQ)
print(x.delete_min())
print(x.PQ)
print(x.delete_min())
print(x.PQ)
print(x.delete_min())
print(x.PQ)'''

class Graph :
     
    def __init__(self,vertices,source,graph):
         self.distance=[float('inf')]*(vertices+1)
         self.vertices=vertices
         self.source=source
         self.original_graph=graph

    def dijikshtra(self):
        y=PriorityQueue(self.vertices)

        for i in range(self.vertices):
            y.insert(i+1,float('inf'))

        self.distance[self.source]=0

        y.decrease_key(self.source,0)

        while (len(y.PQ)!=0):
            v_next=y.find_min()
            y.delete_min()
            distance_v_next=self.distance[v_next[0]]
            if v_next[0] not in self.original_graph:
                pass
            else:
                for i in self.original_graph[v_next[0]]:
                    if self.distance[i[0]]> distance_v_next + i[1]:
                        self.distance[i[0]]=distance_v_next+i[1]
                        y.decrease_key(i[0],self.distance[i[0]])
            
        return self.distance




vert_edge=input()
vert_edge=vert_edge.split(" ")
vertices=int(vert_edge[0])
edges=int(vert_edge[1])
source=int(vert_edge[2])
x=[]
for i in range(edges):
    adj_edge=input()
    adj_edge=adj_edge.split(" ")
    input_edges=[int(adj_edge[0]),int(adj_edge[1]),int(adj_edge[2])]
    x.append(input_edges)

print(x)

original_graph={}

for i in range(len(x)):
    if x[i][0] in original_graph:
        original_graph[x[i][0]].append([x[i][1],x[i][2]])
    else:
        original_graph.setdefault(x[i][0],[])
        original_graph[x[i][0]].append([x[i][1],x[i][2]])

print(original_graph)

u=Graph(vertices,source,original_graph)
x=u.dijikshtra()
for i in range(1,len(x)):
    print(x[i])






