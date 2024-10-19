class User:
    def __init__(self,identificator,name,level):
        self.__identificator = identificator
        self.__name = name
        self.__level = level
        self.__user = []

    def __add(self,identificator,name,level):
        self.__user.append(f"{identificator},{name},{level}")

    def __delete_user(self,identificator):
        del self.__user[identificator]

class Admin(User):
    def __init__(self, identificator, name, level,admin):
        super(). __init__(identificator, name,level)
        self.admin = admin
    def get_add(self):

        identificator = input (f"Введите id пользователя: ")
        name = input(f"Введите имя пользователя: ")
        level = input(f"Введите права пользователя: ")

        self.__add(identificator, name, level)

        print(f"Добавлены следующие пользователи {[self.__add]}")

    def set_del(self):
        identificator = input(f"Введите id пользователя для удаления: ")
        self.__delete_user(identificator)

id_user = input(f"Введите свой ID: ")

if id_user == "100":
    Admin1 = Admin
    choice = input(f"1 - Добавить пользователя, 2 - Удалить пользователя: ")
    if choice == "1":
        Admin.get_add()
    if choice == "2":
        Admin.set_del()
    else:
        choice = input(f"Выберите правильный номер действия: 1 - Добавить пользователя, 2 - Удалить пользователя: ")
else:
    print("У вас нет прав на заведение и удаление пользователей")
