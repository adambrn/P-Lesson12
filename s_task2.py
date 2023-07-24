#Доработаем задачу 1.
#Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.

import json

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
    
class SaveToJson:
    def __init__(self, file_path, instance):
        self.file_path = file_path
        self.instance = instance

    def __enter__(self):
        return self.instance

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.file_path, 'w') as file:
            json.dump(self.instance.get_last(), file)
s = Factorial(5)
with SaveToJson('factorial_values.json',s):
    f1 = s(5)
    f2 = s(6)
    f3 = s(7)
    f4 = s(8)
    f5 = s(9)
    f6 = s(10)
    print(s.get_last())
