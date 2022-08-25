a, b, c=map(int, input().split())
for i in range(3):
    if a>=b and b>=c:
        break
    if b>=a:
        t=a
        a=b
        b=t
    if c>=b:
        t=b
        b=c
        c=t

    if c>=a:
        t=a
        a=c
        c=t #a>b>c

if a==b==c:
    print(10000+(a*1000))
elif a==b!=c:
    print(1000+(a*100))
elif a!=b==c:
    print(1000+(b*100))
else:
    print(a*100)