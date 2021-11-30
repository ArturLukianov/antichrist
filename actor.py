import random
import math


from constants import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Actor:
    def __init__(self, name, pos, levels, level, tile, health, color=COLOR_WHITE):
        self.name = name
        self.pos = pos
        self.level = level
        self.levels = levels
        self.tile = tile
        self.health = health
        self.inventory = []
        self.levels[self.level].actors.append(self)
        self.is_alive = True
        self.color = color
        self.base_color = color
        self.damage = 1

    def move(self, dx, dy):
        self.pos.x += dx
        self.pos.y += dy

    def update_damage(self):
        self.damage = 1
        for item in self.inventory:
            if item.item_type == 'weapon' and item.equipped:
                self.damage += 1

    def receive_damage(self, damage, damager):
        if not self.is_alive: return
        self.health -= damage
        self.color = COLOR_RED
        if self.health <= 0:
            self.is_alive = False
            self.tile = ord('%')
            self.base_color = COLOR_RED

    def get_damage(self):
        return self.damage

    def update(self, ticks):
        if self.base_color != self.color:
            self.color = self.base_color

    def check_location(self):
        if self.pos.x <= 0 or self.pos.y <= 0 or \
           self.pos.x >= self.levels[self.level].width - 1 or self.pos.y >= self.levels[self.level].height - 1:
            if self.level == 'village':
                next_level = 'forest'
            else:
                next_level = 'village'
                
            if self.pos.x <= 0:
                self.pos.x = self.levels[next_level].width - 2
            elif self.pos.x >= self.levels[self.level].width - 1:
                self.pos.x = 1
            
            if self.pos.y <= 0:
                self.pos.y = self.levels[next_level].height - 2
            elif self.pos.y >= self.levels[self.level].height - 1:
                self.pos.y = 1

            self.levels[self.level].actors.remove(self)
            self.levels[next_level].actors.append(self)
            self.level = next_level


class Player(Actor):
    pass


