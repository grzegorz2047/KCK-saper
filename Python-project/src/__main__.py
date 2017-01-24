import pygame
import map
import saper
import bomb
import recognize_words
import sys
reload(sys)
sys.setdefaultencoding('utf8')

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (107, 113, 122)
yellow = (228, 239, 71)
saper_color = (38, 51, 73)
saper_head = (40, 0, 200)
bomb_color = (102, 0, 51)
floor = (249, 137, 17)


map = map.Map()
saper = saper.Saper()
bomb = bomb.Bomb()

walls = [] # lista scian
map.Load('example_map')

window_width = 992
window_height = 800
FPS = 30

gameDisplay = pygame.display.set_mode((window_width, window_height))

chat = recognize_words.Chat(gameDisplay)

pygame.display.set_caption('Saper')

gameExit = False

clock = pygame.time.Clock()

while not gameExit: #game_loop
    for event in pygame.event.get(): #event_loop
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            #CZAT
            chat.ask(event)

            if event.key == pygame.K_ESCAPE:
                gameExit = True

    saper.Update()
    bomb.Update()
    chat.Update()

    gameDisplay.fill(blue)
    map.Render()
    saper.Render()
    bomb.Render()
    chat.Render()

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
quit()