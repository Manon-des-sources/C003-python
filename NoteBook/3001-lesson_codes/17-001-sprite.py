# coding=utf-8
#!python3

# =======================================================================
"""
来源：代码清单17-1
问题：sprite模块
接口：
"""

# =======================================================================
# globals 
# RGB 颜色(colordict.py里面有完整定义)
color_black = [0  ,0  ,0  ]
color_white = [255,255,255]
color_red   = [255,0  ,0  ]
color_green = [0  ,255,0  ]
color_blue  = [0  ,0  ,255]

# =======================================================================
# modules section
import sys
import math
import random
import pygame

# ========
# 创建蓝图
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)         # 继承Sprite 的属性数据
        # 使用继承来的属性数据
        self.image = pygame.image.load(image_file)  # 属性1 image --  初始化image
        self.rect  = self.image.get_rect()          # 属性2 rect  --  包含image边界的矩形对象
        self.rect.left, self.rect.top = location    # rect 的初始位置  --  初始化image的位置
        self.speed = speed                          # 属性3 私有属性  --  移动速度[Vx, Vy]

    def move(self):
        self.rect = self.rect.move(self.speed)      # 移动到新的位置
        if self.rect.left < 0  or  self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0  or  self.rect.bottom > height:
            self.speed[1] = -self.speed[1]


screen_size = width, height = [640, 480]

# 创建balls、每个ball 都是一个sprite 对象、每个ball 都是一个sprite 精灵
image_ball = '0000-photos\\beach_ball.png'
balls = []
for row in range(0, 3):
    for column in range(0, 3):
        location = [column * 180 + 10,  row * 180 + 10]
        speed    = [random.choice([-2, 2]), random.choice([-2, 2])]
        ball     = MyBallClass(image_ball, location, speed)
        balls.append(ball)

# 创建初始显示面
pygame.init()
screen = pygame.display.set_mode(screen_size)
screen.fill(color_white)

# 将balls 们放到初始位置
for ball in balls:
    screen.blit(ball.image, ball.rect)
pygame.display.flip()

# 事件处理
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.time.delay(10)
    screen.fill(color_white)
    for ball in balls:
        ball.move()
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()