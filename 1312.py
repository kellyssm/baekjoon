n = list(map(int, input().split()))
k = n[2]
sumt = n[0] / n[1]
# 소수 부분을 추출
result = str(sum).split('.')[1]
print(int(result[k]))

#왜자꾸 런타임 에러가 나는거임? => n범위 지정 안해줘서
#혜린이 코드
'''
A, B, N = map(int, input().split())

for i in range(N):
    A = (A%B)*10
    res = A//B

print(res)
'''
