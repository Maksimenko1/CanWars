import pygame as pg
from pygame.locals import *
from icecream import ic



def man_run_quickly(show_man,start_home,dect_home,man_rect,man_rect_center,man_dist,man_step,man):
    if show_man:
        if start_home != dect_home:
            man_dist = dect_home - man_rect_center

            if start_home_rect.centerx > dect_home:
                if man_dist > 0:
                    show_man = False
            else:
                if man_dist < 0:
                    show_man = False

            if start_home > dect_home:
                man_rect_center -= man_step
            else:
                man_rect_center += man_step
            display.blit(man, man_rect)
            return show_man
def create_home(path: str, center_x, center_y, x_divider=1, y_divider=1):
    """
    добовляет дом
    :param path:
    :param center_x:
    :param center_y:
    :param x_divider:
    :param y_divider:
    :return: image, rect
    """
    image = pg.image.load(path)
    rect = image.get_rect()
    rect.center = (center_x // x_divider, center_y // y_divider)
    return image, rect
    
def key_123(show_menus, event):
    value = 0
    if True in show_menus and event.type == KEYDOWN:
        if event.key == K_1:
            value = 1
        if event.key == K_2:
            value = 2
        if event.key == K_3:
            value = 3
        if event.key == K_4:
            value = 4
        if event.key == K_5:
            value = 5
        if event.key == K_6:
            value = 6
        if event.key == K_7:
            value = 7
        if event.key == K_8:
            value = 8
        if event.key == K_9:
            value = 9

    return value


def blit_menu(show_menu, menu, home_rect_center, army_menu, some_color):
    if show_menu:
        army_menu_rect = army_menu.get_rect()
        army_menu_rect.right = menu_rect.right - army_padding
        display.blit(menu, home_rect_center)
        menu.fill(some_color)
        menu.blit(army_menu, army_menu_rect)


# Параметры окна
window_w, window_h = 500, 500

pg.init()

some_color = (255, 255, 255, 255)
CYAN = (66, 245, 221)
LIKE_BLUE = (255, 255, 240, 0)
display = pg.display.set_mode((window_w, window_h))
pg.display.set_caption("это я")

# картинка дома
home1, home1_rect = create_home('HOME LEVEL1.png', window_w, window_h, 15, 2)
home2, home2_rect = create_home('HOME LEVEL1.png', window_w, window_h, 4, 2)
home3, home3_rect = create_home('HOME LEVEL1.png', window_w, window_h, 10, 5)
start_home_rect = None
dest_home_rect = None
dest_home_menu = None
start_home_menu = None


# frames per second == FPS
fps = 30
clock = pg.time.Clock()

#  человечек
man = pg.image.load('юнит(свой).jpg')
show_man = False
man_rect = man.get_rect()
man_dist_x = 0
man_dist_y = 0
man_step_x = 1
man_step_y = 1
k = 0

# MENU
menu = pg.image.load('Blue_rectangle.png')
menu_rect = menu.get_rect()
show_menu1 = False
army_num = '0'
army_padding = 5  # px
show_menu2 = False
show_menu3 = False
# show_menus = []
# 1. Выбор шрифта
fontsize = 21
good_msg = pg.font.SysFont('comicsansms', fontsize)
# 2. Отрисовка текста на поверхности: render(text, antialias, color) -> Surface
# 3. Отрисовка поверхности

running = True
while running:

    army_num = int(army_num)

    # Обработка событий
    for event in pg.event.get():
        # Логика завершения игры
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_q:
                running = False
        # Логика расчета войск
        show_menus = [show_menu1, show_menu2, show_menu3]
        army_num += key_123(show_menus, event)

        # Скрыть меню по клавише enter
        if event.type == KEYDOWN:
            if event.key == K_KP_ENTER:
                show_menu1 = False
                show_menu2 = False
                show_menu3 = False
                army_num = 0

    mpos_x, mpos_y = pg.mouse.get_pos()
    mouse_touched_home1 = home1_rect.collidepoint(mpos_x, mpos_y)
    mouse_touched_home2 = home2_rect.collidepoint(mpos_x, mpos_y)
    mouse_touched_home3 = home3_rect.collidepoint(mpos_x, mpos_y)
    mouse_leftbtn_pressed = pg.mouse.get_pressed()[0]
    if mouse_leftbtn_pressed:
        if mouse_touched_home1:
            show_menu1 = True
        else:
            show_menu1 = False
            army_num = 0

        if mouse_touched_home2:
            show_menu2 = True
        else:
            show_menu2 = False
            army_num = 0

        if mouse_touched_home3:
            show_menu3 = True
        else:
            show_menu3 = False
            army_num = 0

    # логика узнавания x и y для ходьбы
    mouse_rightbtn_pressed = pg.mouse.get_pressed()[2]
    if mouse_rightbtn_pressed:
        if show_menu1 or show_menu2 or show_menu3:
            if show_menu1:  # start_home_menu
                start_home_rect = home1_rect
            if show_menu2:  # start_home_menu
                start_home_rect = home2_rect
            if show_menu3:  # start_home_menu
                start_home_rect = home3_rect
            if mouse_touched_home1:  # dest_home_mtouched
                dest_home_rect = home1_rect
            if mouse_touched_home2:  # dest_home_mtouched
                dest_home_rect = home2_rect
            if mouse_touched_home3:  # dest_home_mtouched
                dest_home_rect = home3_rect

            man_rect.center = start_home_rect.center
            dist_x = start_home_rect.centerx - dest_home_rect.centerx
            dist_y = start_home_rect.centery - dest_home_rect.centery

            if dist_y > dist_x:
                if dist_y != 0:
                    man_step_x = abs(dist_x / dist_y)
                    man_step_y = 1
            else:
                if dist_x != 0:
                    man_step_y = abs(dist_y / dist_x)
                    man_step_x = 1

            ic(man_step_y, man_step_x)
            ic(start_home_rect.centerx, start_home_rect.centery, dest_home_rect.centerx, dest_home_rect.centery, dist_y,
               dist_x)
            show_man = True
            show_menu1 = False
            show_menu2 = False
            show_menu3 = False

    # Конвертация текста в картинку
    army_num = str(army_num)
    army_menu = good_msg.render(army_num, False, CYAN)

    # Заливка экрана
    display.fill(LIKE_BLUE)

    # Отрисовка
    display.blit(home1, home1_rect)
    display.blit(home2, home2_rect)
    display.blit(home3, home3_rect)
    blit_menu(show_menu1, menu, home1_rect.center, army_menu, some_color)
    blit_menu(show_menu2, menu, home2_rect.center, army_menu, some_color)
    blit_menu(show_menu3, menu, home3_rect.center, army_menu, some_color)
    '''
    if show_man:
        if start_home_rect.centerx != dest_home_rect.centerx:
            man_dist_x = dest_home_rect.centerx - man_rect.centerx

            if start_home_rect.centerx > dest_home_rect.centerx:
                if man_dist_x > 0:
                    show_man = False
            else:
                if man_dist_x < 0:
                    show_man = False

            if start_home_rect.centerx > dest_home_rect.centerx:
                man_rect.centerx -= man_step_x
            else:
                man_rect.centerx += man_step_x
            display.blit(man, man_rect)
    '''
    man_run_quickly(show_man, start_home_rect.centerx, dest_home_rect.centerx, man_rect, man_rect.centerx, man_dist_x,
                    man_step_x, man)

    if start_home_rect.centery == dest_home_rect.centery:
        continue
    man_dist_y = dest_home_rect.centery - man_rect.centery
    if start_home_rect.centery > dest_home_rect.centery:
        if man_dist_y > 0:
            show_man = False
    else:
        if man_dist_y < 0:
            show_man = False
    if start_home_rect.centery > dest_home_rect.centery:
        man_rect.centery -= man_step_y
    else:
        man_rect.centery += man_step_y
    display.blit(man, man_rect)
    man_step_x = 1
    man_step_y = 1

    # Перерисовка экрана
    pg.display.update()

    # Выдержка FPS
    clock.tick(fps)

pg.quit()
