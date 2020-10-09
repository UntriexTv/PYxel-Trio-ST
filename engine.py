# This engine was specialy created for pyweek castaway
import pathlib

import pygame, pickle, time

# Variables
##############################
red = (250, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)


class animation_player():
    def __init__(self, time):
        self.state = False
        self.number = 0
        self.animation_change = pygame.USEREVENT
        pygame.time.set_timer(self.animation_change, time)

    def set_animation(self, left=[], right=[], idle=[]):
        self.animation_idle = idle
        self.animation_left = left
        self.animation_right = right
        self.animation_state = self.animation_idle

    def get_current_animation(self):
        return self.animation_state[self.number]

    def update_state(self, state):
        if state == "idle" and self.animation_state != self.animation_idle:
            self.number = 0
            self.animation_state = self.animation_idle
        elif state == "left" and self.animation_state != self.animation_left:
            self.number = 0
            self.animation_state = self.animation_left
        elif state == "right" and self.animation_state != self.animation_right:
            self.number = 0
            self.animation_state = self.animation_right

    def animation_next(self):
        if len(self.animation_state) - 1 <= self.number:
            self.number = 0
        else:
            self.number += 1


class animation_block():
    def __init__(self, time):
        self.number = 0
        self.animation_event = pygame.USEREVENT + 2
        pygame.time.set_timer(self.animation_event, time)

    def set_animation(self, animation=[]):
        self.animation = animation

    def get_current_animation(self):
        return self.animation[self.number]

    def animation_next(self):
        if len(self.animation) - 1 <= self.number:
            self.number = 0
        else:
            self.number += 1


class load():
    def __init__(self):
        pass

    def load_list(self, screen, list, image, mapx=0, mapy=0, rig_list=[]):
        # list should be in format [[x,y], [x,y]]
        for i in list:
            cache = screen.blit(image, (i[0] - mapx, i[1] - mapy))
            rig_list.append(cache)

    def load_rotated(self, screen, rotation, image, xko, yko):
        screen.blit(pygame.transform.rotate(image, rotation), (xko, yko))
        pygame.display.update()

    def load_npc_list(self, screen, list, date, mapx=0, mapy=0, rig_list=[]):
        for i in list:
            if not i.inactive:
                if int(i.time_date[1]) > date.time_hours > int(i.time_date[0]) and date.days[date.date_day] in \
                        i.time_date[2]:
                    cache = screen.blit(i.texture, (i.x - mapx, i.y - mapy))
                    rig_list.append(cache)

    def load_list_point(self, screen, list, image, mapx=0, mapy=0, rig_list=[]):
        # list should be in format [[x,y], [x,y]]
        for i in list:
            screen.blit(image, (i[0] - mapx, i[1] - mapy))
            rig_list.append(i)


class map():
    def __init__(self):
        self.map_wood = []
        self.map_grass = []
        self.map_roof = []
        self.spawn = []
        self.map_floor = []
        self.map_npc = []
        self.map_chair = []
        self.map_point = []
        self.map_enchant = []
        self.map_point_g = []
        self.map_bush = []
        self.map_rock = []
        self.map_table = []
        self.map_npc_g = []

    def load_files(self):
        patch_to_map = "./map/map_new/"
        try:
            with open("./map/map_new/map.dat", 'rb') as fp:
                self.cache = pickle.load(fp)
            fp.close()
            self.spawn = self.cache[9]
            self.map_grass = self.cache[0]
            self.map_wood = self.cache[1]
            self.map_roof = self.cache[2]
            self.map_floor = self.cache[3]
            self.map_chair = self.cache[4]
            self.map_npc = self.cache[5]
            self.map_point = self.cache[6]
            self.map_point_g = self.cache[7]
            self.map_enchant = self.cache[8]
            self.map_bush = self.cache[10]
            self.map_rock = self.cache[11]
            self.map_table = self.cache[12]
            self.map_npc_g = self.cache[13]
        except:
            print("failed to load map file")

    def save_points(self):
        for i in self.cache[6]:
            if i not in self.map_point:
                self.cache[6].remove(i)
        for i in self.cache[7]:
            if i not in self.map_point_g:
                self.cache[7].remove(i)
        cache = [self.map_grass, self.map_wood, self.map_roof, self.map_floor, self.map_chair, self.map_npc,
                 self.map_point, self.map_point_g, self.map_enchant, self.spawn, self.map_bush, self.map_rock,
                 self.map_table, self.map_npc_g]
        with open("./map/map_new/map.dat", 'wb') as fp:
            pickle.dump(cache, fp)
        fp.close()


class optimize():
    def __init__(self):
        pass

    def optimize(self, map, load, xmap, ymap, height, width, range=170):
        cache = []
        for i in map:
            if xmap - range < i[0] < width + xmap + range and ymap - range < i[1] < height + ymap + range:
                cache.append(i)
        if load != cache:
            load.clear()
            for i in cache:
                load.append(i)


class date():
    def __init__(self):
        self.time_min = 0
        self.time_hours = 0
        self.date_day = 0
        self.days = ["monday", "thursday", "wednesday", "thurstday", "friday", "saturday", "sunday"]
        self.timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer, 1000)

    def second(self, timeskip):
        if 60 < self.time_min + timeskip:
            while 60 < self.time_min + timeskip:
                self.time_min -= 60
                self.time_hours += 1
            self.time_min += timeskip
            while 24 < self.time_hours:
                self.date_day += 1
                self.time_hours -= 24
                if 6 < self.date_day:
                    self.date_day = 0
        else:
            self.time_min += timeskip


class Npc():
    def __init__(self, npc_list, number, position, texture, screen):
        self.file = open(npc_list[number][1] + ".txt", "r")
        for i in range(-1, position):
            self.dialog = self.file.readline().split("#")
        self.list = npc_list
        self.number = number
        self.position = position
        self.inactive = False
        self.fontmenu34 = pygame.freetype.Font('shpinscher.otf', 34)
        try:
            self.x = self.list[self.number][0][self.position][0]
            self.y = self.list[self.number][0][self.position][1]
            self.time_date = npc_list[self.number][0][self.position][2]
            self.coins = npc_list[self.number][0][self.position][3]
        except:
            self.inactive = True
        self.name = npc_list[number][1]
        self.texture = texture
        self.win = screen
        self.near = False
        self.talk_cache = 0

    def update(self, texture):
        self.texture = texture

    def run(self, xmap, ymap, player_rig):
        self.win.blit(self.texture, (int(self.x - xmap), int(self.y - ymap)))
        self.rig = pygame.Rect(self.x - 25 - xmap, self.y - 25 - ymap, 150, 150)
        if player_rig.colliderect(self.rig) == 1:
            self.near = True
        else:
            self.near = False

    def talk(self, win, width, height):
        for i in self.dialog:
            if "/P" in i:
                lists = i.replace("/P", "Player: ").split("/n")
            elif "/N" in i:
                lists = i.replace("/N", self.name + ": ").split("/n")
            pygame.draw.rect(win, (0, 0, 0), (width * 0.2, height * 0.6, width * 0.6, height * 0.3))
            while True:
                for evt in pygame.event.get():
                    if evt.type == pygame.QUIT:
                        pygame.quit()
                pygame.draw.rect(win, (0, 0, 0), (width * 0.2, height * 0.6, width * 0.6, height * 0.3))
                if len(lists) == 1:
                    self.fontmenu34.render_to(win, (width * 0.23, height * 0.63), lists[0], (150, 150, 150))

                if len(lists) == 2:
                    self.fontmenu34.render_to(win, (width * 0.23, height * 0.63), lists[0], (150, 150, 150))
                    self.fontmenu34.render_to(win, (width * 0.23, height * 0.695), lists[1], (150, 150, 150))

                if len(lists) == 3:
                    self.fontmenu34.render_to(win, (width * 0.23, height * 0.63), lists[0], (150, 150, 150))
                    self.fontmenu34.render_to(win, (width * 0.23, height * 0.695), lists[1], (150, 150, 150))
                    self.fontmenu34.render_to(win, (width * 0.23, height * 0.755), lists[2], (150, 150, 150))

                if len(lists) == 4:
                    self.fontmenu34.render_to(win, (width * 0.23, height * 0.63), lists[0], (150, 150, 150))
                    self.fontmenu34.render_to(win, (width * 0.23, height * 0.695), lists[1], (150, 150, 150))
                    self.fontmenu34.render_to(win, (width * 0.23, height * 0.755), lists[2], (150, 150, 150))
                    self.fontmenu34.render_to(win, (width * 0.23, height * 0.815), lists[3], (150, 150, 150))
                time.sleep(0.1)
                keyboard = pygame.key.get_pressed()
                if keyboard[pygame.K_RETURN]:
                    break
                pygame.display.update()
        self.dialog = self.file.readline().split("#")
        self.position += 1

        try:
            self.time_date = self.list[self.number][0][self.position][2]
            self.coins = self.list[self.number][0][self.position][3]
            self.x = self.list[self.number][0][self.position][0]
            self.y = self.list[self.number][0][self.position][1]
        except:
            self.inactive = True


class Gui():
    def text(self, win, x, y, text, colour=(0, 0, 0), size=10, font="Agency FB"):
        cache = pygame.freetype.Font(font, size)
        cache.render_to(win, (x, y), text, (colour))
