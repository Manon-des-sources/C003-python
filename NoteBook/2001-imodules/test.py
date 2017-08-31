#  coding=utf-8 
#! python3 
#  虽然指定了Python3、但每个module都同时适用于Python2 和Python3
#  如果一个module 只支持其中一个、在它的申明处会特别说明

# =======================================================================
# modules section

import pygame

pygame.init()
screen = pygame.display.set_mode([320, 240])
