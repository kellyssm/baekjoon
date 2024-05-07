a = int(input())

for _ in range(a):
    command = input()
    pos = [0, 0]
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    minx, maxx, miny, maxy = 0, 0, 0, 0
    direction = 0  # 초기 방향은 북쪽

    for i in command:
        if i == 'F':
            x, y = dir[direction]
            pos[0] += x
            pos[1] += y
        
        elif i == 'B':
            x, y = dir[direction]
            pos[0] -= x
            pos[1] -= y

        elif i == 'L':
            direction = (direction - 1) % 4
        
        elif i == 'R':
            direction = (direction + 1) % 4

        minx = min(minx, pos[0])
        maxx = max(maxx, pos[0])
        miny = min(miny, pos[1])
        maxy = max(maxy, pos[1])

    w = maxx - minx
    h = maxy - miny
    area = w * h
    print(area)
#
