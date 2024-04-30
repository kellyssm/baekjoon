#11656
'''
a = input()
array =[]

for i in range(len(a)) :
    array.append(a[i:])

array.sort()
for i in array :
    print(i)'''


#1978
"""
n=int(input())
num=list(map(int,input().split()))
result =0


for i in num:
    if i==1:
        continue
    temp =0
    for j in range(2,i+1):
        if i%j ==0:
            temp+=1
        
    if temp == 1:
        result+=1
print(result)

"""

#9655
'''
n=int(input())
if n%2==0:
    print("CY")
else:
    print("SK")
'''

#2163
'''
N,M= map(int,input().split())
result=(N-1)+N*(M-1)
print(result)
'''

#16499
'''
n = int(input())
arr = []
duplicates = set()

for i in range(n):
    word = input()
    word_sorted = ''.join(sorted(word))
    if word_sorted in duplicates:
        continue
    else:
        duplicates.add(word_sorted)

print(len(duplicates))

'''
