#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import sys

from inputbox import *


def get_textfield_value(screen, msg):
    textfield = ask(screen, msg)
    return textfield


def create_label(screen, msg, pos):
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    myfont = pygame.font.SysFont("monospace", 15)

    # render text
    label = myfont.render(msg, 1, (255, 255, 255))
    screen.blit(label, pos)
    pygame.display.flip()


def visualize():
    pygame.init()

    size = width, height = 800, 600
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Saper')
    ball = pygame.image.load('../assets/ball.bmp')
    ballrect = ball.get_rect()
    input_value = get_textfield_value(screen, 'Polecenie')
    print 'Wpisales', input_value
    random_msg = 'To jest testowa wiadomosc, bo fajnie jest widziec cos na ekranie!'
    while 1:
        # print 'loop!'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        create_label(screen, input_value, (100, 100))
        create_label(screen, random_msg, (200, 200))
        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.update(ballrect)  # aktualizuje pozycje kuli na ekranie

        # quit()
