def hanoi_tower(n, start, end) :
    if n == 1 :
        print(start, end)
        return
       
    hanoi_tower(n-1, start, 6-start-end) # 1단계
    print(start, end) # 2단계
    hanoi_tower(n-1, 6-start-end, end) # 3단계
    
n = int(input())
print(2**n-1) #하노이탑 최소 이동 횟수 2^n-1
hanoi_tower(n, 1, 3)

#하노이 탑이 n개 있다고 가정할 때, n-1개를 2번째에 먼저 옮기고 n번째를 3에 옮김
#그다음에 2번에 있던 n-1개를 3에 다시 옮김.
# 여기서 재귀가 사용되는데, n-1개를 옮길 때/ n-2까지 2에 두고 n-1를 3에 두고
#다시 n-2까지를 3에 냅둠. 머 그런식으로 1에 0개가 될 때까지 한다는 소리임.
#저 중간에 나오는 6은 1+2+3=6이기 때문. 함수에서 탑이 start에서 end로 이동하기 때문에
다 더하면 해당 탑이 어디로 갔는지 알 수 있다고 함. 

#어케.. 이해 되는 것 같기도 하고 아닌 것 같기도 하고.. 내가 안보고 짜라 하면 절대 못 함.ㅎ

#https://study-all-night.tistory.com/6
