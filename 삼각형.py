a = int(input('숫자를 입력하세요 : '))
for i in range(1, a+1):
    for k in range(i):
        print('*',end="")
    print()
