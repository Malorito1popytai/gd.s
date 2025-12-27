from itertools import *

n = 0
for i in product(sorted("ПОБЕДА"), repeat=6):
    s = ''.join(i)
    n += 1
    if n%2==0 and s[0] in "О" and len(set(s))==6:
        print(n, s)
