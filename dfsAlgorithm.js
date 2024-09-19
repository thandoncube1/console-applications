// Adding a sample directed graph structure to look over
// Example:
const europeGraph = {
  Paris: ['London', 'Madrid'],
  London: ['Berlin', 'Amsterdam'],
  Berlin: ['Warsaw', 'Prague'],
  Madrid: ['Lisbon'],
  Lisbon: [],
  Amsterdam: ['Brussels'],
  Brussels: ['Paris'],
  Warsaw: ['Berlin'],
  Prague: ['Vienna'],
  Vienna: ['Budapest'],
  Budapest: [],
  // Assume these are disconnected nodes
  Athens: [],
  Rome: []
};

// Write the algorithm that returns a visited nodes as an array

function dfs(graph, start) {
  const visited = new Set();
  const result = new Array(); // Typed array of size 8.

  function internalDFS(node) {
    if(visited.has(node)) return;
    visited.add(node);
    result.push(node);

    graph[node].forEach((nextNode) => {
      if (!visited.has(nextNode)) {
        internalDFS(nextNode);
      }
    });
  }

  internalDFS(start);
  return result;
}

console.log(dfs(europeGraph, "Paris"));
