# in here we call our nodes vertex
# the plural would be vertecies
# between the vertecies we have what we call an edge or connection

# there is not limit to how many vertices that a vertex can connect to
# now in graphs we can have multiple routes from a vetex to another one,
# buts most of the times we have weights for each edge (not always though)

# we have 2 types : 
# ones with arrows which we name them as directed graphs.
# ones without arros which we name them undirected (bidirectional) graphs.

# there is 2 way that we can represent graphs 
# 1 - Adjacency Matrix
# 2 - Adjacency List

# also remember trees are a form of graphs , but they have limitation of that each node can only point to two other nodes.




class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex, edges in self.adj_list.items():
            print(vertex,":",edges)
    
    def add_vertex(self,vertex):
        # we dont want to have duplicates in our graph
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self,v1,v2):
        # burada bir seyi kontrol etmemiz grekiyor
        # diyelim ki v1 ve v2 var ama biz v1 ve v3 arasinda bir baglanti yapmak istedik
        # bu durumda v3 olmadigina gore bu mantiksiz olacaktir
        all_keys = self.adj_list.keys()
        if v1 in all_keys and v2 in all_keys:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self,v1,v2):
        # tabiki genede once kontrol etmemiz gerekiyor
        all_keys = self.adj_list.keys()
        if v1 in all_keys and v2 in all_keys:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False 
    
    # bir vertexsi silebilmek icin once onunla baglantida olan butun vertex'lerin edge'lerini silmemiz gerekiyor
    def remove_vertex(self,vertex):
        all_keys = self.adj_list.keys()
        if vertex in all_keys:
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex) # 'D' : ['A','B','C']
            del self.adj_list[vertex]
            return True
        return False

        
# -----------------        

# my_graph = Graph()
# my_graph.add_vertex("A")
# my_graph.add_vertex("B")
# my_graph.add_vertex("C")


# my_graph.add_edge("A","B")
# my_graph.add_edge("B","C")
# my_graph.add_edge("C","A")


# my_graph.remove_edge("A","B")

# # my_graph.print_graph()
# my_graph.print_graph()



# ----------------- remove_vertex() -----------------


my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")


my_graph.add_edge("A","B")
my_graph.add_edge("A","C")
my_graph.add_edge("A","D")
my_graph.add_edge("B","D")
my_graph.add_edge("C","D")

my_graph.remove_vertex("D")

# my_graph.print_graph()
my_graph.print_graph()
