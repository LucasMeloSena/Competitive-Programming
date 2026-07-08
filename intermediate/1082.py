import sys
from io import StringIO

_input = """3
3 1
a c
10 10
a b
a c
a g
b c
c g
e d
d f
h i
i j
j h
6 4
a b
b c
c a
e f
"""

sys.stdin = StringIO(_input)

test_cases = int(input())

def dfs(graph, vertex, visited, component):
  visited.add(vertex)
  component.append(vertex)

  for neighbor in graph[vertex]:
    if neighbor not in visited:
      dfs(graph, neighbor, visited, component)

for test_case in range(1, test_cases+1):
  print(f"Case #{test_case}:")

  vertex, edges = [int(item) for item in input().split()]
  graph = {chr(ord('a') + i): [] for i in range(vertex)}
  
  for _ in range(edges):
    a, b = [item for item in input().split()]
    graph[a].append(b)
    graph[b].append(a)

  visited = set()
  components = 0

  for vertex in graph.keys():
    if vertex not in visited:
      component = []
      dfs(graph, vertex, visited, component)
      print(",".join(sorted(component)) + ",")
      components += 1

  print(f"{components} connected components\n")