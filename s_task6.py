#Изменяем класс прямоугольника.
#Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.
class SizeValidator:
    """
    Дескриптор для валидации размера (длины и ширины) прямоугольника.
    """

    def __init__(self, attribute_name):
        self.attribute_name = "_" + attribute_name

    def __get__(self, instance, owner):
        return getattr(instance, self.attribute_name)

    def __set__(self, instance, value):
        if value >= 0:
            setattr(instance, self.attribute_name, value)
        else:
            raise ValueError(f"{self.attribute_name} не может быть отрицательным.")

class Rectangle:
    """
    Класс Rectangle, представляет прямоугольник с длиной и шириной.
    Поддерживает операции сложения и вычитания прямоугольников, а также сравнение по площади.
    """
    __slots__=('_length', '_width',)
    
    def __init__(self, length, width=None):
        self._length = 0
        self._width = 0
        self.length = length
        self.width = length if width is None else width

    length = SizeValidator("length")
    width = SizeValidator("width")


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
    
    print(Rectangle(-1,5))