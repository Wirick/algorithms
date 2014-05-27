from heapq import *


def breadth_first_search(search_problem):
    """Given a SEARCH_PROBLEM, performs a breadth first search on the
    search problem and returns a tuple (x, y, z, w), where x is the length of
    the solution, y number of path vertices, and z is the closed set of
    verticies, and w is the cost. Returns -1 if there is no solution."""
    initial_node = (search_problem.get_start_state(), [], 0)
    dq, closed = [], set()
    heappush(dq, (initial_node[2], initial_node))
    end = search_problem.get_end_state()
    successors = search_problem.get_successors
    goal_test = search_problem.is_goal
    while dq:
        current = heappop(dq)
        closed.add(current[1][0])
        if goal_test(current[1]):
            path = current[1][1] + [end]
            return (path, len(path) - 1, closed, current[1][2])
        else:
            new_nodes = successors(current[1])
            for node in new_nodes:
                if not node[0] in closed:
                    heappush(dq, (node[2], node))
    return -1

def depth_first_search(search_problem):
    """Given a SEARCH_PROBLEM, performs a depth first search on the search problem
    and returns a tuple (x, y, z, w) where x is the length of the solution,
    y is the number of path vertices, z is the closed set of locations, and w
    is the cost. Note the similarity to bfs."""
    initial_node = (search_problem.get_start_state(), [], 0)
    dq, closed = [], set()
    ## ahem..
    heappush(dq, (-initial_node[2], initial_node))
    end = search_problem.get_end_state()
    successors = search_problem.get_successors
    goal_test = search_problem.is_goal
    while dq:
        current = heappop(dq)
        closed.add(current[1][0])
        if goal_test(current[1]):
            return (current[1][1] + [end],
                   len(current[1][1] + [end]) - 1,
                   closed. current[1][2])
        else:
            new_nodes = successors(current[1])
            for node in new_nodes:
                if not node[0] in closed:
                    ## and again.
                    heappush(dq, (-node[2], node))
    return -1
