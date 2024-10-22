class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self, sound):
        print(f"{self.name} разговаривает с нами так: {sound}")

    def eat(self, animal_eat):
        print(f"{self.name} кушает: {animal_eat}")

class Bird(Animal):
    def __init__(self, name="Ворона", age="100 лет", sound="Кар-кар", animal_eat="Сыр"):
        super().__init__(name, age)  # Вызов конструктора родительского класса
        self.sound = sound
        self.animal_eat = animal_eat

class Mammal(Animal):
    def __init__(self, name="Дикий бык", age="10 лет", sound="Муу", animal_eat="Трава"):
        super().__init__(name, age)  # Вызов конструктора родительского класса
        self.sound = sound
        self.animal_eat = animal_eat

class Reptile(Animal):
    def __init__(self, name="Уж", age="5 лет", sound="Шшш", animal_eat="Насекомые"):
        super().__init__(name, age)  # Вызов конструктора родительского класса
        self.sound = sound
        self.animal_eat = animal_eat

class Veterinarian:
    def heal_animal(self):
        print("Ветеринар лечит животных")

class Zookeeper:
    def feed_animal(self):
        print("Служитель зоопарка ухаживает за животными")


class Zoo:
    def __init__(self,name,age,veterinarian,zookeeper):
        self.people_lst = []
        self.animal_lst = []
        self.name = Animal(name,age)
        self.veterinarian = Veterinarian()
        self.zookeeper = Zookeeper()



    def set_people(self):
        people_info = {"ФИО работника": input("Введите ФИО сотрудника ZOO: "), "Специальность": input("Введите рабочую специальность сотрудника: ")}
        self.people_lst.append(people_info)

    def set_animal(self):
        animal_info = {"Имя животного": input("Введите имя животного для ZOO: ")}
        self.animal_lst.append(animal_info)

    def get_info(self):  # Новый метод для возврата информации
        return self.animal_lst, self.people_lst

def animal_sound():

    name = "Еще не задано"
    age = "Еще не задано"
    veterinarian = "Еще не задано"
    zookeeper = "Еще не задано"

    zooGK = Zoo(name,age,veterinarian,zookeeper)

    for i in range(3):
        if i ==0:
            print("Для птицы: ")
        if i ==1:
            print("Для млекопитающего: ")
        if i == 2:
            print("Для рептилии: ")
        zooGK.set_animal()

    for i in range(2):
        if i == 0:
            print("Для Ветеринара: ")
        if i == 1:
            print("Для Служителя зоопарка: ")
        zooGK.set_people()

    print(zooGK.get_info())

    # Создаем список экземпляров класса Bird
    animal_list = [Bird(),Mammal(),Reptile()]

    for animal in animal_list:
        animal.make_sound(animal.sound)  # Вызываем метод make_sound для экземпляра

animal_sound()