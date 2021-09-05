"""
1. Find the cheapest node. This is the node you can get to in the least
amount of time.
2. Check whether there’s a cheaper path to the neighbors of this node.
If so, update their costs.
3. Repeat until you’ve done this for every node in the graph.
4. Calculate the final path. (Coming up in the next section!)

Dijkstra’s algorithm only works with directed acyclic graphs,
called DAGs for short.
"""
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node



graphs={}
costs ={}
parents={}

graphs['start'] = {}

graphs['start']['a'] = 6
graphs['start']['b'] = 2

#to get start neighbors:
#print(graphs['start'].keys())

graphs['a'] = {}
graphs['a']['fin'] = 1

graphs['b'] = {}
graphs['b']['a'] = 3
graphs['b']['fin'] = 5

graphs['fin'] = {}

costs['a'] = 6
costs['b'] = 2
costs['fin'] = float("inf")

parents['a'] = 'start'
parents['b'] = 'start'
parents['fin']=None

processed =[]
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graphs[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n]> new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


