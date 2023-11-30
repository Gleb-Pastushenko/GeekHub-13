# 1. Напишіть програму, де клас «геометричні фігури» (Figure) містить властивість color з початковим значенням white
# і метод для зміни кольору фігури, а його підкласи «овал» (Oval) і «квадрат» (Square) містять методи __init__ для
# завдання початкових розмірів об'єктів при їх створенні.

class Figure:
    def __init__(self):
        self._color = 'white'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


class Oval(Figure):
    def __init__(self, radius1, radius2):
        super().__init__()

        self.radius1 = radius1
        self.radius2 = radius2


class Square(Figure):
    def __init__(self, side):
        super().__init__()

        self.side = side


if __name__ == "__main__":
    oval = Oval(10, 20)

    square = Square(15)

    print(oval.color)
    print(square.color)

    print(f'radius 1: {oval.radius1}')
    print(f'radius 2: {oval.radius2}')

    print(f'square side: {square.side}')
