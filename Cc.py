class Graph:
    def __init__(self,x,vertices) :
        self.reverse_graph={}
        self.reverse_visited={}
        self.pre_list={}
        self.post_list={}
        self.final_list=[]
        self.x=x
        self.vertices=vertices
        self.original_graph={}
        self.original_visited={}
        self.clock=0
        self.num_cc=0
    def reverse_function(self,x):
        reverse_graph={}
        for i in range(len(x)):
            if x[i][1]  in reverse_graph:
                reverse_graph[x[i][1]].append(x[i][0])
            else:
                reverse_graph.setdefault(x[i][1], [])
                reverse_graph[x[i][1]].append(x[i][0])

        return reverse_graph

    def explore(self,vertex):
        self.reverse_visited[vertex]=1
        self.pre_list[vertex]=self.clock
        self.clock+=1
        if vertex not in self.reverse_graph:
            self.post_list[vertex]=self.clock
            self.clock+=1
            self.final_list.append(vertex)
        else: 
            edge_list=self.reverse_graph[vertex]
            for i in range(len(edge_list)):
                if self.reverse_visited[edge_list[i]]==0:
                    self.explore(edge_list[i])
            self.post_list[vertex]=self.clock
            self.clock+=1
            self.final_list.append(vertex)

    def dfs_with_timing(self):
        self.reverse_graph=self.reverse_function(self.x) 
        self.reverse_visited={}
        for i in range(len(self.x)):
            for j in range(len(self.x[i])):
                if self.x[i][j] not in self.reverse_visited:
                    self.reverse_visited[self.x[i][j]]=0
        self.clock=1
        no_of_vertices=len(self.reverse_visited)
        #visited list with 0 
        vertices=list(self.reverse_visited.keys())
        self.pre_list=self.reverse_visited
        self.post_list=self.reverse_visited
        for i in range(len(vertices)):
            if self.reverse_visited[vertices[i]]==0:
                self.explore(vertices[i])
        self.final_list = self.final_list[::-1]
        return self.final_list
    
    def adjancey_matrix(self):
        for i in range(len(x)):
            if x[i][0] in self.original_graph:
                self.original_graph[x[i][0]].append(x[i][1])
            else:
                self.original_graph.setdefault(x[i][0],[])
                self.original_graph[x[i][0]].append(x[i][1])


    
    def explore_cc(self,vertex):
        if vertex not in self.original_graph:
            self.original_visited[vertex]=self.num_cc
 
        else:
            self.original_visited[vertex]=self.num_cc
            edge_list=self.original_graph[vertex]
            for edge in range(len(edge_list)):
                if self.original_visited[edge_list[edge]]==0:
                    self.explore_cc(edge_list[edge])
    
    
    def connected_components_dfs(self): 
        self.num_cc=0
        self.original_visited={}
        #visited list with 0 
        for i in range(len(self.x)):
            for j in range(len(self.x[i])):
                if self.x[i][j] not in self.original_visited:
                    self.original_visited[self.x[i][j]]=0


        for i in range(len(self.final_list)):
            if self.original_visited[self.final_list[i]]==0:
                self.num_cc+=1
                self.explore_cc(self.final_list[i])

        if len(self.original_visited)!=self.vertices:
            return self.num_cc+(self.vertices-len(self.original_visited))


        return self.num_cc







vert_edge=input()
vert_edge=vert_edge.split(" ")
vertices=int(vert_edge[0])
edges=int(vert_edge[1])
x=[]
for i in range(edges):
    adj_edge=input()
    adj_edge=adj_edge.split(" ")
    input_edges=[int(adj_edge[0]),int(adj_edge[1])]
    x.append(input_edges)


s=Graph(x,vertices)
s.dfs_with_timing()
s.adjancey_matrix()
print(s.connected_components_dfs())



    