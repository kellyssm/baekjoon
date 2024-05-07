#효원 코드
n, m = map(int, input().split())

for i in range(n-1):
	if i < n-m:
		print(i, i+1)
	else:
		print(n-m, i+1)

'''
정석 코드도 다시 풀어볼 것
'''
