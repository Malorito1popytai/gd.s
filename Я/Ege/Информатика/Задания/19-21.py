def f(s, m):
    if s <= 40: return m%2==0
    if m == 0: return 0
    h = [f(s-2, m-1), f(s-3, m-1), f(s//2, m-1)]
    return any(h) if (m-1)%2==0 else all(h)

print(19, [s for s in range(41, 1000) if f(s, 2)])
print(20, [s for s in range(41, 1000) if not f(s, 2) and f(s, 3)])
print(21, [s for s in range(41, 1000) if not f(s, 2) and f(s, 4)])
# 1 1 2 2 3
# п в п в п
# 1 2 3 4 5
