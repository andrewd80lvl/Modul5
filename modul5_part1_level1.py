
class StringVar:
    def __init__(self, data):
        self.__string = data

    def set(self,data):
        self.__string = data

    def get(self):
        return self.__string

    # Конкатенация
    def __add__(self, other):
        if not isinstance(other, StringVar | str):
            raise ValueError('Складывать между собой допускаеться только классы StringVar и строки')

        if isinstance(other, StringVar):
            self.__string += other.get()
        else:
            self.__string += other

        return StringVar(self.__string)

    def __radd__(self, other):
        return self + other


test = StringVar("Текст")
print(test.get())

test.set("Новая строка")

print(test.get())
new = StringVar(" с текстом")

test = test + new
print(test.get())

test = str('и яблоками') + test
print(test.get())

# Вывод:
# Текст
# Новая строка
# Новая строка с текстом
# Новая строка с текстоми яблоками
