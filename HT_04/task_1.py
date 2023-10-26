# Написати скрипт, який приймає від користувача два числа (int або float) і робить наступне:
# Кожне введене значення спочатку пробує перевести в int.
# У разі помилки - пробує перевести в float, а якщо і там ловить помилку - пропонує ввести значення ще раз
# (зручніше на даному етапі навчання для цього використати цикл while)
# Виводить результат ділення першого на друге.
# Якщо при цьому виникає помилка - оброблює її і виводить відповідне повідомлення

def inputValue(prompt_text):
    input_val = None

    while not input_val:    
        input_val = input(f'{prompt_text}:  ')
        
        try:
            input_val = int(input_val)
        except:
            try:
                input_val = float(input_val)
            except:
                print("Input value neither int nor float, try again!")
                input_val = None
    return input_val

if __name__ == "__main__":
    dividend = inputValue("Input dividend")
    divider = inputValue("Input divider")

    try:
        print(dividend/divider)
    except Exception as err:
        print(err)
