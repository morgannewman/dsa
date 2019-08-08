"""
You are given a directed graph of courses a college student
has to take. An edge from course A to course B means that you
need to finish A before taking course B. Determine the minimum
number of semesters to finish all the courses.
"""
def topological_sort_helper(start, adj, state, stack):
    state['visiting'].add(start)

    for v in adj[start]:
        if v in state['visiting']:
            raise Exception("cycle detected")
        
        if v not in state['visited']:
            topological_sort_helper(v, adj, state, stack)


    state['visiting'].remove(start)
    state['visited'].add(start)
    stack.append(start)

def topological_sort(V, adj):
    state = {
        'visiting': set(),
        'visited': set()
    }

    stack = []

    for v in V:
        if v not in state['visited']:
            topological_sort_helper(v, adj, state, stack)
    return stack


def min_semesters_helper(v, adj, semesters, i, prereq):
    current_min = min_semesters[current]
    min_semesters[current] = max(current_min, prereq + 1)



def min_semesters(V, adj):
    classes = topological_sort(V, adj)
    classes.reverse()
    
    seen = set()

    min_semesters = [-1 for n in classes]
    min_semesters[0] = 1

    stack = []
    for i, c in enumerate(classes):





    
    return min_semesters
