size = int(input())
arr = [int(item) for item in input().split()]

smallest = min(arr)
index = arr.index(smallest)
        
print(f"Smallest value: {smallest}")
print(f"Position: {index}")