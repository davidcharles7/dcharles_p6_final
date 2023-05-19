# This file was created by: david charles
# Sources: 
# http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# https://www.youtube.com/@Kidscancode/videos
# https://www.youtube.com/watch?v=Ongc4EVqRjo&t=656s

# Images
# https://www.freepik.com/free-vector/dungeon-door-medieval-castle-with-wood-chest_38720947.htm#query=cartoon%20dungeon&position=29&from_view=keyword&track=ais
# https://stock.adobe.com/images/arches-in-wall-from-stone-bricks-in-ancient-classic-architecture-vector-cartoon-illustration-of-vintage-facade-of-castle-palace-or-temple-with-granite-blocks-and-arcade/477404666
# https://www.istockphoto.com/illustrations/throne-room 

# Goals
# Door Class will lead into new areas
# boss fight
# character items 

# import libs
import pygame as pg
import os
# import settings 
from os import path
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "Images")


# create game class in order to pass properties to the sprites file

class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Dungeons and Dungeons")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    # sprite and background images
    def load_data(self):
        self.player_img = pg.image.load(path.join(img_folder, "Wizard_Sprite.png")).convert()
        self.sking_img = pg.image.load(path.join(img_folder, "Skeleton_King_Sprite.png")).convert()
        self.skel_img = pg.image.load(path.join(img_folder, "Skeleton_Sprite.png")).convert()
        self.background1_img = pg.image.load(path.join(img_folder, "Background1.jpg")).convert()
        self.background2_img = pg.image.load(path.join(img_folder, "Background2.jpg")).convert()
        self.background3_img = pg.image.load(path.join(img_folder, "Background3.jpg")).convert()



    def new(self):
        # starting a new game
        self.load_data()


        # allows game to access sprites libraries
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.mob = Mob(self)
        self.boss = Boss(self)

        # adds boss to group
        self.all_sprites.add(self.boss)
        self.enemies.add(self.boss)

        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
            
        for i in range(0,1):
            m = Mob(self)
            self.all_sprites.add(m)
            self.enemies.add(m)

        self.all_sprites.add(self.player)

        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            # checkpos makes sure player stays inbounds
            self.player.checkpos()
            self.room_enter()
            self.events()
            self.update()
            self.draw()
            # print(self.player.pos.x)
    #blits text on screen
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
                #respawn only works if player is dead
                if event.key == pg.K_r:
                    if self.player.living == False:
                        self.player.pos = (50, 660)
                        self.player.living = True
        
    # room_enter checks player pos and changes entered bools if E key pressed
    def room_enter(self):
        keystate = pg.key.get_pressed()
        # door 1
        if self.player.rect.x < 175 and self.player.rect.x > 25: 
            # print("I can go in")
            if keystate[pg.K_e]:
                global ENTEREDR1
                ENTEREDR1 = True
                # print("I went in r1")
        # inside room 1
        if ENTEREDR1 == True:
            if self.player.rect.x < 500 and self.player.rect.x > 175:
                if keystate[pg.K_e]:
                    ENTEREDR1 = False
                    self.screen.blit(self.background1_img, (0,0))
                    # print("I left in r1")
            if self.player.rect.x < 850 and self.player.rect.x > 700:
                if keystate[pg.K_e]:
                    print("player wants to open chest")
        # door 2
        if self.player.rect.x < 625 and self.player.rect.x > 425: 
            # print("I can go in")
            if keystate[pg.K_e]:
                global ENTEREDR2
                ENTEREDR2 = True
                # print("I went in r1")
        # inside room 2
        if ENTEREDR2 == True:
            pass
            # if self.player.rect.x < 500 and self.player.rect.x > 175:
            #     if keystate[pg.K_e]:
            #         ENTEREDR1 = False
            #         self.screen.blit(self.background1_img, (0,0))
            #         # print("I left in r1")
            # if self.player.rect.x < 850 and self.player.rect.x > 700:
            #     if keystate[pg.K_e]:
            #         print("player wants to open chest")
                    
        
        

    def update(self):
        self.all_sprites.update()
        self.player.checkpos()
            
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.standing = True
                self.player.living = True
                if hits[0].variant == "danger":
                    self.player.standing = False
                    self.player.living = False
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
            else:
                self.player.standing = False
        

    def draw(self):
        self.player.checkpos()
        # if the player isn't in a room
        if ENTEREDR1 == False and ENTEREDR2 == False and ENTEREDR3 == False:
            self.screen.blit(self.background1_img, (0,0))
        # if in room 1
        if ENTEREDR1 == True:
            self.screen.blit(self.background2_img, (0,0))
        # in room 2
        if ENTEREDR2 == True:
            self.screen.blit(self.background3_img, (0,0))

        self.all_sprites.draw(self.screen)
        if self.player.standing:
            pass
        if self.player.living == False:
            self.draw_text("PRESS R TO RESPAWN", 72, WHITE, WIDTH/2, 100) 
        # if the player is in the main room 
        if ENTEREDR1 == False and ENTEREDR2 == False and ENTEREDR3 == False:
            if self.player.rect.x < 175 and self.player.rect.x > 25 and ENTEREDR1 == False: 
                self.draw_text("Press E to Enter...", 72, WHITE, WIDTH/2, 460) 
            if self.player.rect.x < 625 and self.player.rect.x > 425 and ENTEREDR2 == False: 
                self.draw_text("Press E to Enter...", 72, WHITE, WIDTH/2, 460) 
        # if the player entered room 1
        if ENTEREDR1 == True:
            if self.player.rect.x < 350 and self.player.rect.x > 175:
                self.draw_text("Press E to leave...", 72, WHITE, WIDTH/2, 460) 
            if self.player.rect.x < 800 and self.player.rect.x > 650:
                if HASKEY == False:
                    self.draw_text("You need a key to open the chest...", 72, WHITE, WIDTH/2, 460) 
                if HASKEY == True:
                    self.draw_text("Press E open the chest...", 72, WHITE, WIDTH/2, 460) 
            
        pg.display.flip()
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()