import heapq

graph = {
  'A': {'B': 2, 'D': 8},
  'B': {'E': 6, 'D': 5},
  'D': {'E': 3, 'F': 2},
  'E': {'C': 9, 'F': 1},
  'F': {'C': 3, 'E': 1},
  'C': {}
}

source_node = 'A'
dest_node = 'C'

def dijkstra(graph, source_node, dest_node):
  distances = {node: float('inf') for node in graph.keys()}
  distances[source_node] = 0
  previous_node = {node: None for node in graph.keys()}

  priority_queue = [(0, source_node)]

  while priority_queue:
    curr_distance, curr_node = heapq.heappop(priority_queue)

    for neighbor, weight in graph[curr_node].items():
      distance = curr_distance + weight
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        previous_node[neighbor] = curr_node
        heapq.heappush(priority_queue, (distance, neighbor))
        
  print(f"Calculated weight from {source_node} to {dest_node}: {distances[dest_node]}")

  prev = previous_node[dest_node]
  path = [dest_node]
  while prev:
    path.append(prev)
    prev = previous_node[prev]

  path = path[::-1]
  print(f"Shortest path from {source_node} to {dest_node}: {'->'.join(path)}")

dijkstra(graph, source_node, dest_node)