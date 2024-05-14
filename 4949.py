while True:
    a = input()
    stack = []

    if a == ".":
        break

    balanced = True
    for i in a:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if not stack or stack.pop() != '[': #균형 안맞음
                balanced = False
                break
        elif i == ')':
            if not stack or stack.pop() != '(': #균형이 안맞으면
                balanced = False
                break

    if balanced and not stack: #균형 맞고, 스택 비어있으면
        print('yes')
    else:
        print('no')
