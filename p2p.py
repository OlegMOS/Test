#__________________________________________________ ИГРА ТИР поймай яблоко______________________________________________
import pygame #импортируем библиотеку pygame
import random #импортируем библиотеку random
pygame.init() #инициализируем pygame

#__________________________________________________ ИГРОВОЕ ОКНО ______________________________________________________
# создаем игровое окно
SCREEN_WIDTH = 800 # задаем ширину окна Функция постоянная поэтому пишем всё заглавными буквами для себя, чтобы не забыть
SCREEN_HEIGHT = 600 # задаем высоту окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # создаём окно pygame с заданными параметрами ширины и высоты

pygame.display.set_caption("Игра - Поймай сбежавшее с дерева яблоко!           Кликай по яблоку, чтобы его поймать") # задаем заголовок окна
icon = pygame.image.load("img/1001.jpg") # загружаем иконку из папки img pyCharm данного проекта
pygame.display.set_icon(icon) # устанавливаем иконку в окно функции pygame

#рисуем цель
target_img = pygame.image.load("img/target.png") # загружаем иконку цели из папки img pyCharm
target_width = 80 # ширина цели
target_height = 80 # высота цели

target_x = random.randint(0, SCREEN_WIDTH - target_width) # генерируем координаты цели минус ширина цели
target_y = random.randint(0, SCREEN_HEIGHT - target_height) # генерируем координаты цели минус высота цели

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # генерируем цвет цели

# загружаем картинки деревьев, солнца и травы
tree1_img = pygame.image.load("img/tree1.png") # загружаем иконку дерева из папки img pyCharm
tree2_img = pygame.image.load("img/tree2.png") # загружаем иконку дерева из папки img pyCharm
tree3_img = pygame.image.load("img/tree3.png") # загружаем иконку дерева из папки img pyCharm

sun_img = pygame.image.load("img/Sun.png") # загружаем иконку cолнца из папки img pyCharm

trava1_img = pygame.image.load("img/trava1.png") # загружаем иконку травы из папки img pyCharm
trava2_img = pygame.image.load("img/trava2.png") # загружаем иконку травы из папки img pyCharm
trava3_img = pygame.image.load("img/trava3.png") # загружаем иконку травы из папки img pyCharm

paple1_img = pygame.image.load("img/paple1.png") # загружаем иконку paple1 из папки img pyCharm
paple2_img = pygame.image.load("img/paple2.png") # загружаем иконку paple2 из папки img pyCharm
paple3_img = pygame.image.load("img/paple3.png") # загружаем иконку paple3 из папки img pyCharm
paple4_img = pygame.image.load("img/paple4.png") # загружаем иконку paple4 из папки img pyCharm
paple5_img = pygame.image.load("img/paple5.png") # загружаем иконку paple5 из папки img pyCharm
paple6_img = pygame.image.load("img/paple6.png") # загружаем иконку paple6 из папки img pyCharm

#__________________________________________________ ИГРОВОЙ ЦИКЛ ______________________________________________________
# создаём игровой цикл
# создаем переменную running со значением истина
running = True # когда игра начинается и если надо остановить, то false присвоим переменной
while running: # цикл пока игра не закончится
    screen.fill(color) # задаем цвет фона на основе переменной color, которая дает рандомный цвет
    for event in pygame.event.get(): # создаём переменную событие, каждое событие содержит информацию о событии и будет сохранятся в переменной event
        if event.type == pygame.QUIT: # если нажата кнопка закрытия
            running = False # то игра закончится
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos() # получаем координаты мыши
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height: # если координаты цели больше координаты мыши# если координаты цели меньше координаты мыши
                target_x = random.randint(0, SCREEN_WIDTH - target_width) # генерируем координаты новой цели минус ширина цели
                target_y = random.randint(0, SCREEN_HEIGHT - target_height) # генерируем координаты новой цели минус высота цели

    # рисуем деревья на экране
    screen.blit(tree1_img, (20, 20))  # рисуем дерево 1
    screen.blit(tree2_img, (230, 250))  # рисуем дерево 2
    screen.blit(tree3_img, (400, 50))  # рисуем дерево 3 без яблок

    screen.blit(sun_img, (680, 10)) # рисуем солнце

    screen.blit(trava1_img, (255, 430))  # рисуем траву 1
    screen.blit(trava2_img, (0, 430)) # рисуем траву 2
    screen.blit(trava3_img, (510, 430))  # рисуем траву 3

    screen.blit(target_img, (target_x, target_y))  # рисуем цель

    screen.blit(paple1_img, (481, 60)) # рисуем paple 1
    screen.blit(paple2_img, (560, 70)) # рисуем paple 2
    screen.blit(paple3_img, (620, 130)) # рисуем paple 3
    screen.blit(paple4_img, (433, 131)) # рисуем paple 4
    screen.blit(paple5_img, (400, 223)) # рисуем paple 5
    screen.blit(paple6_img, (595, 228)) # рисуем paple 6

    pygame.display.update() # обновляем экран

pygame.quit() #закрываем окно с игрой pygame и выходим из программы когда running = False