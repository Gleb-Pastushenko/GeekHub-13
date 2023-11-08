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
    def get_letter(string):
        for letter in string:
            yield letter.lower()

    letters = get_letter(string)
    repetition_counter = 0
    repetition_dict = {}

    while True:
        try:
            current_letter = next(letters)
            if current_letter in repetition_dict:
                repetition_dict[current_letter] += 1
            else:
                repetition_dict.update({current_letter: 1})
        except:
            return len(list(filter(lambda item: repetition_dict[item] > 1, repetition_dict)))


if __name__ == "__main__":
    print(repetitions("abcde"))
    print(repetitions("aabbcde"))
    print(repetitions("aabBcde"))
    print(repetitions("indivisibility"))
    print(repetitions("Indivisibilities"))
    print(repetitions("aA11"))
    print(repetitions("ABBA"))
