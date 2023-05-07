from . import setup
from . import tools


def player() :
    image = tools.get_image(setup.GFX['mario_bros'], 80, 32, 15, 16,
                            (255, 0, 220), 3)
    rect = image.get_rect()  # get_rect lấy ra khung bao quanh ảnh đó, dùng để xác định vị trí khi va trạm
    rect.x, rect.y = (170, 100)
    image_dict = {}
    image_dict['PLAYER'] = (image, rect)
    setup.SCREEN.blit(image, (setup.LOCATION_PLAYER_X, 490))
def player_jum():
    image = tools.get_image(setup.GFX['mario_bros'], 80, 32, 15, 16,
                            (255, 0, 220), 3)
    rect = image.get_rect()  # get_rect lấy ra khung bao quanh ảnh đó, dùng để xác định vị trí khi va trạm
    rect.x, rect.y = (170, 100)
    image_dict = {}
    image_dict['PLAYER'] = (image, rect)
    setup.SCREEN.blit(image, (setup.LOCATION_PLAYER_X, 690))