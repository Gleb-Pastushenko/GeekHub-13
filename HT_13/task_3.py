# 3. Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.

class InstanceCounter():
    counter = 0

    def __init__(self):
        self.__class__.counter += 1


if __name__ == "__main__":
    inst1 = InstanceCounter()
    inst2 = InstanceCounter()
    inst3 = InstanceCounter()

    print(InstanceCounter.counter)
