const bfs = function(start, adj) {
  const levels = { [start]: 0 };
  let frontier = [start];

  let i = 1;
  while (frontier.length > 0) {
    const next = [];
    for (const u of frontier) {
      console.log(u);
      for (const v of adj[u]) {
        if (!(v in levels)) {
          levels[v] = i;
          next.push(v);
        }
      }
    }
    frontier = next;
  }
};

const adj = {
  a: ["c", "d"],
  b: ["d"],
  c: ["a", "d"],
  d: ["a", "b", "c", "e"],
  e: ["d"]
};

bfs("e", adj);
