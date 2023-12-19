n, m =map(int,input().split())
bag=list()
for a in range(n):
    bag.append(a+1)

for b in range(m):
    i, j = map(int,input().split())
    bag[i-1], bag[j-1] = bag[j-1], bag[i-1] #이런.. 까먹었다니

for q in bag:
    print(q, end=" ")

