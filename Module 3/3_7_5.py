# Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
# Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
# Файл состоит из набора строк, каждая из которых представляет собой три поля:
# Класс Фамилия Рост
# Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего требуется вычислить значение в виде вещественного числа.
# Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый). Если про какой-то класс нет информации, необходимо вывести напротив него прочерк.
# В качестве ответа прикрепите файл с полученными данными о среднем росте.
#
# Sample Input:
# 6	Вяххи	159
# 11	Федотов	172
# 7	Бондарев	158
# 6	Чайкина	153
#
# Sample Output:
# 1 -
# 2 -
# 3 -
# 4 -
# 5 -
# 6 156.0
# 7 158.0
# 8 -
# 9 -
# 10 -
# 11 172.0
#
# У вас есть неограниченное число попыток.
# Время одной попытки: 5 mins

classes = {i: [] for i in range(1, 12)}
with open('dataset_3380_5.txt') as f:
    for line in f:
        cls, name, height = line.strip().split('\t')
        classes[int(cls)].append(int(height))

for cls, heights in classes.items():
    print(cls, sum(heights) / len(heights) if heights else '-')