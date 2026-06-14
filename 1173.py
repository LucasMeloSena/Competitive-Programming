num = int(input())
n = []

for i in range(10):
    if i == 0:
        n.append(num)
    else:
        n.append(n[i-1] * 2)
        
for i in range(10):
  print(f"N[{i}] = {n[i]}")