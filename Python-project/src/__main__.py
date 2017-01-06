import pygame
import map
import saper
import bomb

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
saper_color = (255, 128, 0)
bomb_color = (102, 0, 51)

map = map.Map()
saper = saper.Saper()
bomb = bomb.Bomb()

walls = [] # lista scian

map.Load('example_map')

window_width = 800
window_height = 600
FPS = 15

gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Saper')

gameExit = False

clock = pygame.time.Clock()

while not gameExit: #game_loop
    for event in pygame.event.get(): #event_loop
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameExit = True
            if event.key == pygame.K_LEFT and saper.rect.x > 0:
                saper.direction = 3
                if saper.walk == False:
                    saper.Move(1)
            if event.key == pygame.K_RIGHT and saper.rect.x < window_width - saper.saper_width:
                saper.direction = 2
                if saper.walk == False:
                    saper.Move(1)
            if event.key == pygame.K_DOWN and saper.rect.y < 448 - saper.saper_height:
                saper.direction = 1
                if saper.walk == False:
                    saper.Move(1)
            if event.key == pygame.K_UP and saper.rect.y > 0:
                saper.direction = 0
                if saper.walk == False:
                    saper.Move(1)

            #test
            if event.key == pygame.K_t:
                if saper.walk == False:
                    saper.Move(5)
            if event.key == pygame.K_r:
                saper.Rotate()
            if event.key == pygame.K_y:
                saper.Pick_up()

    saper.Update()
    bomb.Update()
    gameDisplay.fill(blue)
    map.Render()
    saper.Render()
    bomb.Render()
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
quit()