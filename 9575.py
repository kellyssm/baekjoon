import sys
input = sys.stdin.read
data = input().split()
    
index = 0
T = int(data[index]) #테스트케이스
index += 1
results = []
    
for _ in range(T):
    N = int(data[index])
    index += 1
    A = list(map(int, data[index:index + N]))
    index += N
        
    M = int(data[index])
    index += 1
    B = list(map(int, data[index:index + M]))
    index += M
        
    K = int(data[index])
    index += 1
    C = list(map(int, data[index:index + K]))
    index += K
       
    lucky_numbers = set() # 중복제거
        
    for a in A:
        for b in B:
            for c in C:
                total = a + b + c
                str_total = str(total) #문자열로 바꿈
                if all(char in '58' for char in str_total): #모든자리가 5,8인지 확인
                    lucky_numbers.add(total)
        
    results.append(len(lucky_numbers))
   
for result in results:
    print(result)
