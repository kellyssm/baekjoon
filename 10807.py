a=int(input())
b=list(map(int,input().split()))
if a!= len(b):
    False
c=int(input())
sum=0
for i in range(len(b)):
    if b[i]==c:
        sum+=1
print(sum)

#https://www.acmicpc.net/problem/10807
