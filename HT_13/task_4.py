# 4. Create 'list'-like object, but index starts from 1 and index of 0 raises error.
# Тобто це повинен бути клас, який буде поводити себе так, як list (маючи основні методи), але індексація повинна починатись із 1

class MyList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getitem__(self, index):
        if index == 0:
            raise IndexError()
        elif index > 0:
            return self.copy()[index - 1]
        else:
            return self.copy()[index]

    def __setitem__(self, index, value):
        if index == 0:
            raise IndexError()
        elif index > 0:
            copy = self.copy()
            copy[index - 1] = value
            self = copy
        else:
            copy = self.copy()
            copy[index] = value
            self = copy


if __name__ == "__main__":
    lst = MyList((1, 2, 3))

    print(f'{lst[1]=}')
    print(f'{lst[3]=}')
    print(f'{lst[-1]=}')
    print(f'{lst[-3]=}')
    print(f'{lst[0]=}')
