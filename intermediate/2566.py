import sys
from io import StringIO
import heapq

_input = """5 6
1 2 0 200
1 3 1 400
2 4 0 300
3 4 1 300
2 5 0 700
4 5 1 100
"""

sys.stdin = StringIO(_input)

def dijkstra(graph, transport_type):
  distances = {node: float('inf') for node in graph.keys()}
  distances[1] = 0
  priority_queue = [(0, 1)]

  while priority_queue:
    curr_dist, curr_city = heapq.heappop(priority_queue)

    if curr_dist > distances[curr_city]:
      continue

    for neighbor, transport, cost in graph[curr_city]:
      distance = curr_dist + cost
      if transport == transport_type:
        if distance < distances[neighbor]:
          distances[neighbor] = distance
          heapq.heappush(priority_queue, (distance, neighbor))

  return distances

while True:
  try:
    n_cities, n_stretches = [int(item) for item in input().split()]
    graph = {i: [] for i in range(1, n_cities + 1)}

    for i in range(1, n_stretches+1):
      city_a, city_b, transport, cost = [int(item) for item in input().split()]
      graph[city_a].append((city_b, transport, cost))
    
    bus_cost = dijkstra(graph, 0)
    airplane_cost = dijkstra(graph, 1)

    print(min(bus_cost[n_cities], airplane_cost[n_cities]))
  except EOFError:
    break
