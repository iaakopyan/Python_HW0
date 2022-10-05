#Задано число N. С начала дня (00:00) прошло N минут.
#Преобразуйте время в этот момент в часы и минуты, которые покажут цифровые часы.
N = -1
h = 0
while N < 0 or N > 10 ** 7:
    N = int(input())
while N >= 60:
    h = h + 1
    N = N - 60
while h >= 24:
    h = 0
if N < 10:
    print(h, ':0', N, sep="")
elif h < 10:
    print('0', h, ':', N, sep="")
elif h < 10 and N < 10:
    print('0', h, ':0', N, sep="")
else:
    print(h, ':', N, sep="")
