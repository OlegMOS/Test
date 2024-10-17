class TaskManager:
    def __init__(self, task, time, result):
        self.task = task
        self.time = time
        self.result = result
        self.spisok = {'Задача: ': "Нет", 'Срок: ': "Нет", 'Выполнение: ': None}

    def create_task(self):
        self.spisok = {'Задача: ': self.task, 'Срок: ': self.time}

    def set_result(self):
        if self.result.lower() == "да":
            self.spisok['Выполнение: '] = True
        else:
            self.spisok['Выполнение: '] = False

    def show_spisok(self):
        print(self.spisok)

# Создание экземпляра класса
Task1 = TaskManager(
    input("Введите содержание задачи: "),
    input("Введите срок выполнения задачи: "),
    input("Если задача закрыта, то введите Да (Нет - не выполнена): ")
)

# Создание задачи и установка результата
Task1.create_task()
Task1.set_result()
Task1.show_spisok()





