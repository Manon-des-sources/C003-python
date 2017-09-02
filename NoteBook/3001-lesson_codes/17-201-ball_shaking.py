# coding=utf-8
#!python3

# =======================================================================
"""
来源：代码清单17-3 
问题：精灵碰撞检测 sprite collision 
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
        self.rect = self.rect.move(self.speed)      # 移动到新的位置(在显示面范围)
        if self.rect.left < 0  or  self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0  or  self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

# ========================
# 动画：处理一组sprite 对象
def animate(group):
    screen.fill(color_white)
    for ball in group:
        #group.remove(ball)
        # 检测一个精灵(不再这个group)和其他所有精灵(在这个group)之间是否发生碰撞
        if pygame.sprite.spritecollide(ball, group, False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]
        #group.add(ball)
        # 移动 这个 精灵
        ball.move()
        screen.blit(ball.image, ball.rect)
    # 刷新画面
    pygame.display.flip()
    pygame.time.delay(10)


# 创建初始显示面
screen_size = width, height = [640, 480]
pygame.init()
screen = pygame.display.set_mode(screen_size)
screen.fill(color_white)

image_ball = '0000-photos\\beach_ball.png'
# 创建精灵组
group_ball = pygame.sprite.Group()
speed    = [random.choice([-1, 1]), random.choice([-1, 1])]
# 每个ball 都是一个sprite 对象、每个ball 都是一个sprite 精灵
ball     = MyBallClass(image_ball, [50, 50], speed)
group_ball.add(ball)

# 事件处理
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    animate(group_ball)
