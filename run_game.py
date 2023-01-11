import engine, time, threading, pygame.freetype, os
try:
    import pygame
except:
    import pip
    pip.main(["install", "pygame"])
    import pygame

res = '1200x600'
fullscreen = False
width = 1200
height = 600
big = 60  # pixel size of block

pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Castaway")

# Fonts settings
pygame.freetype.init()
fontmenu30 = pygame.freetype.Font('shpinscher.otf', 30)
fontmenu34 = pygame.freetype.Font('shpinscher.otf', 34)
fontmenu70 = pygame.freetype.Font('shpinscher.otf', 70)
fontmenu60 = pygame.freetype.Font('shpinscher.otf', 60)
fontmenu50 = pygame.freetype.Font('shpinscher.otf', 50)
fontmenu100 = pygame.freetype.Font('shpinscher.otf', 100)
fontmenu150 = pygame.freetype.Font('shpinscher.otf', 150)

# sound settings
sound = 1
vol = 0.5
pygame.mixer.init()
pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play(-1)


def credloop():
    win.fill((0, 0, 0))
    cred = True
    while cred:
        time_pygame.tick(30)

        fontmenu100.render_to(win, (int(width // 2 - 190), int(height // 2 - height // 4)), 'Matej Justus',
                              (150, 150, 150))
        fontmenu100.render_to(win, (int(width // 2 - 190), int(height // 2)), 'Filip Drábik', (150, 150, 150))
        fontmenu100.render_to(win, (int(width // 2 - 190), int(height // 2 + height // 4)), 'Lukáš Fedor',
                              (150, 150, 150))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                cred = False

        pygame.display.update()


def settloop():
    global res, win, width, height, vol, fullscreen
    win.fill((0, 0, 0))
    sett = True
    while sett:
        pygame.mixer.music.set_volume(vol)
        win.fill((0, 0, 0))
        time_pygame.tick(30)
        click = False
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                click = True

        tomenubut = pygame.Rect(int(width - 210), int(height - 110), 120, 70)
        pygame.draw.rect(win, (100, 100, 100), tomenubut, 3)

        resjedenbut = pygame.Rect(int(width // 17), int(height * 0.1), 330, 50)
        resdvabut = pygame.Rect(int(width // 17), int(height * 0.1 + 75), 330, 50)
        restribut = pygame.Rect(int(width // 17), int(height * 0.1 + 150), 330, 50)
        resstirybut = pygame.Rect(int(width // 17), int(height * 0.1 + 225), 330, 50)
        respatbut = pygame.Rect(int(width // 17), int(height * 0.1 + 300), 330, 50)
        ressestbut = pygame.Rect(int(width // 3), int(height * 0.1), 330, 50)
        ressedembut = pygame.Rect(int(width // 3), int(height * 0.1 + 75), 330, 50)
        resosembut = pygame.Rect(int(width // 3), int(height * 0.1 + 150), 330, 50)
        resdevetbut = pygame.Rect(int(width // 3), int(height * 0.1 + 225), 330, 50)
        resdesatbut = pygame.Rect(int(width // 3), int(height * 0.1 + 300), 330, 50)
        fsbut = pygame.Rect(int(width * 0.7), int(height * 0.1 + 225), 240, 50)
        volm = pygame.Rect(int(width * 0.7 + 40), int(height * 0.1 + 85), 20, 20)
        volp = pygame.Rect(int(width * 0.7 + 105), int(height * 0.1 + 85), 20, 20)

        fontmenu70.render_to(win, (int(width - 200), int(height - 100)), 'Back', (150, 150, 150))
        fontmenu70.render_to(win, (int(width // 17), int(height * 0.1)), '1000x500', (150, 150, 150))
        fontmenu70.render_to(win, (int(width // 17), int(height * 0.1 + 75)), '1200x600', (150, 150, 150))
        fontmenu70.render_to(win, (int(width // 17), int(height * 0.1 + 150)), '1200x800', (150, 150, 150))
        fontmenu70.render_to(win, (int(width // 17), int(height * 0.1 + 225)), '1280x720', (150, 150, 150))
        fontmenu70.render_to(win, (int(width // 17), int(height * 0.1 + 300)), '1366x768', (150, 150, 150))
        fontmenu70.render_to(win, (int(width // 3), int(height * 0.1)), '1440x900', (150, 150, 150))
        fontmenu70.render_to(win, (int(width // 3), int(height * 0.1 + 75)), '1680x1050', (150, 150, 150))
        fontmenu70.render_to(win, (int(width // 3), int(height * 0.1 + 150)), '1920x1080', (150, 150, 150))
        fontmenu70.render_to(win, (int(width // 3), int(height * 0.1 + 225)), '1920x1200', (150, 150, 150))
        fontmenu70.render_to(win, (int(width // 3), int(height * 0.1 + 300)), '2560x1440', (150, 150, 150))
        fontmenu70.render_to(win, (int(width * 0.7 + 105), int(height * 0.1 + 85)), '+', (150, 150, 150))
        fontmenu70.render_to(win, (int(width * 0.7 + 40), int(height * 0.1 + 93)), '_', (150, 150, 150))
        fontmenu70.render_to(win, (int(width * 0.7), int(height * 0.1)), 'Volume', (150, 150, 150))
        fontmenu50.render_to(win, (int(width * 0.7 + 70), int(height * 0.1 + 80)), str(round(vol * 10)),
                             (150, 150, 150))
        fontmenu70.render_to(win, (int(width * 0.7), int(height * 0.1 + 225)), 'Fullscreen', (150, 150, 150))

        if fsbut.collidepoint((mx, my)) and fullscreen == False:
            fontmenu70.render_to(win, (int(width * 0.7), int(height * 0.1 + 225)), 'Fullscreen', (50, 50, 50))
            if click:
                fullscreen = True

        if tomenubut.collidepoint((mx, my)):
            fontmenu70.render_to(win, (int(width - 200), int(height - 100)), 'Back', (50, 50, 50))
            if click:
                os.environ['SDL_VIDEO_CENTERED'] = '1'
                break

        if volp.collidepoint((mx, my)) and click and 0 < vol < 0.9:
            vol += 0.1

        if volm.collidepoint((mx, my)) and click and 0.1 < vol < 1:
            vol -= 0.1

        if fullscreen:
            res = 'fullscreen'
            screen_size = pygame.display.Info()
            win = pygame.display.set_mode((screen_size.current_w, screen_size.current_h), pygame.FULLSCREEN)
            width = screen_size.current_w
            height = screen_size.current_h
            fullscreen = False

        elif resjedenbut.collidepoint((mx, my)):
            fontmenu70.render_to(win, (int(width // 17), int(height * 0.1)), '1000x500', (50, 50, 50))
            if click:
                height = 500
                width = 1000
                res = '1000x500'
                win = pygame.display.set_mode((width, height))

        elif resdvabut.collidepoint((mx, my)):
            fontmenu70.render_to(win, (int(width // 17), int(height * 0.1 + 75)), '1200x600', (50, 50, 50))
            if click:
                height = 600
                width = 1200
                res = '1200x600'
                win = pygame.display.set_mode((width, height))

        elif restribut.collidepoint((mx, my)):
            fontmenu70.render_to(win, (int(width // 17), int(height * 0.1 + 150)), '1200x800', (50, 50, 50))
            if click:
                height = 800
                width = 1200
                res = '1200x800'
                win = pygame.display.set_mode((width, height))

        elif resstirybut.collidepoint((mx, my)):
            fontmenu70.render_to(win, (int(width // 17), int(height * 0.1 + 225)), '1280x720', (50, 50, 50))
            if click:
                height = 720
                width = 1280
                res = '1280x720'
                win = pygame.display.set_mode((width, height))

        elif respatbut.collidepoint((mx, my)):
            fontmenu70.render_to(win, (int(width // 17), int(height * 0.1 + 300)), '1366x768', (50, 50, 50))
            if click:
                height = 768
                width = 1366
                res = '1366x768'
                win = pygame.display.set_mode((width, height))

        elif ressestbut.collidepoint((mx, my)):
            fontmenu70.render_to(win, (int(width // 3), int(height * 0.1)), '1440x900', (50, 50, 50))
            if click:
                height = 900
                width = 1440
                res = '1440x900'
                win = pygame.display.set_mode((width, height))

        elif ressedembut.collidepoint((mx, my)):
            fontmenu70.render_to(win, (int(width // 3), int(height * 0.1 + 75)), '1680x1050', (50, 50, 50))
            if click:
                height = 1050
                width = 1680
                res = '1680x1050'
                win = pygame.display.set_mode((width, height))

        elif resosembut.collidepoint((mx, my)):
            fontmenu70.render_to(win, (int(width // 3), int(height * 0.1 + 150)), '1920x1080', (50, 50, 50))
            if click:
                height = 1080
                width = 1920
                res = '1920x1080'
                win = pygame.display.set_mode((width, height))

        elif resdevetbut.collidepoint((mx, my)):
            fontmenu70.render_to(win, (int(width // 3), int(height * 0.1 + 225)), '1920x1200', (50, 50, 50))
            if click:
                height = 1200
                width = 1920
                res = '1920x1200'
                win = pygame.display.set_mode((width, height))

        elif resdesatbut.collidepoint((mx, my)):
            fontmenu70.render_to(win, (int(width // 3), int(height * 0.1 + 300)), '2560x1440', (50, 50, 50))
            if click:
                height = 1440
                width = 2560
                res = '2560x1440'
                win = pygame.display.set_mode((width, height))

        if res == '1000x500':
            fontmenu70.render_to(win, (int(width // 17), int(height * 0.1)), '1000x500', (50, 50, 50))
        elif res == '1200x600':
            fontmenu70.render_to(win, (int(width // 17), int(height * 0.1 + 75)), '1200x600', (50, 50, 50))
        elif res == '1200x800':
            fontmenu70.render_to(win, (int(width // 17), int(height * 0.1 + 150)), '1200x800', (50, 50, 50))
        elif res == '1280x720':
            fontmenu70.render_to(win, (int(width // 17), int(height * 0.1 + 225)), '1280x720', (50, 50, 50))
        elif res == '1366x768':
            fontmenu70.render_to(win, (int(width // 17), int(height * 0.1 + 300)), '1366x768', (50, 50, 50))
        elif res == '1440x900':
            fontmenu70.render_to(win, (int(width // 3), int(height * 0.1)), '1440x900', (50, 50, 50))
        elif res == '1680x1050':
            fontmenu70.render_to(win, (int(width // 3), int(height * 0.1 + 75)), '1680x1050', (50, 50, 50))
        elif res == '1920x1080':
            fontmenu70.render_to(win, (int(width // 3), int(height * 0.1 + 150)), '1920x1080', (50, 50, 50))
        elif res == '1920x1200':
            fontmenu70.render_to(win, (int(width // 3), int(height * 0.1 + 225)), '1920x1200', (50, 50, 50))
        elif res == '2560x1440':
            fontmenu70.render_to(win, (int(width // 3), int(height * 0.1 + 300)), '2560x1440', (50, 50, 50))
        elif res == 'fullscreen':
            fontmenu70.render_to(win, (int(width * 0.7), int(height * 0.1 + 225)), 'Fullscreen', (50, 50, 50))

        pygame.display.update()


# textures/images:
###########################
# icons
sound_on = pygame.image.load('sound on.png').convert_alpha()
sound_off = pygame.image.load('sound off.png').convert_alpha()

# Player
#   idle
p_i_1 = pygame.transform.scale(pygame.image.load("./Textures/pl_standing.png").convert_alpha(), (big, big))
p_i_2 = pygame.transform.scale(pygame.image.load("./Textures/pl_standing_2.png").convert_alpha(), (big, big))
#   right
p_r_1 = pygame.transform.scale(pygame.image.load("./Textures/player_r_1.png").convert_alpha(), (big, big))
p_r_2 = pygame.transform.scale(pygame.image.load("./Textures/player_r_2.png").convert_alpha(), (big, big))
p_r_3 = pygame.transform.scale(pygame.image.load("./Textures/player_r_3.png").convert_alpha(), (big, big))
p_r_4 = pygame.transform.scale(pygame.image.load("./Textures/player_r_4.png").convert_alpha(), (big, big))
#   left
p_l_1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("./Textures/player_r_1.png")
                                                     .convert_alpha(), (big, big)), True, False)
p_l_2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("./Textures/player_r_2.png")
                                                     .convert_alpha(), (big, big)), True, False)
p_l_3 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("./Textures/player_r_3.png")
                                                     .convert_alpha(), (big, big)), True, False)
p_l_4 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("./Textures/player_r_4.png")
                                                     .convert_alpha(), (big, big)), True, False)
#   "dead"
p_d = pygame.transform.scale(pygame.image.load("./Textures/pl_down.png").convert_alpha(), (big, big))
# Player Ghost
p_s_1_g = pygame.transform.scale(pygame.image.load("./Textures/player_g.png").convert_alpha(), (big, big))
p_r_1_g = pygame.transform.scale(pygame.image.load("./Textures/player_g_r_1.png").convert_alpha(), (big, big))
p_r_2_g = pygame.transform.scale(pygame.image.load("./Textures/player_g_r_2.png").convert_alpha(), (big, big))
p_r_3_g = pygame.transform.scale(pygame.image.load("./Textures/player_g_r_3.png").convert_alpha(), (big, big))
p_l_1_g = pygame.transform.flip(pygame.transform.scale(pygame.image.load("./Textures/player_g_r_1.png").convert_alpha()
                                                       , (big, big)), True, False)
p_l_2_g = pygame.transform.flip(pygame.transform.scale(pygame.image.load("./Textures/player_g_r_2.png").convert_alpha()
                                                       , (big, big)), True, False)
p_l_3_g = pygame.transform.flip(pygame.transform.scale(pygame.image.load("./Textures/player_g_r_3.png").convert_alpha()
                                                       , (big, big)), True, False)

wood = pygame.transform.scale(pygame.image.load("./Textures/wood.png").convert_alpha(), (big, big))
roof = pygame.transform.scale(pygame.image.load("./Textures/roof.png").convert_alpha(), (big, big))
roof_transparent = pygame.transform.scale(pygame.image.load("./Textures/roof_transparent.png").convert_alpha(),
                                          (big, big))
chair = pygame.transform.scale(pygame.image.load("./Textures/chair.png").convert_alpha(), (big, big))
table = pygame.transform.scale(pygame.image.load("./Textures/table.png").convert_alpha(), (big, big))

bush = pygame.transform.scale(pygame.image.load("./Textures/bush.png").convert_alpha(), (big, big))
rock = pygame.transform.scale(pygame.image.load("./Textures/rock.png").convert_alpha(), (big, big))
floor = pygame.transform.scale(pygame.image.load("./Textures/floor.png").convert_alpha(), (big, big))
grass_b = pygame.transform.scale(pygame.image.load("./Textures/grass_block.png").convert_alpha(), (big, big))
npc_1_1 = pygame.transform.scale(pygame.image.load("./Textures/npc_2_1.png").convert_alpha(), (big, big))
npc_1_2 = pygame.transform.scale(pygame.image.load("./Textures/npc_2_2.png").convert_alpha(), (big, big))
npc_2_1 = pygame.transform.scale(pygame.image.load("./Textures/npc_3_1.png").convert_alpha(), (big, big))
npc_2_2 = pygame.transform.scale(pygame.image.load("./Textures/npc_3_2.png").convert_alpha(), (big, big))
npc_g_1 = pygame.transform.scale(pygame.image.load("./Textures/npc_g1.png").convert_alpha(), (big, big))
npc_g_2 = pygame.transform.scale(pygame.image.load("./Textures/npc_g2.png").convert_alpha(), (big, big))
point = pygame.transform.scale(pygame.image.load("./Textures/point.png").convert_alpha(), (big, big))
point_g = pygame.transform.scale(pygame.image.load("./Textures/point_g.png").convert_alpha(), (big, big))
enchant = pygame.transform.scale(pygame.image.load("./Textures/enchant.png").convert_alpha(), (big, big))
enchant1 = pygame.transform.scale(pygame.image.load("./Textures/enchant1.png").convert_alpha(), (big, big))
enchant2 = pygame.transform.scale(pygame.image.load("./Textures/enchant2.png").convert_alpha(), (big, big))
enchant3 = pygame.transform.scale(pygame.image.load("./Textures/enchant3.png").convert_alpha(), (big, big))

# Animations
#   player
#       right
p_r = [p_r_1, p_r_2, p_r_3, p_r_4, p_r_4, p_r_3, p_r_2, p_r_1]
#       left
p_l = [p_l_1, p_l_2, p_l_3, p_l_4, p_l_4, p_l_3, p_l_2, p_l_1]
#       idle
p_i = [p_i_1, p_i_2]
#       Settings
animation_player = engine.animation_player(80)
animation_player.set_animation(left=p_l, right=p_r, idle=p_i)
#   ghost
#       idle/right
g_i = [p_s_1_g, p_r_1_g, p_r_2_g, p_r_3_g, p_r_2_g, p_r_1_g]
#       left
g_l = [p_l_1_g, p_l_1_g, p_l_2_g, p_l_3_g, p_l_2_g, p_l_1_g]
#       Settings
animation_ghost = engine.animation_player(80)
animation_ghost.set_animation(left=g_l, right=g_i, idle=g_i)
#   enchant table
enchant_animation_l = [enchant1, enchant2, enchant3, enchant2]
#       Settings
enchant_animation = engine.animation_block(100)
enchant_animation.set_animation(enchant_animation_l)

# Player variables
rig_l, rig_r, rig_u, rig_d = 0, 0, 0, 0
player = p_i_1
player_g = p_s_1_g
npc_thread = False
npc_talking = 0
block_move = False
state = "idle"
timer = 10
enchant_true = False

# Game Variables
##################################
enable_optimize = True
delay = 12
time_pygame = pygame.time.Clock()
optimize = engine.optimize()
date = engine.date()
load = engine.load()
gui = engine.Gui()
dark = 0
dark_set = 128
night = 19
day = 6
run = True
wall_size = 100
timer_save = pygame.USEREVENT + 3
pygame.time.set_timer(timer_save, 5000)
menu_timer = 10
ghost_timer = 10
enchant_timer = 10
max_timer = 30
max_vel = 10
menu = True

#   Rigs
roof_rig = []
rig_list = []
points = []
points_g = []
enchant_rig = []

# map
map = engine.map()
map.load_files()

# Load save
try:
    save = open('save.txt', 'r')
    p_x = int(save.readline())
    p_y = int(save.readline())
    mode = int(save.readline())
    state_n = save.readline().split("#")
    c_x = int(save.readline())
    c_y = int(save.readline())
    xmap = int(save.readline())
    ymap = int(save.readline())
    date.time_hours = int(save.readline())
    date.time_min = int(save.readline())
    date.date_day = int(save.readline())
    set_vel = float(save.readline())
    timer_set = int(save.readline())
    number_of_points = int(save.readline())
    state_g = save.readline().split("#")
    save.close()
except:
    p_x = map.spawn[0][0]
    p_y = map.spawn[0][1]
    c_x = 2212
    c_y = 492
    set_vel = 3
    mode = 1
    xmap = 0
    ymap = 0
    state_n = [0, 0, 0]
    state_g = [0]
    timer_set = 10
    number_of_points = 0
    if p_x < 0:
        while p_x < 0:
            p_x += 10
            xmap -= 10
    elif 0 < p_x:
        while 0 < p_x:
            p_x -= 10
            xmap += 10
vel = set_vel

#Npc Ghost settings
ghost_animation = engine.animation_block(100)
ghost_animation.set_animation([npc_g_1, npc_g_1, npc_g_2, npc_g_2])
ghost_n = engine.Npc(map.map_npc_g, 0, int(state_g[0]), npc_g_1, win)
emily = engine.Npc(map.map_npc, 1, int(state_n[1]), npc_g_1, win)
npcs_g = [ghost_n]
# Npc People settings
bob_animation = engine.animation_block(100)
bob_animation.set_animation([npc_1_1, npc_1_1, npc_1_2, npc_1_2])
ema_animation = engine.animation_block(100)
ema_animation.set_animation([npc_2_1, npc_2_1, npc_2_2, npc_2_2])
man = engine.Npc(map.map_npc, 0, int(state_n[0]), npc_1_1, win)
npcs = [man, emily]


# definitions for menus
def collisions():
    global rig_l, rig_r, rig_u, rig_d, rig_list
    while True:
        if mode == 0:
            for i in rig_list:
                rig_d = player_rig_d.colliderect(i)
                if rig_d == 1:
                    break
            for i in rig_list:
                rig_u = player_rig_u.colliderect(i)
                if rig_u == 1:
                    break
            for i in rig_list:
                rig_l = player_rig_l.colliderect(i)
                if rig_l == 1:
                    break
            for i in rig_list:
                rig_r = player_rig_r.colliderect(i)
                if rig_r == 1:
                    break
        else:
            rig_l, rig_r, rig_u, rig_d = 0, 0, 0, 0
        time.sleep(0.05)


def optimalisation():
    while True:
        optimize.optimize(map.map_wood, load_wood, xmap, ymap, height, width, range=300)
        optimize.optimize(map.map_roof, load_roof, xmap, ymap, height, width, range=300)
        optimize.optimize(map.map_grass, load_grass, xmap, ymap, height, width, range=300)
        optimize.optimize(map.map_floor, load_floor, xmap, ymap, height, width, range=300)
        optimize.optimize(map.map_chair, load_chair, xmap, ymap, height, width, range=300)
        optimize.optimize(map.map_rock, load_rock, xmap, ymap, height, width, range=300)
        optimize.optimize(map.map_bush, load_bush, xmap, ymap, height, width, range=300)
        time.sleep(0.5)


def save_function():
    save = open("save.txt", "w")
    save.write(str(int(p_x)))
    save.write("\n")
    save.write(str(int(p_y)))
    save.write("\n")
    save.write(str(int(mode)))
    save.write("\n")
    for i in npcs:
        save.write(str(i.position))
        save.write("#")
    save.write("\n")
    save.write(str(int(c_x)))
    save.write("\n")
    save.write(str(int(c_y)))
    save.write("\n")
    save.write(str(int(xmap)))
    save.write("\n")
    save.write(str(int(ymap)))
    save.write("\n")
    save.write(str(date.time_hours))
    save.write("\n")
    save.write(str(date.time_min))
    save.write("\n")
    save.write(str(date.date_day))
    save.write("\n")
    save.write(str(set_vel))
    save.write("\n")
    save.write(str(timer_set))
    save.write("\n")
    save.write(str(number_of_points))
    save.write("\n")
    for i in npcs_g:
        save.write(str(i.position))
        save.write("#")
    save.close()
    map.save_points()


#Preparations to play
if enable_optimize:
    load_roof = []
    load_grass = []
    load_wood = []
    load_floor = []
    load_chair = []
    load_rock = []
    load_bush = []
    optimize_thread = threading.Thread(target=optimalisation, daemon=True)
    optimize_thread.start()
else:
    load_roof = map.map_roof
    load_grass = map.map_grass
    load_wood = map.map_wood
    load_floor = map.map_floor
    load_chair = map.map_chair
    load_rock = map.map_rock
    load_bush = map.map_bush
collision_thread = threading.Thread(target=collisions, daemon=True)
collision_thread.start()
load.load_list_point(win, map.map_point, point, mapx=xmap, mapy=ymap, rig_list=points)
load.load_list_point(win, map.map_point_g, point_g, mapx=xmap, mapy=ymap, rig_list=points_g)
screen_surface = pygame.Surface((width, height))
while run:
    click = False
    ghost_timer -= 10
    state = "idle"
    screen_surface = pygame.Surface((width, height))
    if p_x < 0:
        while p_x < 0:
            p_x += 10
            xmap -= 10
    elif 0 + width < p_x:
        while 0 < p_x:
            p_x -= 10
            xmap += 10
    time_pygame.tick()
    pygame.time.delay(delay)
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
        if evt.type == date.timer and block_move is False:
            date.second(10)
            if mode == 0:
                timer -= 1
        if evt.type == animation_player.animation_change:
            animation_player.animation_next()
            animation_ghost.animation_next()
        if evt.type == enchant_animation.animation_event:
            enchant_animation.animation_next()
            bob_animation.animation_next()
            ema_animation.animation_next()
            ghost_animation.animation_next()
            emily.update(ema_animation.get_current_animation())
            man.update(bob_animation.get_current_animation())
            ghost_n.update(ghost_animation.get_current_animation())

        if evt.type == timer_save:
            save_function()
        if evt.type == pygame.MOUSEBUTTONDOWN:
            click = True

    keyboard = pygame.key.get_pressed()

    if keyboard[pygame.K_g] and block_move is False:
        if mode == 1 and player_rig.colliderect(ghost_rig_cache) == 1 and ghost_timer < 0:
            mode = 0
            p_x = c_x - xmap
            p_y = c_y - ymap
            ghost_timer = 50
        elif mode == 0 and ghost_timer < 0:
            mode = 1
            c_x = p_x + xmap
            c_x_map = xmap
            c_y = p_y + ymap
            c_y_map = ymap
            ghost_timer = 50
    if keyboard[pygame.K_UP] and rig_u == 0 and block_move is False:
        if p_y - vel < wall_size:
            ymap -= vel
        else:
            p_y -= vel
        state = "right"
    if keyboard[pygame.K_RIGHT] and rig_r == 0 and block_move is False:
        if width - wall_size < p_x + big + vel:
            xmap += vel
        else:
            p_x += vel
        state = "right"
    if keyboard[pygame.K_DOWN] and rig_d == 0 and block_move is False:
        if height - wall_size < p_y + big + vel:
            ymap += vel
        else:
            p_y += vel
        state = "right"
    if keyboard[pygame.K_LEFT] and rig_l == 0 and block_move is False:
        if p_x - vel < wall_size:
            xmap -= vel
        else:
            p_x -= vel
        state = "left"
    if keyboard[pygame.K_ESCAPE] and rig_d == 0 and block_move is False:
        if 0 < menu_timer:
            menu = True
    else:
        if menu is False:
            menu_timer = 15
    if keyboard[pygame.K_r]:
        cache_sleep = 10
        cache_dark = 1
        while True:
            click = False
            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    click = True

            plusbut = pygame.Rect(width // 2 + 35, height // 2 + 7, 25, 25)
            minusbut = pygame.Rect(width // 2 - 35, height // 2 + 7, 25, 25)
            pygame.draw.rect(win, (0, 0, 0), (width // 2 - 35, height // 2 - 2, 95, 50))
            pygame.draw.rect(win, (0, 0, 0), plusbut)
            pygame.draw.rect(win, (0, 0, 0), minusbut)
            fontmenu50.render_to(win, (width // 2 - 5, height // 2), str(cache_sleep), (255, 255, 255))
            fontmenu70.render_to(win, (width // 2 + 37, height // 2 + 9), '+', (255, 255, 255))
            fontmenu70.render_to(win, (width // 2 - 32, height // 2 + 16), '_', (255, 255, 255))

            if plusbut.collidepoint((mx, my)) and click and cache_sleep < 24:
                cache_sleep += 1

            if minusbut.collidepoint((mx, my)) and click and cache_sleep > 0:
                cache_sleep -= 1

            keys = pygame.key.get_pressed()

            if keys[pygame.K_RETURN]:
                date.second(cache_sleep * 60)
                break
            pygame.display.update()

    animation_player.update_state(state)
    player = animation_player.get_current_animation()
    animation_ghost.update_state(state)
    ghost = animation_ghost.get_current_animation()
    win.fill((255, 255, 255))
    player_rig_l = pygame.Rect(int(p_x), int(p_y) + 10, 5, big - 20)
    player_rig_r = pygame.Rect(int(p_x) + big, int(p_y) + 10, 5, big - 20)
    player_rig_u = pygame.Rect(int(p_x) + 10, int(p_y), big - 20, 5)
    player_rig_d = pygame.Rect(int(p_x) + 10, int(p_y) + big, big - 20, 5)
    rig_list.clear()
    load.load_list(win, load_wood, wood, mapx=xmap, mapy=ymap, rig_list=rig_list)
    load.load_list(win, load_grass, grass_b, mapx=xmap, mapy=ymap)
    load.load_list(win, load_floor, floor, mapx=xmap, mapy=ymap)
    load.load_list(win, map.map_table, table, mapx=xmap, mapy=ymap)
    load.load_list(win, load_bush, bush, mapx=xmap, mapy=ymap, rig_list=rig_list)
    load.load_list(win, load_rock, rock, mapx=xmap, mapy=ymap)
    load.load_list(win, load_chair, chair, mapx=xmap, mapy=ymap, rig_list=rig_list)
    load.load_list_point(win, points, point, mapx=xmap, mapy=ymap)
    enchant_rig.clear()
    load.load_list(win, map.map_enchant, enchant_animation.get_current_animation(), mapx=xmap, mapy=ymap,
                   rig_list=enchant_rig)
    load.load_npc_list(win, npcs, date, mapx=xmap, mapy=ymap)
    if mode == 0:
        player_rig = win.blit(player, (p_x, p_y))
        for i in npcs:
            if not i.inactive:
                if int(i.time_date[1]) > date.time_hours > int(i.time_date[0]) and date.days[date.date_day] \
                        in i.time_date[2]:
                    i.run(xmap, ymap, player_rig)
                    if i.near:
                        pygame.draw.rect(win, (0, 0, 0), (p_x + 60, p_y - 30, 30, 30), 4)
                        fontmenu34.render_to(win, (int(p_x + 71), int(p_y - 26)), 'E', (250, 250, 250))
                        if keyboard[pygame.K_e]:
                            i.talk(win, width, height)
                            block_move = False
                            break
        if timer <= 0:
            mode = 1
            c_x = p_x + xmap
            c_x_map = xmap
            c_y = p_y + ymap
            c_y_map = ymap
        for i in points:
            if player_rig.collidepoint(i[0] - xmap + big // 2, i[1] + big // 2 - ymap):
                points.remove([i[0], i[1]])
                number_of_points += 1
                map.map_point.remove([i[0], i[1]])
        for i in enchant_rig:
            if player_rig.colliderect(i) and enchant_true is False:
                pygame.draw.rect(win, (0, 0, 0), (p_x + 60, p_y - 30, 30, 30), 4)
                fontmenu34.render_to(win, (p_x + 71, p_y - 26), 'E', (250, 250, 250))
                if keyboard[pygame.K_e] and enchant_timer < 10 and block_move is False:
                    time.sleep(0.1)
                    enchant_timer = -10
                    enchant_true = True
                    block_move = True
                    break
                else:
                    enchant_timer -= 1
        for i in roof_rig:
            if player_rig.colliderect(i) == 1:
                win.blit(player, (p_x, p_y))
                roof_rig.clear()
                load.load_list(win, load_roof, roof_transparent, mapx=xmap, mapy=ymap, rig_list=roof_rig)
                break
        else:
            roof_rig.clear()
            load.load_list(win, load_roof, roof, mapx=xmap, mapy=ymap, rig_list=roof_rig)
    else:
        player_rig = win.blit(p_d, (c_x - xmap, c_y - ymap))
        ghost_rig_cache = win.blit(ghost, (p_x, p_y))
        for i in npcs_g:
            if not i.inactive:
                if int(i.time_date[1]) > date.time_hours > int(i.time_date[0]) and date.days[date.date_day] \
                        in i.time_date[2] and int(i.coins) <= number_of_points:
                    i.run(xmap, ymap, ghost_rig_cache)
                    if i.near:
                        pygame.draw.rect(win, (0, 0, 0), (p_x + 60, p_y - 30, 30, 30), 4)
                        fontmenu34.render_to(win, (p_x + 71, p_y - 26), 'E', (250, 250, 250))
                        if keyboard[pygame.K_e]:
                            i.talk(win, width, height)
                            block_move = False
                            break
        if timer < timer_set:
            timer += 0.05

        load.load_list_point(win, points_g, point_g, mapx=xmap, mapy=ymap)
        for i in points_g:
            if ghost_rig_cache.collidepoint(i[0] - xmap + big // 2, i[1] + big // 2 - ymap):
                points_g.remove([i[0], i[1]])
                map.map_point_g.remove([i[0], i[1]])
                number_of_points += 1
        for i in roof_rig:
            if ghost_rig_cache.colliderect(i) == 1:
                roof_rig.clear()
                load.load_list(win, load_roof, roof_transparent, mapx=xmap, mapy=ymap, rig_list=roof_rig)
                break
        else:
            roof_rig.clear()
            load.load_list(win, load_roof, roof, mapx=xmap, mapy=ymap, rig_list=roof_rig)

    if night < date.time_hours or date.time_hours < day:
        if dark < dark_set:
            dark += 1
    else:
        if dark != 0:
            dark -= 1

    screen_surface.set_alpha(dark)
    screen_surface.fill((0, 0, 0))
    win.blit(screen_surface, (0, 0))
    fontmenu30.render_to(win, (width - 120, height - 90), str(date.time_hours) + " : " + str(date.time_min),
                         (100, 100, 100))
    fontmenu30.render_to(win, (width - 120, height - 60), "Points: " + str(number_of_points), (100, 100, 100))
    fontmenu30.render_to(win, (width - 120, height - 30), "Stamina: " + str(round(timer)), (100, 100, 100))
    fontmenu30.render_to(win, (30, 30), "FPS: " + str(round(time_pygame.get_fps())), (100, 100, 100))
    if menu:
        menu_timer -= 1
        block_move = True
        screen_surface.set_alpha(150)
        screen_surface.fill((0, 0, 0))
        win.blit(screen_surface, (0, 0))
        if keyboard[pygame.K_ESCAPE] and menu_timer < 0:
            menu = False
            block_move = False

        mx, my = pygame.mouse.get_pos()

        playbut = pygame.Rect(width // 17, height * 0.85 - 225, 100, 65)
        settbut = pygame.Rect(width // 17, height * 0.85 - 150, 200, 65)
        credbut = pygame.Rect(width // 17, height * 0.85 - 75, 175, 50)
        quitbut = pygame.Rect(width // 17, height * 0.85, 100, 50)
        musicbut = pygame.Rect(width - 70, 50, 32, 32)

        if sound == 0:
            win.blit(sound_off, (width - 70, 50))

        if sound == 1:
            win.blit(sound_on, (width - 70, 50))

        fontmenu70.render_to(win, (int(width // 17), int(height * 0.85 - 225)), 'Play', (150, 150, 150))

        fontmenu70.render_to(win, (int(width // 17), int(height * 0.85 - 150)), 'Settings', (150, 150, 150))

        fontmenu70.render_to(win, (int(width // 17), int(height * 0.85 - 75)), 'Credits', (150, 150, 150))

        fontmenu70.render_to(win, (int(width // 17), int(height * 0.85)), 'Quit', (150, 150, 150))

        fontmenu150.render_to(win, (int(width // 2 - 210), int(height // 8)), 'Soul Town', (150, 150, 150))

        if playbut.collidepoint((mx, my)):
            fontmenu70.render_to(win, (int(width // 17), int(height * 0.85 - 225)), 'Play', (50, 50, 50))
            if click:
                menu = False
                block_move = False

        if settbut.collidepoint((mx, my)):
            fontmenu70.render_to(win, (int(width // 17), int(height * 0.85 - 150)), 'Settings', (50, 50, 50))
            if click:
                settloop()

        if credbut.collidepoint((mx, my)):
            fontmenu70.render_to(win, (int(width // 17), int(height * 0.85 - 75)), 'Credits', (50, 50, 50))
            if click:
                credloop()

        if quitbut.collidepoint((mx, my)):
            fontmenu70.render_to(win, (int(width // 17), int(height * 0.85)), 'Quit', (250, 50, 50))
            if click:
                map.save_points()
                pygame.quit()

        if musicbut.collidepoint((mx, my)) and click and sound == 0:
            pygame.mixer.music.unpause()
            sound = 1

        elif musicbut.collidepoint((mx, my)) and click and sound == 1:
            pygame.mixer.music.pause()
            sound = 0
    if enchant_true:
        enchant_timer += 1
        pygame.draw.rect(win, (0, 0, 0), (width // 4, height // 4, width // 2, height // 2), 20)

        screen_surface = pygame.Surface((width // 2, height // 2))
        screen_surface.set_alpha(180)
        screen_surface.fill((0, 0, 0))
        win.blit(screen_surface, (width // 4, height // 4))

        fontmenu60.render_to(win, (int(width * 0.43), int(height // 3)), 'Enchants', (0, 0, 255))
        fontmenu50.render_to(win, (int(width * 0.3), int(height // 2 - 25)), '1.', (255, 0, 0))
        fontmenu50.render_to(win, (int(width * 0.3), int(height // 2 + 25)), '2.', (255, 0, 0))

        fontmenu50.render_to(win, (int(width * 0.35), int(height // 2 - 25)), 'Time', (255, 255, 255))
        fontmenu50.render_to(win, (int(width * 0.35), int(height // 2 + 25)), 'Speed', (255, 255, 255))

        fontmenu50.render_to(win, (int(width * 0.6), int(height // 2 - 25)), str(timer_set) + '/' + str(max_timer),
                             (255, 255, 255))
        fontmenu50.render_to(win, (int(width * 0.6), int(height // 2 + 25)), str(set_vel) + "/" + str(max_vel),
                             (255, 255, 255))

    if keyboard[pygame.K_1]:
        if 0 < number_of_points and timer_set < max_timer:
            number_of_points -= 1
            timer_set += 1
            time.sleep(0.2)
    if keyboard[pygame.K_2]:
        if 0 < number_of_points and set_vel < max_vel:
            number_of_points -= 1
            set_vel += 0.25
            time.sleep(0.2)
    if keyboard[pygame.K_e] and 10 < enchant_timer:
        enchant_timer = 20
        enchant_true = False
        block_move = False

    pygame.display.update()
