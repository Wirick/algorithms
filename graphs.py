## General note: I have used a dictionary as my graph data structure. My dictionary maps
## verticies to sets of (incident vertex, cost) tuples. We view every graph as a directed
## graph, as an undirected graph with an edge a -- b can be represented as a --> b and
## b --> a.
from search import *
from collections import defaultdict

def incident_list(edges):
    """Given the incident list EDGES of a directed graph represented as
    strings of the form "a b(\\s cost)!", adds to a dictionary
    of edges with keys the starting location and values a tuple
    (end location, cost). When no cost is specified, a cost of 1 is assigned."""
    dic = defaultdict(lambda: set())
    for edge in edges:
        vals = edge.split(" ")
        if len(vals) == 2:
            dic[int(vals[0])].add((int(vals[1]), 1))
        else:
            a, b, c = vals[0], vals[1], vals[2]
            dic[int(a)].add((int(b), int(c)))
    return dic

def undirected_incident_list(edges):
    """Given the incident list EDGES of an undirected graph represented as
    strings of the form "a b(\\s cst)!" where a and b have an edge, adds
    to a dictionary of edges with keys the starting location and values a tuple
    (end location, cst). When no cst is specified, a cost of 1 is assigned."""
    dic = defaultdict(lambda: set())
    for edge in edges:
        vals = edge.split(" ")
        if len(vals) == 2:
            dic[int(vals[0])].add((int(vals[1]), 1))
            dic[int(vals[1])].add((int(vals[0]), 1))
        else:
            a, b, c = vals[0], vals[1], vals[2]
            dic[int(a)].add((int(b), int(c)))
            dic[int(b)].add((int(a), int(c)))
    return dic

def degree_array(incidents, n):
    """Given a graph of INCIDENTS of order N, returns a counter where
    counter[i] = d, where d is the degree of vertex i: element of {1, ... , N}."""
    counter = defaultdict(lambda: 0)
    for line in incidents:
        a, b = line.split(" ")
        counter[a] += 1
        counter[b] += 1
    return counter

def double_degree_array(incidents, n):
    """Given a graph of INCIDENTS of order N, returns
    a count(er) where count[i] = the total sum of the degrees of i's neighbors."""
    degreeList = degreeArray(incidents, n)
    incidents = incidentList(incidents)
    count = defaultdict(lambda: 0)
    for i in range(n):
        for j in incidents[str(i+1)]:
            count[str(i+1)] += degreeList[j]
    return count

def length_of_shortest_cycle(incidents, vert1, vert2):
    """Returns the length of the shortest cycle in a graph
    with given INCIDENTS through the edge VERT1 --> VERT2. 
    Assumes this edge is not contained in incidents."""
    problem = GraphSearchProblem(vert1, vert2, graph_path_goal_test, incidents)
    x = breadth_first_search(problem)
    return x[3]

def search_from_to_vertex(
        frm, to, search_function,
        incidents):
    """Searches FRM a vertex in a graph INCIDENTS to see if there is a path TO another
    vertex using SEARCH_FUNCTION, where the verticies are given as a dictionary
    whose keys are starting locations and whose values are a (end location, cost)
    tuple. Returns a (path, path verticies, closed set, cost) tuple if the
    search is successful, and -1 otherwise."""
    m = GraphSearchProblem(frm, to, graph_path_goal_test,
                           incidents)
    return search_function(m)

def get_component_of(x, incidents, n):
    """Returns the set of connected verticies associated to a particular vertex X from a
    dictionary of INCIDENTS for a graph of order N."""
    closed = set()
    for i in range(n):
        if i+1 in closed:
            continue
        problem = GraphSearchProblem(x, i+1, graph_path_goal_test, incidents)
        result = depth_first_search(problem)
        if result == -1:
           continue
        closed = closed.union(result[2])
    return closed

def get_connected_components(incidents, order):
    """Returns the number of connected components in an undirected graph represented by
    an ORDER and a dictionary of INCIDENTS whose values are (end location, cost) tuples
    and whose keys are starting locations."""
    closed = set()
    components = 0
    for i in range(order):
        if i+1 in closed:
            continue
        components += 1
        closed = closed.union(get_component_of(i+1, incidents, order))
    return components

def get_graph_successors(node, incidents):
    """Given a graph as a default dict INCIDENTS, returns the graph
    sucessors in the (location, path, cost) form of a typical node in a
    search problem"""
    succ = []
    for point in incidents[node[0]]:
        succ = succ + [(point[0], node[1] + [node[0]], node[2] + point[1])]
    return succ

def graph_path_goal_test(node, end_state):
    """Given a tuple NODE consisting of a current location, a path taken to get there,
    and the total cost of the trip, compares the current location to END_STATE, and
    returns true exacly when the current location is equal to the end state, and flase
    otherwise"""
    if node[0] == end_state:
        return True
    else:
        return False


class GraphSearchProblem:
    """Class for a graph search problem."""
    def __init__(self, startState, endState,
                 goalTest, incidents):
        self.succFunc = get_graph_successors
        self.startState = startState
        self.endState = endState
        self.goalTest = goalTest
        self.incidents = incidents

    def get_start_state(self):
        return self.startState

    def get_end_state(self):
        return self.endState

    def get_successors(self, node):
        return self.succFunc(node, self.incidents)

    def is_goal(self, node):
        return self.goalTest(node, self.endState)


