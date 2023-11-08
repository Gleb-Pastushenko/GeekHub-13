# Напишіть функцію, яка приймає 2 списки. Результатом має бути новий список,
# в якому знаходяться елементи першого списку, яких немає в другому.
# Порядок елементів, що залишилися має відповідати порядку в першому (оригінальному) списку.
# Реалізуйте обчислення за допомогою генератора.
#     Приклад:
#     array_diff([1, 2], [1]) --> [2]
#     array_diff([1, 2, 2, 2, 4, 3, 4], [2]) --> [1, 4, 3, 4]


def array_diff(list1, list2):
    def get_element(list1, list2):
        for item in list1:
            if item not in list2:
                yield item

    result_list = []
    elements = get_element(list1, list2)

    while True:
        try:
            result_list.append(next(elements))
        except:
            return result_list


if __name__ == "__main__":
    print(array_diff([1, 2], [1]))
    print(array_diff([1, 2, 2, 2, 4, 3, 4], [2]))
