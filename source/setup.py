
import pygame as pg
from . import tools

pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
pg.display.set_caption("Mario")   #tên game
SCREEN = pg.display.set_mode((800,600))   # set độ rộng màn hình 
SCREEN_RECT = SCREEN.get_rect()

# bắt đầu game
START = False
PLAY_GAME = False
LOCATION_MAP_X = 0 # vị trí ban đầu ảnh tại x = 0

# SETUP TEXT - DETAIL
GFX = tools.load_all_gfx('assets')
font = pg.font.Font("C:\\Users\\cuong\\AppData\\Local\\Microsoft\\Windows\\Fonts\\joystixmonospace.ttf", 30)
# điểm
LABLE_SCORE = font.render("MARIO", True, (255, 255, 255))
SCORE = font.render("00000", True, (255, 255, 255))
# coin
COIN = font.render("00", True, (255, 255, 255))
LABLE_COIN = font.render("COIN", True, (255, 255, 255))
LABLE_WORLD = font.render("WORLD", True, (255, 255, 255))

# time
TIME = font.render("0", True, (255, 255, 255))
LABLE_TIME = font.render("TIME", True, (255, 255, 255))

# Enter play game
ENTER_PLAY_GAME = font.render("ENTER PLAY GAME", True, (255, 255, 255))

#TOP
LABLE_TOP_SCORE = font.render("TOP: ", True, (255, 255, 255))
TOP_SCORE= font.render("000", True, (255, 255, 255))

#SETTING
LABLE_SETTING = font.render("ENTER 'S' TO OPEN SETTING", True, (255, 255, 255))

#BACK_MAIN
LABLE_BACK = font.render("ENTER 'B' TO BACK", True, (255, 255, 255))


