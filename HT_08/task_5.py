# Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих регістро-незалежних букв та цифр,
# які зустрічаються в рядку більше ніж 1 раз. Рядок буде складатися лише з цифр та букв (великих і малих).
# Реалізуйте обчислення за допомогою генератора.
#     Example (input string -> result):
#     "abcde" -> 0            # немає символів, що повторюються
#     "aabbcde" -> 2          # 'a' та 'b'
#     "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
#     "indivisibility" -> 1   # 'i' присутнє 6 разів
#     "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
#     "aA11" -> 2             # 'a' і '1'
#     "ABBA" -> 2             # 'A' і 'B' кожна двічі


def repetitions(string):
    string = string.lower()
    return len(list((letter for letter in set(string) if string.count(letter) > 1)))


if __name__ == "__main__":
    print(repetitions("abcde"))
    print(repetitions("aabbcde"))
    print(repetitions("aabBcde"))
    print(repetitions("indivisibility"))
    print(repetitions("Indivisibilities"))
    print(repetitions("aA11"))
    print(repetitions("ABBA"))
