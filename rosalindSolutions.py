import algorithms
from util import Counter
from arrays import *
from search import *
from graphs import *
import numpy


def binary_search_reader():
    """Reads a text file in a certain format and returns a list of two elements:  [mData, nData].
    MData is a sorted array and nData is a list."""
    f = open("binarySearch.txt")
    all_lines = [line.rstrip() for line in f]
    f.close()
    m, m_data, n_data, m_data_len = int(all_lines[0]), [], [], 0
    for line in all_lines[2:]:
        new_data = [int(x) for x in line.split(" ")]
        if m_data_len < m:
            m_data = m_data + new_data
            m_data_len += len(new_data)
        else:
            n_data = n_data + new_data
    return [m, numpy.asarray(m_data), n_data]

def binary_search_problem(m, mData, nData):
    """MDATA a sorted array of length M taking integer values x st.
    -10^5 <= x <= 10^5. NDATA is a list. Outputs for each
    y element of NDATA an index i, such that MData[i] = y XOR i = -1 if
    the former does not exist."""
    f = open("binarySearchSoln.txt", "w")
    for x in nData:
        f.write(str(arrays.binary_search(mData, m, x)) + " ")
    print "Wrote file BinarySearchSoln.txt"
    f.close()

def vertex_degrees(fl1, fl2, incident_function):
    """Reads a file FL1 containing an edge list for a graph G, generates
    G using an INCIDENT_FUNCTION, and writes
    a FL2 with the degree of each vertex of G."""
    f, g = open(fl1), open(fl2, "w")
    lines = split(f)
    x, y = lines[0].split(" ")
    x, y, lines = int(x), int(y), lines[1:]
    counter = incident_function(lines, x)
    for i in range(x):
        g.write(str(counter[str(i+1)]) + " ")
    print "Wrote " + str(fl2)

def sum2_solution():
    f = open("sort.txt")
    contents = [lines.rstrip() for lines in f]
    f.close()
    size1, size2 = contents[0].split(" ")
    size1, size2 = int(size1), int(size2)
    g = open("generalSoln.txt", "w")
    for x in range(size1):
        arr1 = numpy.asarray([int(z) for z in contents[x + 1].split(" ")])
        arr1, number_of_actions = algorithms.has_additive_inverse(arr1, size2)
        if arr1 == -1:
            g.write(str(-1) + "\n")
        else:
            x, y = arr1
            g.write(str(x) + " " + str(y) + "\n")
        print "wrote to generalSoln.txt"
        print "efficiency of array number " + str(x+1) + " is " + str(number_of_actions)
    print "done"
    g.close()

def incident_list_from_file(fil):
    """Given a FILe, parses a graph in edge list format and returns the incidents."""
    f = open(fil)
    lines = [line.rstrip() for line in f]
    vals = lines[0].split(" ")
    a, b, graph = int(vals[0]), int(vals[1]), lines[1:]
    return incident_list(graph)

def get_majority_element_sol(fl1, fl2):
    """From a file FL1, parses k, n integers representing k arrays of size n,
    then proceeds to parse the arrays and find the majority element of each
    one, writing the element, followed by a space into the file FL2."""
    f, g = open(fl1), open(fl2, "w")
    f.close()
    l = [lines for lines in f]
    k, n = [int(a) for a in l[0].split(" ")]
    q = []
    m = get_majority_element
    for i in range(k):
        g.write(str(m([int(a) for a in l[i+1].split(" ")], n)) + " ")
    g.close()

def search_from_vertex(vertx, search_function, fl1, fl2):
    """Given an unweighted directed graph in edge list format in FL1, performs SEARCH_FUNCTION
    search on the graph to compute a distance from VERTX to vertex x st.
    1 <= x <= a, where a is the number of verticies in the graph. The function
    writes to FL2 -1 exactly when there does not exist a path from VERTX to vertex x,
    and with the length of the discovered path otherwise."""
    f, g = open(fl1), open(fl2, "w")
    a, b, lines = split(f)
    runs = 0
    f.close()
    for n in range(int(a)):
        runs += 1
        incidents = incident_list(lines)
        x = search_from_to_vertex(vertx, n+1, search_function, incidents)
        if x == -1:
            g.write(str(x) + " ")
        else:
            g.write(str(x[3]) + " ")
    if runs == a:
        print str(fl2)
    g.close()

def components_from_file(fl1):
    """Parses a graph from a file FL1 in edge list and prints
    the number of connected components of the graph"""
    f = open(fl1)
    a, b, lines = split(f)
    incidents = undirected_incident_list(lines)
    print get_connected_components(incidents, a)

def merge_sort_from_file(fl1, fl2):
    """Reads an array from a file FL1 and writes the
    sorted array to a file FL2."""
    f, g = open(fl1), open(fl2, "w")
    a = [lines for lines in f]
    order = int(a[0])
    arr = [int(b) for b in a[1].split(" ")]
    f.close()
    x = merge_sort(arr, order)
    for vals in x:
        g.write(str(vals) + " ")
    g.close()

def shortest_cycles(fl1, fl2):
    """Reads from a file FL1 an integer k and k graphs in edge list format, and
    writes the length of the shortest cylcle containing the leading edge of
    each graph, and -1 if such a cycle does not exist to FL2."""
    f, g = open(fl1), open(fl2, "w")
    lines = [line.rstrip() for line in f]
    graphs, lines, build  = [], lines[2:], []
    for line in lines:
      if len(line) == 0:
	graphs = graphs + [distinguished_edge_graph(build[1:])]
	build = []
      else:
	build = build + [line]
    graphs = graphs + [distinguished_edge_graph(build[1:])]
    for graph in graphs:
      prob = GraphSearchProblem(graph[0][1], graph[0][0], graph_path_goal_test, graph[1])
      sol = breadth_first_search(prob)
      if sol == -1:
	g.write(str(-1) + " ")
      else:
	g.write(str(sol[3] + graph[0][2]) + " ")
    g.close()
    f.close()
    
def distinguished_edge_graph(lst):
    """Parses a LST into a distinguished edge and the graph generated by
    the remaining edges and returns the ((start_vertex, end_vertex, cost),  graph) 
    tuple with start_vertex --> end_vertex being the distinguished edge with a cost."""
    edge, rest = lst[0], lst[1:]
    start_vertex, end_vertex, cost = edge.split(" ")
    graph = incident_list(rest)
    return (int(start_vertex), int(end_vertex), int(cost)), graph

shortest_cycles("graph.txt", "generalSoln.txt")
