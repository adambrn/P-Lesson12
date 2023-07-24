#Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.

class Rectangle:
    """
    Класс Rectangle, представляет прямоугольник с длиной и шириной.
    Поддерживает операции сложения и вычитания прямоугольников, а также сравнение по площади.
    """
    __slots__=('_length', '_width',)
    
    def __init__(self, length, width=None):
        self._length = length
        self._width = length if width is None else width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value >= 0:
            self._length = value
        else:
            raise ValueError("Длина прямоугольника не может быть отрицательной.")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value >= 0:
            self._width = value
        else:
            raise ValueError("Ширина прямоугольника не может быть отрицательной.")

    def perimeter(self):
        """
        Периметр прямоугольника
        """
        return 2 * (self._length + self._width)

    def area(self):
        """
        Площадь прямоугольника
        """
        return self._length * self._width

    def __add__(self, other):
        """
        Сложение прямоугольников возвращает квадрат со сложенным периметром
        """
        total_perimeter = self.perimeter() + other.perimeter()
        return Rectangle(total_perimeter // 4)

    def __sub__(self, other):
        """
        Вычетание прямоугольников возвращает квадрат с разностью периметров
        если разность отрицательная - нулевой
        """
        result_perimeter = self.perimeter() - other.perimeter()
        new_perimeter = max(0, result_perimeter)
        return Rectangle(new_perimeter // 4)

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()


if __name__ == "__main__":
    
    print(Rectangle.__dict__)

  
