import json

class Model:

    def __init__(self):
        self.title = 'Снежная королева'
        self.content = [0, 5, 10, 17, 29, 29, 34, 43, 45, 46, 47, 49, 52, 52, 55, 59, 73, 77, 89, 99]
        self.date_posted = '17:47 02.02.2023'
        self.autor = 'Ханс Кристиан Андерсен'

    def save(self):
        with open('save.json', 'w') as sh_file:  # Открываем файл на чтение

            print(model.__dict__)
            json.dump(model.__dict__, sh_file)

model = Model()
model.save()

