class GraphCycleError(Exception):
    pass

def dfs_visit(start, adj, state):
    state[start] = 1
    
    for v in adj[start]:
        if state[v] == 1:
            raise GraphCycleError
        
        if state[v] != 2:
            dfs_visit(v, adj, state)
    
    state[start] = 2
    

def can_finish(numCourses, prerequisites):
    adj = [set() for each in range(numCourses)]

    for dest, origin in prerequisites:
        adj[origin].add(dest)

    """
    0 = not visited
    1 = visiting
    2 = visited
    """
    state = [0 for each in range(numCourses)]

    for v in range(numCourses):
        if state[v] == 2:
            continue

        try:
            dfs_visit(v, adj, state)
        except GraphCycleError:
            return False
    
    return True

print(can_finish(2, [[1,0],[0,1]]))