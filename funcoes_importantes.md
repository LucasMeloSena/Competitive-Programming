### Descobrir codigo ascii caractere upper
```python
string.ascii_uppercase.index(char)
```

### Configurar a input
```python
from io import StringIO
import sys
sys.stdin = StringIO(entrada)
```

### Preencher uma matriz: 
```python
array = [[0 for _ in range(12)] for _ in range(12)]
```

### Range decrescente:
```python
for i in range(11, 0, -1):
```

### Formatar ponto flutuante:
```python
f"{_sum:.1f}"
```

### Adicionar espaços a esquerda:
```python
f"{valor:3}" # e.g adicionando 3 espaços
```

### Renderizando uma matriz:
```python
for i in range(n):
    print(" ".join([f"{item}" for item in array[i]]))
```

### Filas:
```python
from collections import deque

fila = deque()

fila.append("Cliente 1")
fila.append("Cliente 2")

primeiro = fila.popleft()
print(primeiro) # Cliente 1
```