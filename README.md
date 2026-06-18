# Competitive Programming Notes

### Get the ASCII Position of an Uppercase Character
```python
import string

string.ascii_uppercase.index(char)
```

### Configure Standard Input
```python
from io import StringIO
import sys

sys.stdin = StringIO(input_data)
```

### Initialize a Matrix
```python
matrix = [[0 for _ in range(12)] for _ in range(12)]
```

### Descending Range
```python
for i in range(11, 0, -1):
```

### Format a Floating-Point Number
```python
f"{total:.1f}"
```

### Add Left Padding (Fixed Width)
```python
f"{value:3}"  # e.g., width of 3 characters
```

### Print a Matrix
```python
for i in range(n):
    print(" ".join([f"{item}" for item in matrix[i]]))
```

### Queues
```python
from collections import deque

queue = deque()

queue.append("Customer 1")
queue.append("Customer 2")

first = queue.popleft()
print(first)  # Customer 1
```

### EOF Error
```python
while True:
  try:
    # code here
  except EOFError:
    break
```