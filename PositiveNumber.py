print("Enter the list:")
numbers = [int(a) for a in input().split()]
print(*[x for x in numbers if x > 0])
print(*[x for x in [int(a) for a in input().split()] if x > 0])
