# Катя узнала, что ей для сна надо XX минут.
# В отличие от Коли, Катя ложится спать после полуночи в HH часов и MM минут.
# Помогите Кате определить, на какое время ей поставить будильник, чтобы он прозвенел ровно через XX минут после того, как она ляжет спать.
# На стандартный ввод, каждое в своей строке, подаются значения XX, HH и MM.
# Гарантируется, что Катя должна проснуться в тот же день, что и заснуть.
# Программа должна выводить время, на которое нужно поставить будильник: в первой строке часы, во второй — минуты.
#
# Sample Input 1:
# 480
# 1
# 2
#
# Sample Output 1:
# 9
# 2
#
# Sample Input 2:
# 475
# 1
# 55
#
# Sample Output 2:
# 9
# 50

X = int(input())
H = int(input())
M = int(input())
print((X + M) // 60 + H)
print((X + M) % 60)