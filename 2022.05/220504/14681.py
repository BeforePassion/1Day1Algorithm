# 예를 들어, 좌표가 (12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다. 
# 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.
# 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오. 
# 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.

x=int(input())
y=int(input())
if 0<x:
    if 0<y:print('1')
    else:print('4')
else:
    if 0<y:print('2')
    else:print('3')

# 다른 코드
a = int(input())
b = int(input())
if a > 0:
    print(1 if b > 0 else 4)
elif a < 0:
    print(2 if b > 0 else 3)