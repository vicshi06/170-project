#!/usr/bin/env python
# coding: utf-8


# In[2]:


# The starter code is short and simple, take a look!
from starter import *
import random 


# In[9]:
def solve(G: nx.Graph):
    # TODO implement this function with your solver
    # Assign a team to v with G.nodes[v]['team'] = team_id
    # Access the team of v with team_id = G.nodes[v]['team']
    greedy_color(G, order(G))
    
# In[7]:
def order(G:nx.Graph):
    "Order the vertex according to decreasing endpoints"
    edges=sorted(G.edges(data=True), key=lambda t: t[2].get('weight', 1), reverse = True)
    ordered = []
    nodes = list(G.nodes)
    for i in range(len(edges)):
        first = edges[i][0]
        second = edges[i][1]
        if first not in ordered:
            ordered.append(first)
            nodes.remove(first)
        if second not in ordered:
            ordered.append(second)
            nodes.remove(second)
    ordered = ordered + nodes
    return ordered

def first_available1(color_list):
    """Return smallest non-negative integer not in the given list of colors."""
    #print("my color list is ", color_list)
    color_set = set(color_list)
    count = 1
    while True:
        if count not in color_set:
            return count
        count += 1


# In[71]:


def find_next_available_group(G, vertex, assigned_nodes, first_team, k, group):
    """if the current group number is smaller than the largest possible number,
    we directly append it to another group"""
    # 
    neighbor_edges = [(n, nbrdict) for n, nbrdict in G.adjacency()]
    curr_neighbors = neighbor_edges[vertex][1]
    sorted_neighbors_by_weights = list(sorted(curr_neighbors.items(), key=lambda item: item[1].get('weight', 1)))
    i = 0
    min_num_nodes = 100 / k #should be this amount of nodes in the team 
    while i < len(sorted_neighbors_by_weights):
        nearest_neighbor = sorted_neighbors_by_weights[i][0]
        # iff the neighbor has been assigned team
        if nearest_neighbor in assigned_nodes:
            #G.nodes[nearest_neighbor]["team"]
            if G.nodes[nearest_neighbor]["team"] < first_team:
                return nearest_neighbor
            else:
                break
        i = i + 1
    return random.randint(min(group.values(), key=len))

# In[76]:
def greedy_color(G, order):
    color = {}
    total_group_num = 0
    max_allowed = sorted(G.degree, key=lambda x: x[1], reverse=True)[0][1] + 1
    group_size = {} #key: color value: associated nodes of that color [list]
    group_sum = {}
    
    copy_G = G.copy() 
    
    # run the pure greedy and caculate the best score
    for node in order:
        used_neighbour_colors = [color[nbr] for nbr in copy_G[node]
                                 if nbr in color]
        color[node] = first_available1(used_neighbour_colors) 
        copy_G.nodes[node]['team'] = color[node] #color[node] 颜色 node: values 
        if group_size.get(color[node]) == None: 
            group_size[color[node]] = []
        group_size[color[node]].append(node)
        
    # Update best graph, best score, and k becomes number of groups in this graph
    best_G = copy_G.copy() 
    best_score = score(copy_G) 
    max_num_group = len(group_size) #the number of color
    best_group = {}
    best_k = 1 
    
    
    # Run greedy algorithm on different k values
    for k in range(1, max_num_group):
        copy_G = G.copy()
        color = {}
        group_size = {}
        assigned_nodes = []
        used_neighbour_colors = []
        
        for node in order:
            used_neighbour_colors = [color[nbr] for nbr in copy_G[node] if nbr in color]
            # Find team assignment
            # Check if k value returned < max_team_number
            first_team = first_available1(used_neighbour_colors)
            #print("first team is", first_team)
            if first_team > k:
                # Find the neighbor who has been assigned colors with lowest edge weight
                nearest_neighbor = find_next_available_group(copy_G, node, assigned_nodes, first_team, k, group_size)
                first_team = copy_G.nodes[nearest_neighbor]["team"]
            # updates graph values
            copy_G.nodes[node]["team"] = first_team
            assigned_nodes.append(node)
            color[node] = first_team
            if group_size.get(color[node]) == None: 
                group_size[color[node]] = []
            group_size[color[node]].append(node)
            
            
        curr_score = score(copy_G)
        if curr_score < best_score:
            best_score = curr_score
            best_G = copy_G.copy()
            best_group = group_size
            best_k = k 
        
    # Update G        
    for node in best_G.nodes:
        G.nodes[node]["team"] = best_G.nodes[node]["team"]

    # find the sum of edges within each team and put those values in a list
    for team in best_group:
        team_edges = []
        for node in best_group[team]:
            for neighbor in G[node]:
                if G.nodes[neighbor]["team"] == team:
                    team_edges.append(G[node][neighbor]["weight"])
        group_sum[team] = sum(team_edges)
    
    # find the team with the highest sum of edges
    max_team = max(group_sum, key=group_sum.get)
    counter = 0

    # iterate through the nodes in the team with the highest sum of edges
    # randomly choose a team that is not the max team
    # switch the team assignment of each node to a team that doesn't share any edges with it
    
    # some nodes might not be able to be switched because they share edges with all other teams
    # if this happens, we will just assign its team to a team that has the least number of nodes
    for node in best_group[max_team]:
        connection = False

        while G.nodes[node]["team"] == max_team and counter < 100: 
            random_team = random.randint(1, best_k)
            while random_team == max_team:
                random_team = random.randint(1, best_k)
            
            for next in best_group[random_team]:
                if G.has_edge(node, next):
                    connection = True
                    break

            if not connection:
                G.nodes[node]["team"] = random_team
                best_group[max_team].remove(node)
                best_group[random_team].append(node)
            
            counter += 1

            print(counter)
        
        if counter == 100:
            temp_group = best_group.copy()
            temp_group.pop(max_team, None)

            min_team = min(temp_group, key=lambda x: len(temp_group[x]))
            G.nodes[node]["team"] = min_team
            temp_group[min_team].append(node)
            counter = 0
            
    temp = []

    for team in best_group:
        temp.append(len(best_group.get(team)))
        
# In[85]:

# G = read_input('medium.in')
# solve(G)
# validate_output(G)
# visualize(G)
# score(G)

path = 'inputs/small' + str(4) + '.in'
G = read_input(path)
solve(G)
visualize(G)
print("score for input " + str(4) + " is " + str(score(G)))


# %%
