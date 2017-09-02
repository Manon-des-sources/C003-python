# coding=utf-8
#!python3

# =======================================================================
"""
来源：代码清单16-7
问题：现代艺术-随机矩形
接口：
"""

# =======================================================================
# globals 

# =======================================================================
# modules section

import sys
import random
import pygame

from pygame.color import THECOLORS

screen_size = [640, 480]


# RGB 颜色(colordict.py里面有完整定义)
color_black = [0  ,0  ,0  ]
color_white = [255,255,255]
color_red   = [255,0  ,0  ]
color_green = [0  ,255,0  ]
color_blue  = [0  ,0  ,255]
color_list  = [color_red, color_green, color_blue]

pygame.init()
screen = pygame.display.set_mode(screen_size)
screen.fill(color_white)
for i in range(100):
    # 矩形的尺寸与位置
    left   = random.randint(0, 500)
    top    = random.randint(0, 400)
    width  = random.randint(0, 250)
    height = random.randint(0, 100)
    rect_position = [left, top, width, height]
    # 颜色
    rect_color = random.randint(0, color_list.__len__() - 1)
    rect_color = color_list[rect_color]
    pygame.draw.rect(screen, color_green, rect_position, 2)     # 线宽 = 2，线宽 = 0 表示填充
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()