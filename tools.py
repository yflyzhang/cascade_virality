import numpy as np
import networkx as nx




# For illustration purpose only [easy to understand the process]
# -----------------------------
def pure_cascade_virality(G):
    '''G is a directed graph(tree)'''
    if not nx.is_weakly_connected(G):
        # return None
        return
    
    nodes = [k for (k,v) in G.out_degree() if v>0]  # non-leaf nodes
    
    virality = 0
    
    for source in nodes:
        path_lens = nx.single_source_shortest_path_length(G, source)  # shortest path length
        path_lens = {k: v for k, v in path_lens.items() if v > 0}    # filter 0
        virality += np.array(list(path_lens.values())).mean()    # mean length from source to other nodes
        
    return virality






# Works in a recursive manner [more efficient]
# -----------------------------
def recursive_path_length(G, V, seed):
    '''G is a directed graph(tree)''' 
    
    V[seed] = []
    for i in  G.successors(seed):
        V[seed].append(1)
        V[seed] += [j+1 for j in recursive_path_length(G, V, i)]
    return V[seed]




def recursive_cascade_virality(G, source=None):
    '''G is a directed graph(tree)'''
    if not nx.is_weakly_connected(G):
        # return None
        return
    if not source:
        # if root is not given, find it by yourself
        source = [k for (k,v) in G.in_degree() if v==0][0]
        
    V_dic = {}
    recursive_path_length(G, V_dic, source)
    
    # return V_dic # return original paths

    virality = 0
    for (k, v) in V_dic.items():
        # print(k, v)
        if len(v)>0:
            virality += np.mean(v)
    
    return virality # return cascade virality




