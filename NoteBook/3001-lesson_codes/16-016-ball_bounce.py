# coding=utf-8
#!python3

# =======================================================================
"""
来源：代码清单16-9
问题：小球反弹
接口：
"""

# =======================================================================
# globals 

# =======================================================================
# modules section

import sys
import math
import pygame

# RGB 颜色(colordict.py里面有完整定义)
color_black = [0  ,0  ,0  ]
color_white = [255,255,255]
color_red   = [255,0  ,0  ]
color_green = [0  ,255,0  ]
color_blue  = [0  ,0  ,255]
color_list  = [color_red, color_green, color_blue]

screen_size = [640, 480]
where_is_the_ball = '0000-photos\\beach_ball.png'
x = 50
y = 50
x_speed = 5     # 移动速度，正值表示正向移动、负值表示反向移动
y_speed = 5

# init 
pygame.init()
screen = pygame.display.set_mode(screen_size)   # 创建初始显示面
screen.fill(color_white)
# do something
my_ball = pygame.image.load(where_is_the_ball)  # 创建显示面对象

# 事件处理
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.time.delay(10)
    pygame.draw.rect(screen, color_white, [x, y, 90, 90], 0)
    x += x_speed
    y += y_speed
    if x > (screen.get_width() - 90)  or  x < 0 :
        x_speed = -x_speed
    if y > (screen.get_height() - 90)  or  y < 0 :
        y_speed = -y_speed
    screen.blit(my_ball, [x, y])        # [x, y]为beach_ball 图片左上角定点的坐标，图片宽度 = 90
    pygame.display.flip()
