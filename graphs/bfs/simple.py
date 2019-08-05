def bfs(start, adj):
    level = {start: 0}
    frontier = [start]
    
    i = 1
    while frontier:
        next = []
        for u in frontier:
            print(u)
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    next.append(v)
        i += 1
        frontier = next


adj = {
    "a": ["c", "d"],
    "b": ["d"],
    "c": ["a", "d"],
    "d": ["a", "b", "c", "e"],
    "e": ["d"]
}

bfs("e", adj)