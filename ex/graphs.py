from collections import deque

"""
Problem nº 1:
"""
def hasPathDFS(graph, source, dest, visited = None):
    if source == dest:
        return True
      
    if visited is None:
      visited = set()
      
    if source in visited:
      return False
      
    visited.add(source)

    for neighbor in graph[source]:
        if hasPathDFS(graph, neighbor, dest, visited) == True:
            return True
    return False


def hasPathBFS(graph, source, dest):
    if source == dest:
        return True
    
    visited = set([source])
    queue = deque([source])

    while len(queue) > 0:
        current = graph[queue.popleft()]
        for neighbor in current:
          if neighbor not in visited:
              visited.add(neighbor)
              if neighbor == dest:
                  return True
              queue.append(neighbor)

    return False


# Repeated nodes
graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["f"],
    "e": [],
    "f": [],
}

# Grafo cíclico
graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": ["b"],
    "f": [],
}

dfs = hasPathDFS(graph, "a", "f")
print(f"Has path DFS? {dfs}")

bfs = hasPathBFS(graph, "a", "f")
print(f"Has path BFS? {bfs}")

"""
Problem nº 2:
"""
def connected_components_count(graph):
    count = 0
    visited = set()
    for node in graph:
        if explore(graph, node, visited) == True: 
            count += 1
    return count

def explore(graph, current, visited):
    if current in visited: 
        return False
    
    visited.add(current)
    
    for node in graph[current]:
        explore(graph, node, visited)
    
    return True

graph = {
    '3': [],
    '4': ['6'],
    '6': ['4', '5', '7', '8'],
    '8': ['6'],
    '7': ['6'],
    '5': ['6'],
    '1': ['2'],
    '2': ['1']
}

count = connected_components_count(graph)
print(f"Connected components count: {count}")

"""
Problem nº 3:
"""
def largest_component(graph):
    largest = 0
    visited = set()
    for node in graph:
        size = explore(graph, node, visited)
        if size > largest: 
            largest = size
            
    return largest
    
def explore(graph, current, visited):
    if current in visited:
        return 0
    
    visited.add(current)
    
    size = 1
    for node in graph[current]:
        size += explore(graph, node, visited)
        
    return size

graph = {
    '0': ['8', '1', '5'],
    '1': ['0'],
    '5': ['0', '8'],
    '8': ['0', '5'],
    '2': ['3', '4'],
    '3': ['2', '4'],
    '4': ['3', '2']
}

largest = largest_component(graph)
print(f"Largest component: {largest}")

"""
Problem nº 4:
"""
edges = [
    ['w', 'y'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

graph = {}

for edge in edges:
    [a, b] = edge
    if a not in graph: graph[a] = []
    if b not in graph: graph[b] = []
    
    graph[a].append(b)
    graph[b].append(a)

def shortest_path(graph, source, dest):
    visited = set()
    
    if source == dest:
        return 0
    
    queue = deque([(source, 0)])
    
    while len(queue) > 0:
        current = queue.popleft()
        current_node = current[0]
        
        if current_node not in visited:
            visited.add(current_node)
            current_distance = current[1]
            
            for node in graph[current_node]:
                if node == dest:
                    return current_distance + 1
                queue.append((node, current_distance + 1))
    
    return -1

shortest = shortest_path(graph, 'w', 'c')
print(f"Shortest path: {shortest}")