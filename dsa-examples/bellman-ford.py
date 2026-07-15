graph = {
  'A': {'B': 4, 'C': 2},
  'B': {'C': 3, 'D': 2, 'E': 3},
  'C': {'B': 1, 'D': -2},
  'D': {'E': 2},
  'E': {}
}

source_node = 'A'
dest_node = 'C'

def bellmand_ford(graph, source_node, dest_node):
  distances = {node: float('inf') for node in graph.keys()}
  previous_distances = {node: None for node in graph.keys()}
  distances[source_node] = 0

  for _ in range(len(graph.keys()) - 1):
    has_changed = False

    for vertex in graph.keys():
      for neighbor, weight in graph[vertex].items():
        distance = distances[vertex] + weight
        if distance < distances[neighbor]:
          distances[neighbor] = distance
          previous_distances[neighbor] = vertex
          has_changed = True

    if not has_changed:
      break

  # Detect negative cycles:
  for vertex in graph.keys():
    for neighbor, weight in graph[vertex].items():
      distance = distances[vertex] + weight
      if distance < distances[neighbor]:
        raise ValueError("Graph has a negative cycle")
      
  print(distances)
  print(previous_distances)

bellmand_ford(graph, source_node, dest_node)