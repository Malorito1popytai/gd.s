m = []

for x in range(1, 3001):
    n = 4**210+4**110-x
    while n > 0:
        if n%4 ==0:
            i += 1
            n //= 4
    m.append(i)
print(max(m))
