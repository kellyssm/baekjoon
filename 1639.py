S = input().strip()

max_len = 0 #조건을 만족하는 최대 길이
n = len(S)

for length in range(2, n + 1, 2):
    for start in range(n - length + 1):
        mid = start + length // 2
        end = start + length

        # 왼쪽 절반과 오른쪽 절반의 합
        left_sum = sum(int(S[i]) for i in range(start, mid))
        right_sum = sum(int(S[i]) for i in range(mid, end))

        #값이 같으면
        if left_sum == right_sum:
            max_len = length

print(max_len)

