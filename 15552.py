import sys
ls=list()
num = int(sys.stdin.readline())
for i in range(num):
    a,b = map(int,sys.stdin.readline().split())
    ls.append(a+b)

for i in range(num):
    print(ls[i])
    
# 파이썬은 input() 대신에 sys.stdin.readline()을 사용함.
# 반복문으로 여러줄을 입력받을 때 input()으로 받으면 시간 초과가 일어날 수 있음. 
# sys.stdin.readline() 얘는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열 저장하고 싶은 경우에 .rstrip()을 
# 추가적으로 써주는 것이 좋음.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# C++을 사용하고 있고 cin/cout을 사용하고자 한다면, cin.tie(NULL)과 sync_with_stdio(false)를 둘 다 적용해 주고,
# endl 대신 개행문자(\n)를 쓰자. 단, 이렇게 하면 더 이상 scanf/printf/puts/getchar/putchar 등 C의 입출력 방식을 
# 사용하면 안 된다.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Java를 사용하고 있다면, Scanner와 System.out.println 대신 BufferedReader와 BufferedWriter를 사용할 수 있다. 
# BufferedWriter.flush는 맨 마지막에 한 번만 하면 된다.
