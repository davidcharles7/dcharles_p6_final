# file created by david charles
WIDTH = 1440
HEIGHT = 720
PLAYER_ACC = 0.8
PLAYER_FRICTION = -0.2
PLAYER_JUMP = 15
PLAYER_GRAV = 1
MOB_ACC = 1
MOB_FRICTION = -0.12
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (173,216,230)
RED = (255, 50, 50)
GREEN = (140,200,120)
ORANGE = (255,165,0)
GRAY = (100,100,100)
FPS = 60 
RUNNING = True
SCORE = 0
PAUSED = False

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 60, WIDTH, 60 , GREEN, "normal"),
                #  (0, HEIGHT+200, WIDTH, 1, ORANGE, "normal"),
                #  (0, HEIGHT * 3 / 4, 100, 20, GRAY, "normal"),
                #  (150, 330 , 100, 20, GREEN, "bouncey"),
                #  (700, HEIGHT * 3 / 4, 100, 20, GRAY, "normal"),
                #  (500, HEIGHT * 3 / 4, 100, 20, GRAY, "normal"),
                #  (350, 200, 100, 20, GRAY, "normal"),
                #  (0, 100, 120, 20, GRAY, "normal"),
                ]