# 4. Create 'list'-like object, but index starts from 1 and index of 0 raises error.
# Тобто це повинен бути клас, який буде поводити себе так, як list (маючи основні методи), але індексація повинна починатись із 1

class MyList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getitem__(self, index):
        if index == 0:
            raise IndexError()
        elif index > 0:
            return super().__getitem__(index - 1)
        else:
            return super().__getitem__(index)

    def __setitem__(self, index, value):
        if index == 0:
            raise IndexError()
        elif index > 0:
            super().__setitem__(index - 1, value)
        else:
            super().__setitem__(index, value)


if __name__ == "__main__":
    lst = MyList((1, 2, 3))

    print(f'{lst[1]=}')
    print(f'{lst[3]=}')
    print(f'{lst[-1]=}')
    print(f'{lst[-3]=}')
    lst[1] = -1
    lst[-1] = -3
    print(f'{lst[1]=}')
    print(f'{lst[-1]=}')
    print(lst)
    print(f'{lst[0]=}')
