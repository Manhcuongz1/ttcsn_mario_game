import pygame
from . import setup, tools


def main():
    pygame.init()
    run = True
    # setup screen
    setup_background()
    setup_text_background()

    # vòng lặp xử lý game
    pygame.display.update()
    #  event = pygame.event
    while run :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    setup.START = True
                if event.key == pygame.K_s :
                    if setup.START == False and setup.PLAY_GAME == False :
                        screen_setting()
                if event.key == pygame.K_b :
                    if setup.START == False and setup.PLAY_GAME == False :
                        setup_background()
                        setup_text_background()


        if setup.START:
            screen_delay_start_game()
            setup.START = False  # thiết lập lại màn khởi động bằng False nghĩa là tắt màn khởi động
            setup.PLAY_GAME = True  # thiết lập màn chơi game bằng True nghĩa là bắt đầu màn game
        # di chuyển màn hình
        if setup.PLAY_GAME:
            screen_update()
        # # mở setting
        # if setup.START == False and setup.PLAY_GAME == False:
        #     screen_setting()
        pygame.display.update()


def setup_background():
    background = setup.GFX['level_1']
    background_rect = background.get_rect()
    background = pygame.transform.scale(background,
                                        (int(background_rect.width * 2.69),
                                         int(background_rect.height * 2.679)))
    setup.SCREEN.blit(background, (0, 0))
    viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)
    image_dict = {}
    image = tools.get_image(setup.GFX['title_screen'], 1, 60, 176, 88,
                            (255, 0, 220), 2.5)
    rect = image.get_rect()  # get_rect lấy ra khung bao quanh ảnh đó, dùng để xác định vị trí khi va trạm
    rect.x, rect.y = (170, 100)
    image_dict['GAME_NAME_BOX'] = (image, rect)
    setup.SCREEN.blit(image, (170, 100))


def setup_text_background():
    setup.SCREEN.blit(setup.LABLE_SCORE, (40, 10))
    setup.SCREEN.blit(setup.SCORE, (40, 40))

    setup.SCREEN.blit(setup.LABLE_COIN, (240, 10))
    setup.SCREEN.blit(setup.COIN, (265, 40))

    setup.SCREEN.blit(setup.LABLE_WORLD, (440, 10))

    setup.SCREEN.blit(setup.LABLE_TIME, (640, 10))
    setup.SCREEN.blit(setup.TIME, (675, 40))

    setup.SCREEN.blit(setup.ENTER_PLAY_GAME, (150, 350))

    setup.SCREEN.blit(setup.LABLE_SETTING,(150,410))

    setup.SCREEN.blit(setup.LABLE_TOP_SCORE, (150, 480))
    setup.SCREEN.blit(setup.TOP_SCORE, (300, 480))


def screen_delay_start_game():
    frame = setup.GFX['text_images']
    frame_rect = frame.get_rect()
    frame = pygame.transform.scale(frame,
                                   (int(frame_rect.width * 3.06),
                                    int(frame_rect.height * 2.61)))
    setup.SCREEN.blit(frame, (0, 0))
    pygame.display.update()
    pygame.time.delay(1000)
    screen_play_game()
    pygame.display.update()

def screen_play_game():
    background = setup.GFX['level_1']
    background_rect = background.get_rect()
    background = pygame.transform.scale(background,
                                        (int(background_rect.width * 2.69),
                                         int(background_rect.height * 2.679)))
    setup.SCREEN.blit(background, (setup.LOCATION_MAP_X, 0))
def screen_update():
    # nhấn giữ nút RIGHT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        setup.LOCATION_MAP_X -= 5 # cập nhật toạ độ của ảnh
        screen_play_game()
        keys = pygame.key.get_pressed()
    # nhấn giữ nhất LEFT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        setup.LOCATION_MAP_X += 5 # cập nhật toạ độ của ảnh
        screen_play_game()
        keys = pygame.key.get_pressed()
def screen_setting() :
    # tải hình ảnh background và thay đổi kích thước
    background_image = setup.GFX['backgrmario']
    background_image = pygame.transform.scale(background_image, (800, 600))
    setup.SCREEN.blit(background_image, (0, 0))
    setup.SCREEN.blit(setup.LABLE_BACK, (10, 10))
