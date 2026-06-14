# -*- coding: utf-8 -*-

total = int(input())
rabbit = 0
rat = 0
frog = 0

for i in range(total):
    values = input().split()
    n = int(values[0])
    _type = values[1]
    
    if _type == 'C':
        rabbit += n
    elif _type == 'R':
        rat += n
    else:
        frog += n
        
total = rabbit + rat + frog
perc_rabbit = (rabbit / total) * 100
perc_rat = (rat / total) * 100
perc_frog = (frog / total) * 100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {rabbit}")
print(f"Total de ratos: {rat}")
print(f"Total de sapos: {frog}")
print(f"Percentual de coelhos: {perc_rabbit:.2f} %")
print(f"Percentual de ratos: {perc_rat:.2f} %")
print(f"Percentual de sapos: {perc_frog:.2f} %")