# Выведите таблицу размером n×n, заполненную числами от 11 до n^2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
#
# Sample Input:
# 5
#
# Sample Output:
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

a=int(input())
nul=[[0]*a for i in range(a)]
x,y=0,0
for i in range(1,a**2+1):
    nul[x][y]=i
    if x<=y+1 and x+y<a-1: y+=1
    elif x<y: x+=1
    elif x+y>=a : y-=1
    elif x>=y : x-=1
for i in range(a):
    print(*nul[i])