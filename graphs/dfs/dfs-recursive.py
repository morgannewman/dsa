def dfs(V, Adj):
    seen = set()

    for v in V:
        if v not in seen:
            seen.add(v)
            dfs_visit(v, Adj, seen)
            


def dfs_visit(start, Adj, seen):
    print(start)
    for v in Adj[start]:
        if v not in seen:
            seen.add(v)
            dfs_visit(v, Adj, seen)
            


vertices = [1, 2, 3, 4, 5]

Adj = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 5],
    4: [2],
    5: [2, 3]
}

dfs(vertices, Adj)