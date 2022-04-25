# Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.
# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
# В качестве ответа укажите вывод программы, а не саму программу.
# Слова, написанные в разных регистрах, считаются одинаковыми.
#
# Sample Input:
# abc a bCd bC AbC BC BCD bcd ABC
#
# Sample Output:
# abc 3
#
# У вас есть неограниченное число попыток.
# Время одной попытки: 5 mins

with open('dataset_3363_3.txt') as inf, open('dataset_3363_3_out.txt','w') as ouf:
    max_count = 0
    s = inf.read().lower().strip().split()
    s.sort()
    for word in s:
        counter = s.count(word)
        if counter > max_count:
            max_count = counter
            result_word = word
    ouf.write(result_word +' ' + str(max_count))