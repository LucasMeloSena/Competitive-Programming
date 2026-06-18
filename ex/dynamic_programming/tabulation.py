def fib(n):
  table = [0 for _ in range(n+1)]
  table[1] = 1

  for i in range(0, n+1):
    if i + 1 <= len(table) - 1:
      table[i+1] += table[i]
    if i + 2 <= len(table) - 1:
      table[i+2] += table[i]

  return table[n]

print(fib(6))
print(fib(50))

def grid_traveler(i, j):
  i += 1
  j += 1
  table = [[0 for _ in range(i)] for _ in range(j)]
  table[1][1] = 1

  for m in range(i):
    row_in_bounds = m + 1 <= (len(table) - 1)
    for n in range(j):
      col_in_bounds = n + 1 <= (len(table[0]) - 1)
      if row_in_bounds:
        table[m+1][n] += table[m][n]
      if col_in_bounds:
        table[m][n+1] += table[m][n]

  print("\n".join(str(row) for row in table))
  return table[i-1][j-1]

print(grid_traveler(3,3))