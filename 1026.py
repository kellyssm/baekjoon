k=int(input())
A = list(map(int,input().split()[:k]))
B= list(map(int,input().split()[:k]))

#A의 작은수와 B의 큰수를 곱한다.
A.sort()
maxB=max(B)
result=0

for a in A:
    result += a * maxB
    B.remove(maxB)  # B 배열에서 가장 큰 수를 제거
    if len(B) > 0:
        maxB = max(B)  # B 배열의 가장 큰 수 갱신

print(result)
