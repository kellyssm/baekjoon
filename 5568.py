import itertools
n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
print(len(set("".join(i) for i in itertools.permutations(cards, k))))
#k장을 선택한 모든 순열 생성.
#join로 합치는데 set으로 중복제거
