#Задание номер один
# w=int(input('Enter width: '))
# h=int(input('Enter hight: '))
# for i in range(h):
#     print('*' * w)
#Задание номер два
# h=int(input('Enter hight'))
# for i in range(1, h+1):
#     print('*' * i)
#Задание номер три
# h=int(input())
# for i in range(1, h+1):
#     print(' ' * (h-i)+ '*'*i)
#Задание номер четыре
# h=int(input('Enter size of the side: '))
# for i in range(h):
#     if i==0 or i==h-1:
#         print('*'*h)
#     else:
#         print('*'+' '*(h-2)+'*')
h=int(input('Enter hight: '))
for i in range(h):
    for j in range(h-i-1):
        print(' ', end='')
    for j in range(2*i+1):
        print('*', end='')
    print()
for i in range(h-2, -1, -1):
    for j in range(h-i-1):
        print(' ', end='')
    for j in range(2*i+1):
        print('*', end='')
    print()    