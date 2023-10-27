# Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345" -> просто потицяв по клавi =)
# Створіть ф-цiю, яка буде отримувати рядки на зразок цього та яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр лише з буквами (без пробілів)
# -  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)

import re


def extract_alpha_digits(string):
    alpha_list = re.findall(r'[a-zA-Z]', string)
    digits_list = re.findall(r'\d+', string)

    return alpha_list, digits_list


def alpha_digits_counter(string):
    alpha_list, digits_list = extract_alpha_digits(string)

    print(f'Total string length:  {len(string)}')
    print(f'Number of alphabetical chars:  {len("".join(alpha_list))}')
    print(f'Number of digit characters:  {len("".join(digits_list))}')


def concat_alpha_sum_numbers(string):
    alpha_list, digits_list = extract_alpha_digits(string)

    numbers_sum = sum(map(lambda x: int(x), digits_list))
    strings_concat = "".join(alpha_list)

    print(f'Numbers sum:  {numbers_sum}')
    print(f'Concatenated alphabetical:  {strings_concat}')


def sentense_lengths(string):
    sentenses = list(map(lambda sentense: sentense.strip(), string.split(' ')))
    sentenses_lengths = list(filter(lambda item: bool(
        item), (map(lambda sentense: len(sentense), sentenses))))

    print(f'Sentenses number:  {len(sentenses)}')
    print(
        f'Sentenses lengths:  {sentenses_lengths}')


def hangle_string(string):
    str_len = len(string)

    if 30 <= str_len <= 50:
        alpha_digits_counter(string)
    elif str_len < 30:
        concat_alpha_sum_numbers(string)
    else:
        sentense_lengths(string)


if __name__ == "__main__":
    hangle_string(input('Enter custom string:  '))
