from collections import deque


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []



def check(key):
    return key[-1] == 'm'


def breadth_first_search(starting_point):
    queue = deque()
    queue += graph[starting_point]  # add starting_point's neighbours initially
    searched = []  # track items we've already checked

    while queue:
        item = queue.popleft()
        if item not in searched:
            if check(item):
                print('found a match: {}'.format(item))
                return True  # we're finished!
            else:
                queue += graph[item]  # add this item's neighbours
                searched.append(item)  # tracked as being checked already

    return False



breadth_first_search('you')  # found a match: thom


"""
Breadth First Search
Description:
    Breadth-first search tells you if there’s a path from A to B.
    If there’s a path, breadth-first search will find the shortest path.
    A directed graph has arrows, and the relationship follows the direction of the arrow.
    Undirected graphs don’t have arrows, and the relationship goes both ways.
Explanation:
    A graph is made up of 'nodes' and 'edges'.
    In this algorithm there are no 'weights' to the edges (see: Dijkstra’s algorithm)
    An directed graph can also be a 'Tree', but an undirected graph cannot.
    The closest nodes are our 1st 'degree', outer nodes are 2nd, 3rd degrees etc.
    We keep a queue of the 1st degree nodes.
    Pop the first node off the queue and check if this gives you your 'match'
        'match' being the logic that determines if you can stop searching
    If it doesn't match, then add all the 'neighbours' for that node to the queue.
    Rinse and Repeat (e.g. pop next 1st degree node, check it, add neighbours...)
    If the queue is empty, then there were no matches within your network graph.
Performance:
    O(V+E)
    It means V for vertices and E for edges.
    That is, worst case, you have to search the entire graph & follow every edge.
    It also includes O(1) for adding new degrees to the queue
Notes:
    Only provides you with the 'shortest' route, not the 'fastest'
    For 'fastest' route (i.e. weighted graphs) see Dijkstra’s algorithm
    You need to check people in the order they were added to the search list,
    so the search list needs to be a queue.
    Otherwise, you won’t get the shortest path.
    You also need to make sure not to check the same node twice.
    Some nodes from a degree could share a node in the next outer degree.
    It doesn't break the algorithm but is a wasteful operation performance-wise.
'''
"""