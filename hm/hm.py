def func(a):
    numb = ''
    while a > 0:
        numb = str(a % 2) + numb
        a = a // 2
    print(numb)


while True:
    x = int(input('-> '))
    if x == 0:
        break
    func(x)
