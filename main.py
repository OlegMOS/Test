class User:
    def __init__(self, identificator, name, level):  # Исправлено init на __init__
        self.identificator = identificator
        self.__name = name
        self.__level = level
        self.__user = []

    def __add_user(self, identificator, name, level):  # Исправлено __add на __add_user
        self.__user.append(f"{identificator},{name},{level}")

    def __delete_user(self, identificator):  # Здесь нужно изменить способ удаления
        # Предполагается, что идентификатор – это индекс, но лучше использовать другой подход
        for i, user in enumerate(self.__user):
            if user.startswith(identificator + ","):  # Проверяем по идентификатору
                del self.__user[i]
                return
        print("Пользователь не найден.")


class Admin(User):
    def __init__(self, identificator, name, level, admin):  # Исправлено init на __init__
        super().__init__(identificator, name, level)  # Исправлено на super().__init__
        self.admin = admin

    def get_add(self):
        while True:
            identificator = input("Введите id пользователя: ")
            name = input("Введите имя пользователя: ")
            level = input("Введите права пользователя: ")

            self._User__add_user(identificator, name, level)  # Используем _User для доступа к защищенному методу
            choice = input(f"Продолжить (Да/Нет): ")
            if choice == "Нет":
                break
        print(f"Добавлены следующие пользователи: {self._User__user}")  # Добавлено отображение списка пользователей

    def set_del(self):
        identificator = input("Введите id пользователя для удаления: ")
        self._User__delete_user(identificator)  # Используем _User для доступа к защищенному методу
        print(f"Остались следующие пользователи: {self._User__user}")

# Основной блок выполнения
id_user = input("Введите свой ID: ")

if id_user == "100":
    admin = Admin(id_user, "AdminName", "High", True)  # Создаем экземпляр Admin

    while True:

        choice = input("1 - Добавить пользователя, 2 - Удалить пользователя, 3 - Завершить: ")

        if choice == "1":
            admin.get_add()  # Вызываем метод экземпляра
        elif choice == "2":
            admin.set_del()  # Вызываем метод экземпляра
        elif choice == "3":
            break
        else:
            print("Выберите правильный номер действия: 1 - Добавить пользователя, 2 - Удалить пользователя")
else:
    print("У вас нет прав на заведение и удаление пользователей.")





