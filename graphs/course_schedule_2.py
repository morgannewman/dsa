"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
"""

class GraphCycleError(Exception):
    pass

def topological_sort_helper(start, adj, state, result):
    state[start] = 1

    for v in adj[start]:
        if state[v] == 1:
            raise GraphCycleError
        
        if state[v] != 2:
            topological_sort_helper(v, adj, state, result)
    
    state[start] = 2
    result.append(start)

def topological_sort(num_nodes, adj):
    sorted_stack = []
    state = [0 for each in range(num_nodes)]

    for n in range(num_nodes):
        if state[n] != 2:
            topological_sort_helper(n, adj, state, sorted_stack)

    sorted_stack.reverse()
    return sorted_stack


def find_order(numCourses, prerequisites):
    adj = [set() for each in range(numCourses)]

    for dest, origin in prerequisites:
        adj[origin].add(dest)

    try:
        return topological_sort(numCourses, adj)
    except GraphCycleError:
        return []


print(find_order(4, [[1,0],[2,0],[3,1],[3,2]]))