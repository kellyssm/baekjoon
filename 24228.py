nr=list(map(int,input().split()))
print(nr[0] +2*nr[1]-1)

'''
왜 n+2r-1?
: 각 종류의 젓가락을 1개씩 뽑았기 때문에 2r개의 젓가락을 짝을 맞추기 위해선
2r-1개의 추가적인 젓가락이 필요하다. => 최악의 경우 하나의 젓가락에서 2r번째 젓가락을 얻을 수 있다.

따라서 n + 2r - 1
'''
