a=list(map(int,input().split()))
b=list(map(int,input().split()))

result=list()
result.append(a[0]*b[1]+b[0])
result.apeend(a[1]*b[1])

if result[0]%result[1]==1: #기약분수로 만드는거.
