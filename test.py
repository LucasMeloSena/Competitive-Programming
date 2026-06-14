from collections import deque

fila = deque()

fila.append("Cliente 1")
fila.append("Cliente 2")

primeiro = fila.popleft()
print(primeiro) # Cliente 1
print(fila)