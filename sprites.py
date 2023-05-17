# file created by david charles

import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint

vec = pg.math.Vector2

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        self.image = pg.transform.scale(game.player_img, (150,150))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(150, 660)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
        self.standing = False
        self.living = True
    # ...
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP
    
    def checkpos(self):
        if self.rect.x > WIDTH - 80:
            self.pos.x = WIDTH - 25
            self.vel.x = 0
            # print("i am off the right side of the screen...")
        if self.rect.x < -45:
            self.pos.x = 30
            self.vel.x = 0
            # print("i am off the left side of the screen...")
        if self.rect.y > HEIGHT:
            self.living = False
        

    def input(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
        # if keystate[pg.K_p]:
        #     if PAUSED == False:
        #         PAUSED = True
        #         print(PAUSED)
        #     else:
        #         PAUSED = False
        #         print(PAUSED)
            
        
    def mob_collide(self):
            hits = pg.sprite.spritecollide(self, self.game.enemies, True)
            if hits:
                print("you collided with an enemy...")
                
    def update(self):
        self.checkpos()
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        

class Mob(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.transform.scale(game.skel_img, (150,150))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = (1000, 1000)
        self.vel = vec(randint(1,5),randint(1,5))
        self.acc = vec(1,1)
        self.cofric = 0.01
    # ...
    def checkpos(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.x < 0:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y < 0:
            self.pos.y = 25
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
    def update(self):
        self.checkpos()
        # self.pos.x += self.vel.x
        # self.pos.y += self.vel.y
        # self.pos += self.vel
        self.rect.center = self.pos

class Boss(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.transform.scale(game.sking_img, (300,300))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = (700, 1000)
        self.vel = vec(randint(1,5),randint(1,5))
        self.acc = vec(1,1)
        self.cofric = 0.01
    def checkpos(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.x < 0:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y < 0:
            self.pos.y = 25
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
    def update(self):
        self.checkpos()
        # self.pos.x += self.vel.x
        # self.pos.y += self.vel.y
        # self.pos += self.vel
        self.rect.center = self.pos

class Platform(Sprite):
    def __init__(self, x, y, width, height, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant