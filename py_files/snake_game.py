import pygame
import time
import random

pygame.init()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

display_width = 600
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pygame')
pygame.display.update()

clock = pygame.time.Clock()

block_size = 20
fps = 19


def text_objects(msg, color):
    font = pygame.font.SysFont(name='arial', size=25)
    textSurface = font.render(msg, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color):
    # screen_text = font.render(msg, True, color)
    # gameDisplay.blit(screen_text, [200, 200])
    # pygame.display.update()
    textSurf, textRect = text_objects(msg, color)
    textRect.center = display_width/2, display_height/2
    gameDisplay.blit(textSurf, textRect)


def generate_apple(snakeList):
    randAppleX = round((random.randrange(0, display_width - block_size + 1)) / 20) * 20
    randAppleY = round((random.randrange(0, display_height - block_size + 1)) / 20) * 20
    if [randAppleX, randAppleY] in snakeList:
        return generate_apple(snakeList)
    else:
        return randAppleX, randAppleY


def snake(snakeList):
    for s in snakeList:
        pygame.draw.rect(gameDisplay, green, [s[0], s[1], block_size, block_size])


def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = block_size
    lead_y_change = 0

    snakeList = []
    snakeLength = 2

    randAppleX, randAppleY = generate_apple(snakeList)

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

            if event.type == pygame.QUIT:
                gameExit = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        if lead_x + block_size > display_width or lead_x < 0 or lead_y + block_size > display_height or lead_y < 0:
            gameOver = True
        else:
            snakeHead = [lead_x, lead_y]
            snakeList.append(snakeHead)

            if snakeHead in snakeList[:-1]:
                gameOver = True
            else:
                if len(snakeList) > snakeLength:
                    del snakeList[0]

                if (lead_x == randAppleX) and (lead_y == randAppleY):
                    randAppleX, randAppleY = generate_apple(snakeList)
                    snakeLength += 1

                gameDisplay.fill(gray)
                pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])
                snake(snakeList=snakeList)
                pygame.display.update()

        clock.tick(fps)

        while gameOver:
            gameDisplay.fill(gray)
            message_to_screen('press C to play Q to quit', blue)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        gameOver = False
                        gameExit = True

    pygame.quit()  # this uninitialize the pygame
    quit()  # this exits from python


gameLoop()




















# if event.type == pygame.KEYUP:
#     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#         lead_x_change = 0
# gameDisplay.fill((255, 0, 0), [400, 100, 50, 50])
# if (lead_x == 0 or lead_x + block_size == display_width) and (lead_y + block_size < display_height) and (lead_y > 0):
# gameExit = False
# elif (lead_y == 0 or lead_y + block_size == display_height) and (lead_x + block_size < display_width) and (lead_x > 0):
# gameExit = False


# with out passing objects as arguments to the function if we change the object variables it will change the object variables like in snake function