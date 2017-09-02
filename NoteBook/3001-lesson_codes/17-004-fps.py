# coding=utf-8
#!python3

# =======================================================================
"""
来源：代码清单17-4
问题：动画帧速率控制
接口：
说明：如果frame_race = m，而我们设置了clock.tick(n)，
     那么、实际的移动速度就是 speed = speed * (n / m)，
     也就是说、如果实际帧速率fps 比预期的小、我们的speed 就应该增大以跟上需要的移动速率
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
    # 移动精灵
    for ball in group:
        ball.move()
        screen.blit(ball.image, ball.rect)
    for ball in group:
        group.remove(ball)
        # 检测一个精灵(不再这个group)和其他所有精灵(在这个group)之间是否发生碰撞
        if pygame.sprite.spritecollide(ball, group, False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]
        group.add(ball)
    # 刷新画面
    pygame.display.flip()


# 创建初始显示面
screen_size = width, height = [640, 480]
pygame.init()
screen = pygame.display.set_mode(screen_size)
screen.fill(color_white)

# 创建clock对象
clock = pygame.time.Clock()

# 创建精灵组
image_ball = '0000-photos\\beach_ball.png'
group_ball = pygame.sprite.Group()
for row in range(0, 2):
    for column in range(0, 2):
        location = [column * 180 + 10,  row * 180 + 10]
        speed    = [random.choice([-2, 2]), random.choice([-2, 2])]
        # 每个ball 都是一个sprite 对象、每个ball 都是一个sprite 精灵
        ball     = MyBallClass(image_ball, location, speed)
        group_ball.add(ball)

# 事件处理
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            frame_race = clock.get_fps()    # 检测当前帧速率
            print("fram_race = ", frame_race)
            sys.exit()
    animate(group_ball)
    # 控制帧速率为30fps
    clock.tick(30)