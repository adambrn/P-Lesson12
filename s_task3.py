""" Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1. """

class FactorialGenerator:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 1
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.step = step

    def factorial(self, num):
        if num == 0:
            return 1
        else:
            return num * self.factorial(num - 1)

    def __iter__(self):
        current = self.start
        while current <= self.stop:
            yield self.factorial(current)
            current += self.step


if __name__ == "__main__":
    gen1 = FactorialGenerator(1, 5)
    for num in gen1:
        print(num)

    gen2 = FactorialGenerator(1, 10, 2)
    for num in gen2:
        print(num)
    