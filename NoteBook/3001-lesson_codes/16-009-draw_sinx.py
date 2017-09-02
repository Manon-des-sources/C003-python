# coding=utf-8
#!python3

# =======================================================================
"""
来源：代码清单16-9
问题：绘制sinx曲线
接口：
"""

# =======================================================================
# globals 

# =======================================================================
# modules section

import sys
import math
import pygame

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

plotPoints = []

for x in range(640):
    y = math.sin(x/640.0 * 4 * math.pi)
    y = y * 200 + 240
    y = int(y)
    plotPoints.append([x, y])                                   # 收集数据点
pygame.draw.lines(screen, color_green, False, plotPoints, 1)    # 把数据点连成线(False = 不连接起点和终点)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()