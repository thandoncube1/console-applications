// Adding a sample directed graph structure to look over
// Example:
const graph = {
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
