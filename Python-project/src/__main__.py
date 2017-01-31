import sys

import pygame

from recognize_words import Chat
from bomb import Bomb
from game_map import GameMap
from saper import Saper
import xml.etree.cElementTree as ET

reload(sys)
sys.setdefaultencoding('utf8')


class Colors:
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

class FileController:
    def __init__(self):
        self.functions_file = ET.ElementTree(file='../Slownik/Funkcje.xml')
        self.objects_file = ET.ElementTree(file='../Slownik/Obiekty.xml')
        self.parameters_file = ET.ElementTree(file='../Slownik/Parametry.xml')


class GameLogic:
    def __init__(self, colors_arg):
        self.colors = colors_arg
        pass

    def loadMap(self, game_map):
        game_map.load('example_map')

    def runGameLoop(self, game_display, game_map, saper, bomb, chat, fps, file_controller):
        quitted = False

        clock = pygame.time.Clock()

        while not quitted:  # game_loop
            for event in pygame.event.get():  # event_loop
                if event.type == pygame.QUIT:
                    quitted = True
                if event.type == pygame.KEYDOWN:
                    # CZAT
                    chat.ask(event, saper, file_controller)

                    if event.key == pygame.K_ESCAPE:
                        quitted = True

            saper.update(game_map.walls)
            bomb.Update()
            chat.update()

            game_display.fill(self.colors.blue)
            game_map.render()
            saper.render()
            bomb.Render()
            chat.render()

            pygame.display.update()

            clock.tick(fps)


def __main__():
    pygame.init()
    window_width = 992
    window_height = 668
    fps = 30
    game_display = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Saper')

    file_controller = FileController()
    chat = Chat(game_display)
    game_logic = GameLogic(Colors())

    game_map = GameMap(game_logic, game_display)
    bomb = Bomb(game_logic, game_display)
    saper = Saper(game_logic, bomb, chat, game_display)

    game_logic.loadMap(game_map)

    game_logic.runGameLoop(game_display, game_map, saper, bomb, chat, fps, file_controller)
    pygame.quit()
    quit()


__main__()
