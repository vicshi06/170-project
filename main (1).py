# In[1]: 

# Install packages
get_ipython().run_line_magic('pip', 'install networkx')
get_ipython().run_line_magic('pip', 'install numpy')
get_ipython().run_line_magic('pip', 'install tqdm')
get_ipython().run_line_magic('pip', 'install matplotlib')


# In[2]:


# The starter code is short and simple, take a look!
from starter import *
import random 


# In[3]:

def solve(G: nx.Graph):
    # TODO implement this function with your solver
    # Assign a team to v with G.nodes[v]['team'] = team_id
    # Access the team of v with team_id = G.nodes[v]['team']

    list = [n for n in range(0, 300)]
    color, teams = greedy_color(G, list)

def first_available(color_list):
    """Return smallest non-negative integer not in the given list of colors."""
    color_set = set(color_list)
    count = 1
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
    teams = dict()
    for node in order:
        used_neighbour_colors = [color[nbr] for nbr in G[node]
                                 if nbr in color]
        color[node] = first_available(used_neighbour_colors)
        G.nodes[node]['team'] = color[node]
        if color[node] not in teams:
            teams[color[node]] = []
        teams[color[node]].append(node)


    # gets the smallest weight that are coming into the first group 

    # for node in teams[1]:
    #         for nbr in teams[2]:
    #             if G.has_edge(node, nbr):
    #                 if G[node][nbr]['weight'] < smallest:
    #                         smallest = G[node][nbr]['weight']
    #                         smallest_nbr = nbr
   

    while len(teams[1]) < 60:
        smallest = 1000
        for node in teams[1]:
            for nbr in range(len(G.nodes)):
                if G.nodes[nbr]['team'] != G.nodes[node]['team'] and G.has_edge(node, nbr):
                    if G[node][nbr]['weight'] < smallest:
                        smallest = G[node][nbr]['weight']
                        smallest_nbr = nbr

                        
        # if smallest == 1000:
        #     next_team += 1
        #     print("next team")
        # print(smallest_node, smallest_nbr)
        # print(G.nodes[smallest_nbr]['team'])

        
        # add the smallest node to the first group 
        # delete the smallest node's neighbor from its original group
        
        if smallest_nbr not in teams[1]:
            teams[1].append(smallest_nbr)
        if smallest_nbr in teams[color[smallest_nbr]]:
            teams[color[smallest_nbr]].remove(smallest_nbr)
        
        G.nodes[smallest_nbr]['team'] = 1

    while len(teams[2]) < 60:
        smallest = 1000
        for node in teams[2]:
            for nbr in range(len(G.nodes)):
                if G.nodes[nbr]['team'] != G.nodes[node]['team'] and G.has_edge(node, nbr) and nbr not in teams[1]:
                    if G[node][nbr]['weight'] < smallest:
                        smallest = G[node][nbr]['weight']
                        smallest_nbr = nbr

                        
        # if smallest == 1000:
        #     next_team += 1
        #     print("next team")
        # print(smallest_node, smallest_nbr)
        # print(G.nodes[smallest_nbr]['team'])

        
        # add the smallest node to the first group 
        # delete the smallest node's neighbor from its original group
        
        if smallest_nbr not in teams[2]:
            teams[2].append(smallest_nbr)
        if smallest_nbr in teams[color[smallest_nbr]]:
            teams[color[smallest_nbr]].remove(smallest_nbr)
        
        G.nodes[smallest_nbr]['team'] = 2
    
    while len(teams[3]) < 60:
        smallest = 1000
        for node in teams[3]:
            for nbr in range(len(G.nodes)):
                if G.nodes[nbr]['team'] != G.nodes[node]['team'] and G.has_edge(node, nbr) and nbr not in teams[1] and nbr not in teams[2]:
                    if G[node][nbr]['weight'] < smallest:
                        smallest = G[node][nbr]['weight']
                        smallest_nbr = nbr

                        
        # if smallest == 1000:
        #     next_team += 1
        #     print("next team")
        # print(smallest_node, smallest_nbr)
        # print(G.nodes[smallest_nbr]['team'])

        
        # add the smallest node to the first group 
        # delete the smallest node's neighbor from its original group
        
        if smallest_nbr not in teams[3]:
            teams[3].append(smallest_nbr)
        if smallest_nbr in teams[color[smallest_nbr]]:
            teams[color[smallest_nbr]].remove(smallest_nbr)
        
        G.nodes[smallest_nbr]['team'] = 3
    
    while len(teams[4]) < 60:
        smallest = 1000
        for node in teams[4]:
            for nbr in range(len(G.nodes)):
                if G.nodes[nbr]['team'] != G.nodes[node]['team'] and G.has_edge(node, nbr) and nbr not in teams[1] and nbr not in teams[2] and nbr not in teams[3]:
                    if G[node][nbr]['weight'] < smallest:
                        smallest = G[node][nbr]['weight']
                        smallest_nbr = nbr

                        
        # if smallest == 1000:
        #     next_team += 1
        #     print("next team")
        # print(smallest_node, smallest_nbr)
        # print(G.nodes[smallest_nbr]['team'])

        
        # add the smallest node to the first group 
        # delete the smallest node's neighbor from its original group
        
        if smallest_nbr not in teams[4]:
            teams[4].append(smallest_nbr)
        if smallest_nbr in teams[color[smallest_nbr]]:
            teams[color[smallest_nbr]].remove(smallest_nbr)
        
        G.nodes[smallest_nbr]['team'] = 4

    while len(teams[5]) < 60:
        smallest = 1000
        for node in teams[5]:
            for nbr in range(len(G.nodes)):
                if G.nodes[nbr]['team'] != G.nodes[node]['team'] and G.has_edge(node, nbr) and nbr not in teams[1] and nbr not in teams[2] and nbr not in teams[3] and nbr not in teams[4]:
                    if G[node][nbr]['weight'] < smallest:
                        smallest = G[node][nbr]['weight']
                        smallest_nbr = nbr

                        
        # if smallest == 1000:
        #     next_team += 1
        #     print("next team")
        # print(smallest_node, smallest_nbr)
        # print(G.nodes[smallest_nbr]['team'])

        
        # add the smallest node to the first group 
        # delete the smallest node's neighbor from its original group
        
        if smallest_nbr not in teams[5]:
            teams[5].append(smallest_nbr)
        if smallest_nbr in teams[color[smallest_nbr]]:
            teams[color[smallest_nbr]].remove(smallest_nbr)
        
        G.nodes[smallest_nbr]['team'] = 5

    print(color)
    print(teams)

    return color, teams

            
        

# In[4]:


G = read_input('medium.in')
solve(G)
validate_output(G)
visualize(G)
score(G)

# for i in range(1, 261):
#     path = 'inputs/medium' + str(i) + '.in'
#     G = read_input(path)
#     solve(G)
#     print(score(G))

# In[33]:


run(solve, 'medium.in', 'medium.out')


# In[ ]:


run_all(solve, 'input', 'output')
tar('output')

