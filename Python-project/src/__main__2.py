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

map = map.Map()
saper = saper.Saper()
bomb = bomb.Bomb()

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


            #sterowanie strzalkami
            if event.key == pygame.K_LEFT and saper.saper_x > 0:
                saper.saper_x -= saper.saper_width
                saper.direction = 3
            if event.key == pygame.K_RIGHT and saper.saper_x < window_width - saper.saper_width:
                saper.saper_x += saper.saper_width
                saper.direction = 2
            if event.key == pygame.K_DOWN and saper.saper_y < 448 - saper.saper_height:
                saper.saper_y += saper.saper_height
                saper.direction = 1
            if event.key == pygame.K_UP and saper.saper_y > 0:
                saper.saper_y -= saper.saper_height
                saper.direction = 0
            #---------------------

            #test
            if event.key == pygame.K_t:
                if saper.walk == False:
                    saper.Move(5)
            if event.key == pygame.K_r:
                saper.Rotate()

    saper.Update()
    #bomb.Update()
    gameDisplay.fill(blue)
    map.Render()
    saper.Render()
    bomb.Render()
    pygame.display.update()

    clock.tick(FPS)



pygame.quit()
quit()