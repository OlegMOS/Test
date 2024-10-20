class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id  # Защищенный атрибут
        self.__name = name         # Защищенный атрибут
        self.__access_level = 'user'  # Уровень доступа по умолчанию

    # Метод для получения ID пользователя
    def get_user_id(self):
        return self.__user_id

    # Метод для получения имени пользователя
    def get_name(self):
        return self.__name

    # Метод для получения уровня доступа
    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name, admin_access_level):
        super().__init__(user_id, name)
        self.__access_level = 'admin'  # Уровень доступа для администратора
        self.__admin_access_level = admin_access_level  # Дополнительный уровень доступа

    # Метод для добавления пользователя
    def add_user(self, user_list, user):
        #if isinstance(user, User):
            user_list.append(user)
            print(f"User {user.get_name()} added.")
        #else:
        #    print("Only User instances can be added.")

    # Метод для удаления пользователя
    def remove_user(self, user_list, user):
        if user in user_list:
            user_list.remove(user)
            print(f"\nUser {user.get_name()} removed.")
        else:
            print("User not found in the list.")

    # Метод для получения уровня доступа администратора
    def get_admin_access_level(self):
        return self.__admin_access_level


# Пример использования:
user_list = []

# Создаем обычных пользователей
user1 = User(1, "Alice")
user2 = User(2, "Bob")

# Создаем администратора
admin = Admin(3, "Charlie", "full")
print("Администратор заведен под id = 3")


# Администратор добавляет пользователей
chek_admin = int(input(f"Для изменения данных пользователей введите id администратора: "))
print("")

if chek_admin == 3:
    admin.add_user(user_list, user1)
    admin.add_user(user_list, user2)

    # Выводим список пользователей
    print("Current users:")
    for user in user_list:
        print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

    # Администратор удаляет пользователя
    admin.remove_user(user_list, user1)

    # Выводим список пользователей после удаления
    print("Users after removal:")
    for user in user_list:
        print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")
else:
    print("Введенный id не принадлежит администратору")
