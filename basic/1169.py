test_cases = int(input())

for _ in range(test_cases):
  squares_number = int(input())
  prev = 1
  amount = 0
  for _ in range(1, squares_number+1):
    amount = prev * 2
    prev = amount
  
  res = amount / 12 / 1000
  print(f"{int(res // 1)} kg")