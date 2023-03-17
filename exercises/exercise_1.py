# EXERCISE 1
words = input().split(' ')

solve = {w:words.count(w) for w in words if w.isalpha()}

print(len(solve.values()))

print(*solve.values())
