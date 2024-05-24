from math import gcd

a = list(map(int, input().split()))
b = list(map(int, input().split()))
temp = []

temp.append(a[0] * b[1] + b[0] * a[1])
temp.append(a[1] * b[1])

numerator = temp[0] #분자
denominator = temp[1] #분모
gcdn = gcd(numerator, denominator) #기약분수 만들기


simplified_numerator = numerator // gcdn
simplified_denominator = denominator // gcdn

print(simplified_numerator, simplified_denominator)


