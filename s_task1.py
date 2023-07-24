""" 1. Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
Экземпляр должен запоминать последние k рассчитанных факториалов.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
"""
class Factorial:
    def __init__(self, k):
        self.k = k
        self.res = []

    def __call__(self, n):
        factorial = self._factorial(n)
        self.res.append({n: factorial})
        self.res = self.res[-self.k:]
        return factorial

    def _factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self._factorial(n - 1)

    def get_last(self):
        return self.res


f = Factorial(5)
f1 = f(5)
f2 = f(6)
f3 = f(7)
f4 = f(8)
f5 = f(9)
f6 = f(10)
print(f.get_last())
