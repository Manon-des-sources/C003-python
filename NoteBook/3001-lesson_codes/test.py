# coding=utf-8
#!python3

# =======================================================================
"""
来源：代码清单18-2
问题：Ping 游戏
接口：
说明：小球随机开始下落、球拍跟随鼠标移动
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


# ============
# 创建蓝图-ball
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)         # 继承Sprite 的属性数据
        # 使用继承来的属性数据
        self.image = pygame.image.load(image_file)  # 属性1 image --  初始化image
        self.rect  = self.image.get_rect()          # 属性2 rect  --  包含image边界的矩形对象
        self.rect.left, self.rect.top = location    # rect 的初始位置  --  初始化image的位置
        self.speed = speed                          # 属性3 私有属性  --  移动速度[Vx, Vy]

    def move(self):
        global points, textmsg
        self.rect = self.rect.move(self.speed)      # 移动到新的位置(在显示面范围)
        if self.rect.left  <= screen.get_rect().left  or  \
           self.rect.right >= screen.get_rect().right:
            self.speed[0] = -self.speed[0]
            hit_wall.play()
        if self.rect.top    <= screen.get_rect().top:
            self.speed[1] = -self.speed[1]
            get_point.play()
            # 计算分数
            points += 1
            msg     = 'score:' + str(points) + ' ' +  \
                      'lives:' + str(lives)
            textmsg = font.render(msg, 1, color_red)

# ==============
# 创建蓝图-paddle
class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)                 # 继承Sprite 的属性数据
        image_surface = pygame.surface.Surface([100, 20])   # 创建一个矩形表面
        image_surface.fill(color_black)
        self.image = image_surface.convert()                # 将表面转换成一个图像/图片
        self.rect  = self.image.get_rect()                  # 可以用这个来创建一个ball ?
        self.rect.left, self.rect.top = location


# 创建初始显示面
screen_size = [640, 480]
pygame.init()
screen = pygame.display.set_mode(screen_size)
back_ground = pygame.Surface(screen.get_size())
back_ground.fill(color_white)

# 创建wav声音对象(适合短小的声音)
pygame.mixer.init()
sound_file = 'sounds\\bg_music.mp3'
pygame.mixer.music.load(sound_file)
pygame.mixer.music.set_volume(0.2)    # 20% 音量 
sound_file = 'sounds\\game_over.wav'
game_over = pygame.mixer.Sound(sound_file)
game_over.set_volume(0.2)
sound_file = 'sounds\\hit_paddle.wav'
hit_paddle = pygame.mixer.Sound(sound_file)
hit_paddle.set_volume(0.2)
sound_file = 'sounds\\hit_wall.wav'
hit_wall = pygame.mixer.Sound(sound_file)
hit_wall.set_volume(0.2)
sound_file = 'sounds\\get_point.wav'
get_point = pygame.mixer.Sound(sound_file)
get_point.set_volume(0.2)
sound_file = 'sounds\\splat.wav'
splat = pygame.mixer.Sound(sound_file)
splat.set_volume(0.2)
sound_file = 'sounds\\new_life.wav'
new_life = pygame.mixer.Sound(sound_file)
new_life.set_volume(0.2)

# 创建ball 精灵
image_ball = '0000-photos\\wackyball.bmp'
speed      = [10, 5]
ball       = MyBallClass(image_ball, [50, 50], speed)
# 创建balls 精灵组
ball_group = pygame.sprite.Group(ball)

# 创建paddle 精灵
paddle = MyPaddleClass([270, 400])

# 创建信息显示对象
lives  = 4
points = 0
msg    = 'score:' + str(points) + ' ' +  \
         'lives:' + str(lives)
font   = pygame.font.Font(None, 50)
textmsg = font.render(msg, 1, color_red)    # 渲染文本
textpos = [10, 10]

# 创建clock对象
clock = pygame.time.Clock()

pygame.mixer.music.play(-1)

# 事件处理
while True:
    # 控制帧速率为30fps
    clock.tick(30)
    screen.fill(color_white)
    screen.blit(back_ground, [0, 0])
    for event in pygame.event.get():
        # 界面控制按钮
        if event.type == pygame.QUIT:
            frame_race = clock.get_fps()    # 检测当前帧速率
            print("fram_race = ", frame_race)
            sys.exit()
        # 移动paddle
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]
    # ball 与paddle 碰撞则反弹
    if pygame.sprite.spritecollide(paddle, ball_group, False):
        ball.speed[1] = -ball.speed[1]
        hit_paddle.play()
    # 移动ball
    ball.move()
    # 刷新显示
    screen.blit(ball.image, ball.rect)
    screen.blit(paddle.image, paddle.rect)
    screen.blit(textmsg, textpos)
    # 生命值
    if ball.rect.top >= screen.get_rect().bottom:
        lives -= 1
        splat.play()
        if lives == 0:
            pygame.time.delay(1000)
            game_over.play()
            pygame.time.delay(1000)
            pygame.mixer.music.fadeout(2000)    # 以淡出的方式结束背景音乐
            final_text1 = "Game Over"
            final_text2 = "Your final score is: " + str(points)
            ft1_font = pygame.font.Font(None, 70)
            ft2_font = pygame.font.Font(None, 50)
            ft1_surf = font.render(final_text1, 1, color_red)
            ft2_surf = font.render(final_text2, 1, color_red)
            screen.blit(ft1_surf, [screen.get_width()/2 - ft1_surf.get_width()/2, 100])
            screen.blit(ft2_surf, [screen.get_width()/2 - ft2_surf.get_width()/2, 200])
            # 游戏结束后、小球不再移动(这里必须赋值为list而不是tuple、否则它将不可修改)
            ball.speed = [0, 0]
        else:
            pygame.time.delay(2000)
            new_life.play()
            ball.rect.topleft = [screen.get_rect().width - 40*lives, 20]
    for i in range(lives):
        width = screen.get_rect().width
        screen.blit(ball.image, [width - 40 * i, 20])
    pygame.display.flip()
