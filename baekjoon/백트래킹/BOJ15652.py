from itertools import permutations

n, m = map(int, input().split())
data = list(range(1, n + 1))

result = list(permutations(data, m))
result.sort()

for i in result:
    print(*i)
