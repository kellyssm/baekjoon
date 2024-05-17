x = int(input())

count =0
k=2 #분모 + 분자 초기값

while True:
    for n in range(1,k):
        m = k -n
        count +=1
        if count ==n:
            print(f"{n}/{m}")
            break
    if count == x:
        break
    k+=1

#시간 초과 에러남

'''
n = int(input())

line = 0
end = 0
while n > end:
    line += 1
    end += line

diff = end - n
if line%2 == 0: #짝수 라인 일때
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print("%d/%d"%(top,bottom))
'''
