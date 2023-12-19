n, m = map(int,input().split())
bag=[0 for i in range(5)]  # -> bag = [for i in range(n)] 으로 수정하니까 맞췄음 하놔...
for a in range(m):
    i,j,k=map(int,input().split())
    del bag[i-1:j]
    for b in range(i-1,j):
        if i <= j:
            bag.insert(i-1,k)
            i+=1
        
for p in bag:
    print(p, end=' ')

#예제 출력 잘 나오는데 왜 안되는거임?
#아..

#언제쯤 저 시뮬레이터 안돌리고 코딩을 할 수 있을까?

#------------------------------------------------------------
'''
n, m = map(int,input().split())
bag=[0 for i in range(n)]
for k in range(m):
    i, j, k = map(int, innput().split())
    for n in range(i,j+1):
        bag(n-1)=k
    
for n in range(N):
    print(bag[n], end=' ')
'''
#다른 사람이 한건데... 뭔 원리고...
