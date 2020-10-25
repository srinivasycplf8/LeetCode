class bellman_ford_algo:
    def __init__(self,vertices,source,original_graph,reverse_graph) :
        self.source=source
        self.original_graph=original_graph
        self.reverse_graph=reverse_graph
        self.distance=[float('inf')]*(vertices+1)
        self.previous=[None]*vertices
        self.vertices=vertices
    

    def update(self,u,v,length_of_the_edge):
        if (self.distance[u]+length_of_the_edge<self.distance[v]):
            self.distance[v]=self.distance[u]+length_of_the_edge
            #self.previous[v]=u


    def bellmanford_algorithm(self):
        self.distance[self.source]=0
        x=[0]*len(self.distance)
        for k in range(len(self.distance)):
            for v in range(1,self.vertices+1):
                if v not in self.reverse_graph:
                    pass
                else:
                    for i in self.reverse_graph[v]:
                        self.update(i[0],v,i[1])

            if k==len(self.distance)-2:
                x=self.distance[:]
            else:
                pass

        if x==self.distance:
            return False
        else:
            return True





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


original_graph={}

for i in range(len(x)):
    if x[i][0] in original_graph:
        original_graph[x[i][0]].append([x[i][1],x[i][2]])
    else:
        original_graph.setdefault(x[i][0],[])
        original_graph[x[i][0]].append([x[i][1],x[i][2]])


reverse_graph={}
for i in range(len(x)):
    if x[i][1]  in reverse_graph:
        reverse_graph[x[i][1]].append([x[i][0],x[i][2]])
    else:
        reverse_graph.setdefault(x[i][1], [])
        reverse_graph[x[i][1]].append([x[i][0],x[i][2]])


y=bellman_ford_algo(vertices,source,original_graph,reverse_graph)
print(y.bellmanford_algorithm())


    
