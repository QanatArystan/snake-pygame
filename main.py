import pygame, sys
from button import Button
from snake import Snake

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
GRID_SIZE = 40
BLOCK_SIZE = GRID_SIZE - 2
HEIGHT = SCREEN.get_height() // GRID_SIZE
WIDTH = SCREEN.get_width() // GRID_SIZE

BG = pygame.image.load("assets/Background.png")




def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

#game logic
def play():
    clock = pygame.time.Clock()
    running = True
    dt = 0


    grid = [[0] * (WIDTH + 1) for _ in range(HEIGHT + 1)]
    zeros = []

    dtx = dty = 0

    snake = Snake(WIDTH // 2, HEIGHT // 2)
    snake.apple = [5,5]


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        SCREEN.blit(BG, (0, 0))
        apple = pygame.Rect(snake.apple[0] * GRID_SIZE, snake.apple[1] * GRID_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, "red", apple)
        # apple1 = pygame.Rect((WIDTH - 1) * GRID_SIZE, HEIGHT * GRID_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        # pygame.draw.rect(SCREEN, "red", apple1)


        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and [dtx, dty] != [0, 1]:
            dty = -1
            dtx = 0
        if keys[pygame.K_s] and [dtx, dty] != [0, -1]:
            dty = 1
            dtx = 0
        if keys[pygame.K_a] and [dtx, dty] != [1, 0]:
            dty = 0
            dtx = -1
        if keys[pygame.K_d] and [dtx, dty] != [-1, 0]:
            dty = 0
            dtx = 1

        print(snake.x + dtx, snake.y + dty)

        if snake.x + dtx < 0 or snake.x + dtx == WIDTH or snake.y + dty < 0 or snake.y + dty == HEIGHT:
                running = False
                print("error")
                game_over()
        elif [snake.x, snake.y] in snake.body:
            running = False
            game_over()


        snake.update(dtx, dty, zeros)
        grid = [[0] * (WIDTH + 1) for _ in range(HEIGHT + 1)]
        grid[snake.y][snake.x] = 1

        for block in snake.body:
            grid[block[1]][block[0]] = 1


        for column in range(HEIGHT):
            for row in range(WIDTH):
                if grid[column][row] == 1:
                    rect = pygame.Rect((row + 0) * GRID_SIZE, (column + 0) * GRID_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                    pygame.draw.rect(SCREEN, "chartreuse3", rect)
                elif grid[column][row] == 0:
                    zeros.append([row, column])

        bar = pygame.Surface((SCREEN.get_width(), GRID_SIZE), pygame.SRCALPHA)  # per-pixel alpha
        bar.fill((200, 200, 200, 128))  # notice the alpha valued in the color
        SCREEN.blit(bar, (0, 0))
        str = f'Score: {snake.count}\n'
        MENU_TEXT = get_font(20).render(str, True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(100, 20))

        SCREEN.blit(MENU_TEXT, MENU_RECT)


        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(10) / 1000


def game_over():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("GAME OVER", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 400),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("SNAKE", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 400), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()