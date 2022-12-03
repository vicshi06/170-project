#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Install packages
get_ipython().run_line_magic('pip', 'install networkx')
get_ipython().run_line_magic('pip', 'install numpy')
get_ipython().run_line_magic('pip', 'install tqdm')
get_ipython().run_line_magic('pip', 'install matplotlib')


# In[2]:


# The starter code is short and simple, take a look!
from starter import *
import networkx as nx
import random 


# # Phase 1 - Create Inputs


# In[4]:


# Add edges with G.add_edge(u, v, weight=w)
# Idea: consider making the inputs with a solution in mind, 
# such that you know the solution when the outputs are released

def small(G: nx.Graph):
    # TODO add edges to complete the small input
    # generate the nodes 
    for i in range(100):
        G.add_node(i)
        
    # randomly generate the number of edges and loop through the # of edges 
    num_edges = random.randint(0, 10000)
    new_range = 10000
    copy = num_edges 
    total = 0
   
    while total < 500000:
        for i in range(num_edges):
            u = random.randint(0, 99)
            v = random.randint(0, 99)
            while u == v: 
                v = random.randint(0, 99)
            w = random.randint(1, 1000)
            total += w
            G.add_edge(u, v, weight = w)
        new_range -= copy 
        num_edges = random.randint(0, new_range)
        copy = num_edges 
    print(total)
        
    # check to see if the sum meets the requirement 
    # add edge and randomly generate the vertices and weights 
        
    
def medium(G: nx.Graph):
    # TODO add edges to complete the medium input
    for i in range(300):
        G.add_node(i)
        
    # randomly generate the number of edges and loop through the # of edges 
    num_edges = random.randint(0, 10000)
    new_range = 10000
    copy = num_edges 
    total = 0
   
    while total < 500000:
        for i in range(num_edges):
            u = random.randint(0, 299)
            v = random.randint(0, 299)
            while u == v: 
                v = random.randint(0, 299)
            w = random.randint(1, 1000)
            total += w
            G.add_edge(u, v, weight = w)
        new_range -= copy 
        num_edges = random.randint(0, new_range)
        copy = num_edges 
    print(total)
    
def large(G: nx.Graph):
    # TODO add edges to complete the large input
    for i in range(1000):
        G.add_node(i)
        
    # randomly generate the number of edges and loop through the # of edges 
    num_edges = random.randint(0, 10000)
    new_range = 10000
    copy = num_edges 
    total = 0
   
    while total < 500000:
        for i in range(num_edges):
            u = random.randint(0, 999)
            v = random.randint(0, 999)
            while u == v: 
                v = random.randint(0, 999)
            w = random.randint(1, 1000)
            total += w
            G.add_edge(u, v, weight = w)
        new_range -= copy 
        num_edges = random.randint(0, new_range)
        copy = num_edges 
    print(total)


# In[5]:


G = nx.empty_graph(N_SMALL)
small(G)
write_input(G, 'small.in')

G = nx.empty_graph(N_MEDIUM)
medium(G)
write_input(G, 'medium.in')

G = nx.empty_graph(N_LARGE)
large(G)
write_input(G, 'large.in')


# # Phase 2 - Implement your Solver

# In[ ]:

    # Assign a team to v with G.nodes[v]['team'] = team_id
    # Access the team of v with team_id = G.nodes[v]['team']

    # group_num = 4 
    # nodes_per_group = len(G.nodes) // group_num

    # for i in range(group_num):
    #     for j in range(nodes_per_group):
    #         G.nodes[i*nodes_per_group + j]['team'] = i + 1
    
    # for i in range(len(G.nodes)):
    #     # get the biggest weight and the nodes within the nodes in a group
    #     max_weight = 0
    #     max_node = 0
    #     for j in range(len(G.nodes)):
    #         if G.nodes[j]['team'] == G.nodes[i]['team']:
    #             if G.has_edge(i, j):
    #                 if G[i][j]['weight'] > max_weight:
    #                     max_weight = G[i][j]['weight']
    #                     max_node = j
    #       # randomly switch the max_node with the node in other groups
    # G.nodes[max_node]['team'] = random.randint(1, group_num)
    
    # return G    



# In[30]:
def solve(G: nx.Graph):
    # TODO implement this function with your solver

    # greedy coloring algorithm keeping track the number of nodes in each group 

    # assign the first node to the first group
def first_available(color_list):
    """Return smallest non-negative integer not in the given list of colors."""
    color_set = set(color_list)
    count = 0
    while True:
        if count not in color_set:
            return count
        count += 1
        
def greedy_color(G, order):
    """Find the greedy coloring of G in the given order.
    The representation of G is assumed to be like https://www.python.org/doc/essays/graphs/
    in allowing neighbors of a node/vertex to be iterated over by "for w in G[node]".
    The return value is a dictionary mapping vertices to their colors."""
    color = dict()
    for node in order:
        used_neighbour_colors = [color[nbr] for nbr in G[node]
                                 if nbr in color]
        color[node] = first_available(used_neighbour_colors)
    return color



    


# In[31]:

# for i in range(1, 261):
#     path = 'inputs/small' + str(i) + '.in'
#     G = read_input(path)
#     solve(G)
#     print(score(G))

for i in range(1, 261):
    path = 'inputs/medium' + str(i) + '.in'
    G = read_input(path)
    solve(G)
    print(score(G))

# In[33]:


run(solve, 'medium.in', 'medium.out')


# In[ ]:


run_all(solve, 'inputs', 'outputs')
tar('output')


# %%
