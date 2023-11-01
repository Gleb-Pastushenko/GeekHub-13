# Написати функцію, яка приймає на вхід список (через кому),
# підраховує кількість однакових елементів у ньомy і виводить результат.
# Елементами списку можуть бути дані будь-яких типів.
# Наприклад:
# 1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"


def repetitions(lst):
    rep_list = []

    while lst:
        cur_item = lst.pop(0)
        count = 1
        
        for i in range(len(lst)-1, -1, -1):
            if lst[i] == cur_item and type(lst[i]) == type(cur_item):
                lst.pop(i)
                count += 1
        
        rep_list.append([cur_item, count])
    
    print(', '.join([f'{item} -> {count}' for item, count in rep_list]))