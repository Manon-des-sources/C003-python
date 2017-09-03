# coding=utf-8
#!python3

# =======================================================================
"""
来源：代码清单18-1
问题：按键、鼠标控制
接口：
说明：
"""
# =======================================================================
# modules section
import sys
import random
import pygame

# =======================================================================
# globals 
# RGB 颜色(colordict.py里面有完整定义)
color_black = [0  ,0  ,0  ]
color_white = [255,255,255]
color_red   = [255,0  ,0  ]
color_green = [0  ,255,0  ]
color_blue  = [0  ,0  ,255]

# 创建初始显示面
screen_size = [640, 480]
pygame.init()
screen = pygame.display.set_mode(screen_size)
back_ground = pygame.Surface(screen.get_size())
back_ground.fill(color_white)

# 创建clock对象
clock = pygame.time.Clock()


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
        if self.rect.left  <= screen.get_rect().left  or  \
           self.rect.right >= screen.get_rect().right:
            self.speed[0] = -self.speed[0]
            newpos = self.rect.move(self.speed)
            self.rect = newpos
        if self.rect.top    <= screen.get_rect().top  or  \
           self.rect.bottom >= screen.get_rect().bottom: 
            self.speed[1] = -self.speed[1]
            newpos = self.rect.move(self.speed)
            self.rect = newpos
        # 这里有个bug：将ball 拖到screen 的四个角，ball 会一直在那里抖动停留
        # 或者拖到screen 的某一边上，ball 就会一直沿着边直着走，不会反弹
        # 原因在于如果ball 不止一两点超过边界、move() 里面会连续执行 self.speed[0] = -self.speed[0]
        # 这导致一会儿上一会儿又下、结果就是一直出不去

        # 而下面按键那里、

# 创建精灵组
image_ball = '0000-photos\\beach_ball.png'
location   = [10, 10]
speed      = [1, 1]
ball       = MyBallClass(image_ball, location, speed)

# 按键重复设置：长按200后开始重复输出按键(每隔50ms出一个)
# 相当于另一种模式的保持事件
# 这些参数会影响按键灵敏度
pygame.key.set_repeat(200, 20)

mouse_hold = False
# 事件处理
while True:
    for event in pygame.event.get():
        # 界面控制按钮
        if event.type == pygame.QUIT:
            frame_race = clock.get_fps()    # 检测当前帧速率
            print("fram_race = ", frame_race)
            sys.exit()
        # 按键事件
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball.rect.top -= 10
            elif event.key == pygame.K_DOWN:
                ball.rect.top += 10
            elif event.key == pygame.K_LEFT:
                ball.rect.left -= 10
            elif event.key == pygame.K_RIGHT:
                ball.rect.left += 10
        # 鼠标事件
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_hold = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_hold = False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_hold:
             ball.rect.center = event.pos    # 使用鼠标的位置
    # 控制帧速率为30fps
    clock.tick(30)
    screen.blit(back_ground, [0, 0])
    ball.move()
    screen.blit(ball.image, ball.rect)
    pygame.display.flip()
