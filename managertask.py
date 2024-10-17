class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнена" if self.completed else "Не выполнена"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        new_task = Task(description, deadline)
        self.tasks.append(new_task)
        print(f"Задача добавлена: {description}")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
            print(f"Задача '{self.tasks[task_index].description}' отмечена как выполненная.")
        else:
            print("Некорректный индекс задачи.")

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def show_pending_tasks(self):
        pending_tasks = self.get_pending_tasks()
        if not pending_tasks:
            print("Нет невыполненных задач.")
        else:
            print("Невыполненные задачи:")
            for index, task in enumerate(pending_tasks):
                print(f"{index}. {task}")


def main():
    manager = TaskManager()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Показать невыполненные задачи")
        print("4. Выйти")

        choice = input("Ваш выбор: ")

        if choice == '1':
            description = input("Введите описание задачи: ")
            deadline = input("Введите срок выполнения задачи: ")
            manager.add_task(description, deadline)

        elif choice == '2':
            manager.show_pending_tasks()
            task_index = int(input("Введите индекс задачи, которую хотите отметить как выполненную: "))
            manager.mark_task_completed(task_index)

        elif choice == '3':
            manager.show_pending_tasks()

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")

main()
