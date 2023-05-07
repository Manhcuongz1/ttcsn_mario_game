import pygame

# khởi tạo Pygame
pygame.init()

# tạo màn hình game
screen = pygame.display.set_mode((800, 600))
In_font = pygame.font.Font('graphics\\joystixmonospace.ttf', 32)
instructions_text = In_font.render("Instructions", True, (255, 255, 255))
instructions_text_rect = instructions_text.get_rect(center=(400, 130))

screen = pygame.display.set_mode((800, 600))
Left_font = pygame.font.Font('graphics\\joystixmonospace.ttf', 20)
Left_text = Left_font.render("Left", True, (255, 255, 255))
Left_text_rect = Left_text.get_rect(x=170, y=290)

screen = pygame.display.set_mode((800, 600))
Right_font = pygame.font.Font('graphics\\joystixmonospace.ttf', 20)
Right_text = Right_font.render("Right", True, (255, 255, 255))
Right_text_rect = Right_text.get_rect(x=260, y=290)

screen = pygame.display.set_mode((800, 600))
Jump_font = pygame.font.Font('graphics\\joystixmonospace.ttf', 20)
Jump_text = Jump_font.render("Jump", True, (255, 255, 255))
Jump_text_rect = Jump_text.get_rect(x=450, y=290)
#tải hình ảnh background và thay đổi kích thước
background_image = pygame.image.load('graphics\\backgrmario.png')
background_image = pygame.transform.scale(background_image, (800, 600))
# tạo nút Back
Back_font = pygame.font.Font('graphics\\joystixmonospace.ttf', 32)
back_text = Back_font.render("Back", True, (255, 255, 255))

# căn chỉnh vị trí của văn bản "Back"
back_text_rect = back_text.get_rect(x=30, y=30)
# tải file âm thanh
#sound = pygame.mixer.Sound('HuongDan\\mariotheme.wav')

# phát âm thanh khi màn hình hiện lên
#sound.play()
# chạy vòng lặp game
running = True
while running:
    # xử lý các sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # kiểm tra xem người dùng có nhấn vào nút "Back" không
            if back_text_rect.collidepoint(event.pos):
                running = False

    # vẽ các đối tượng lên màn hình
    screen.blit(background_image, (0, 0))
    screen.blit(back_text, back_text_rect)
    screen.blit(instructions_text, instructions_text_rect)
    screen.blit(Left_text, Left_text_rect)
    screen.blit(Right_text, Right_text_rect)
    screen.blit(Jump_text, Jump_text_rect)
    # cập nhật màn hình
    pygame.display.update()

# kết thúc Pygame
pygame.quit()