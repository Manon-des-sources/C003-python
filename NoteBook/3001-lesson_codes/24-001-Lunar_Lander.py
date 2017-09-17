# coding=utf-8 
#!python3 

# =======================================================================
"""
来源：
问题：模拟飞船着陆月球
接口：
说明：
一、仿真跟踪(属性)
1、飞船相对于月球表面的高度、速度、加速度
2、飞船的质量、随着燃料的消耗、飞船的质量会变化
3、发动机的推力、推力不同、燃料消耗的速率不同
4、燃料剩余
5、飞船受到的重力、这与月球的质量、飞船的重量相关

二、实时跟踪
1、每隔固定的时刻、检查并更新飞船的属性参数

三、模块
1、初始状态：建立一个pygame窗口、加载背景图像、初始化参数
2、将推进器定义为动画精灵
3、计算高度、速度、加速度、燃料消耗
4、显示参数信息
5、更新燃料表
6、显示火箭尾焰、推力不同尾焰长度不同
7、将以上更改blit 到screen 上，检查鼠标事件、更新推进器位置、检查飞船是否着陆
8、显示‘游戏结束’信息和统计信息
"""
# =======================================================================
# modules section
import pygame
import sys


# =======================================================================
# globals 
# RGB 颜色(colordict.py里面有完整定义)
color_black = [0  ,0  ,0  ]
color_gray  = [128,128,128]
color_white = [255,255,255]
color_red   = [255,0  ,0  ]
color_green = [0  ,255,0  ]
color_blue  = [0  ,0  ,255]

color_flame   = [255, 109, 14]
color_ctrlBar = [60,  60,  60]

# =======================================================================
# 初始界面
pygame.init()
screen = pygame.display.set_mode([400, 600])
screen.fill(color_black)

ship_image = '0000-photos\\lunarlander.png'
ship = pygame.image.load(ship_image)

lunar_image = '0000-photos\\moonsurface.png'
moon = pygame.image.load(lunar_image)

ground = 540        # landing pad is y=540
start  = 90

clock = pygame.time.Clock()

# 初始参数
ship_mass =  5000.0     # 飞船质量 
fuel      =  5000.0     # 燃料质量 
velocity  = -100.0      # 速度(矢量)
gravity   =  10         # 重力加速度
height    =  2000       # 飞船高度
thrust    =  0          # 飞船推力
delta_v   =  0          # 速度增量 
y_pos     =  90         # 
held_down = False       # 

# 推进器蓝图(动画精灵)
class ThrottleClass(pygame.sprite.Sprite):
    def __init__(self, location = [0,0]):
        pygame.sprite.Sprite.__init__(self)     # 继承动画精灵的属性
        image_surface = pygame.surface.Surface([30, 10])
        image_surface.fill(color_gray)
        self.image = image_surface.convert()
        self.rect  = self.image.get_rect()
        self.rect.left, self.rect.centery = location

# 速度
def calculate_velocity():
    global thrust, fuel, velocity, delta_v, height, y_pos
    # 
    delta_v = 1/fps
    thrust  = (500 - myThrottle.rect.centery) * 5.0     # 将推进器的y 轴高度转换为推力

    # 燃料
    fuel   -= thrust / (10*fps)
    if fuel < 0:
        fuel = 0.0
    if fuel < 0.1:
        thrust = 0.0

    delta_v  = delta_v * (-gravity + 200*thrust / (ship_mass + fuel))
    velocity = velocity + delta_v
    delta_h  = velocity * delta_v

    # 将高度转化为pygame 中的y 轴位置
    y_pos = ground - (height * (ground - start) / 2000) - 90

# 显示统计信息
def display_stats():
    v_str  = 'velocity:     %i m/s' % velocity
    h_str  = 'height:       %.1f'   % height
    t_str  = 'thrust:       %i'     % thrust
    a_str  = 'acceleration: %.1f'   % (delta_v * fps)
    f_str  = 'fuel:         %i'     % fuel
    v_font = pygame.font.Font(None, 26)

    v_surf = v_font.render(v_str, 1, color_white)
    screen.blit(v_surf, [10, 50])

    a_font = pygame.font.Font(None, 26)
    a_surf = a_font.render(a_str, 1, color_white)
    screen.blit(a_surf, [10, 100])

    h_font = pygame.font.Font(None, 26)
    h_surf = h_font.render(h_str, 1, color_white)
    screen.blit(h_surf, [10, 150])

    t_font = pygame.font.Font(None, 26)
    t_surf = t_font.render(t_str, 1, color_white)
    screen.blit(t_surf, [10, 200])

    f_font = pygame.font.Font(None, 26)
    f_surf = f_font.render(f_str, 1, color_white)
    screen.blit(f_surf, [60, 300])

# 显示尾焰
def display_flames():
    flame_size = thrust / 15
    for i in range(2):
        startx = 252 - 10 + i*19
        starty = y_pos + 83 
        pygame.draw.polygon(screen, 
                            color_flame, 
                            [(startx,     starty)
                            (startx + 4, starty + flame_size)
                            (startx + 8, starty)],
                            0)

# 显示游戏结束信息
def display_final():
    final1 = 'Game Over'
    final2 = 'You landed at %.1f m/s' % velocity

    if velocity > -5:
        final3 = 'Nice landing!'
        final4 = 'I hear NASA is hiring'
    elif velocity > -15:
        final3 = 'Ouch! A bit rough, but you survived'
        final4 = "You'll do better next time"
    else:
        final3 = 'Yikes! You crashed a 30 Billion dollar ship'
        final4 = 'How are you getting home?'
    
    pygame.draw.rect(screen, color_black, [5,5,350,280], 0)
    f1_font = pygame.font.Font(None, 70)
    f1_surf = f1_font.render(final1, 1, color_white)
    screen.fill(f1_surf, [20, 50])

    f2_font = pygame.font.Font(None, 40)
    f2_surf = f2_font.render(final2, 1, color_white)
    screen.fill(f2_surf, [20, 100])

    f3_font = pygame.font.Font(None, 26)
    f3_surf = f3_font.render(final3, 1, color_white)
    screen.fill(f3_surf, [20, 150])

    f4_font = pygame.font.Font(None, 26)
    f4_surf = f4_font.render(final4, 1, color_white)
    screen.fill(f4_surf, [20, 180])

# 创建推进器对象
myThrottle = ThrottleClass([15, 500])

while True:
    clock.tick(30)
    fps = clock.get_fps()
    if fps < 1:
        fps = 30
    
    if height > 0.01:
        calculate_velocity()
        screen.fill(color_black)
        display_stats()
        # 燃料表
        pygame.draw.rect(screen, color_blue, [80, 350, 24, 100], 2)
        fuelbar = 96 * fuel / 5000
        pygame.draw.rect(screen, color_green, [84, 448-fuelbar, 18, fuelbar], 0)
        # 推进器滑块
        pygame.draw.rect(screen, color_red, [25, 300, 10, 200], 0)
        screen.blit(moon, [0, 500, 400, 100])
        pygame.draw.rect(screen, color_ctrlBar, [220, 535, 70, 5], 0)
        screen.blit(myThrottle.image, myThrottle.rect)
        display_flames()
        screen.blit(ship, [230, y_pos, 50, 90])

        instruct1 = 'Land softly without running out of fuel'
        instruct2 = 'Good landing: < 15m/s  Great landing: < 5m/s'
        inst1_font = pygame.font.Font(None, 24)
        inst1_surf = inst1_font.render(instruct1, 1, color_white)
        screen.blit(inst1_surf, [50, 550])
        inst2_font = pygame.font.Font(None, 24)
        inst2_surf = inst2_font.render(instruct2, 1, color_white)
        screen.blit(inst2_surf, [20, 575])
        pygame.display.flip()
    else:
        display_final()

    for event in pygame.event.get():
        if   event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBOTTONDOWN:
            held_down = True
        elif event.type == pygame.MOUSEBOTTONUP:
            held_down = False
        elif event.type == pygame.MOUSEMOTION:
            if held_down:
                myThrottle.rect.centery = event.pos[1]
                if myThrottle.rect.centery < 300:
                    myThrottle.rect.centery = 300
                if myThrottle.rect.centery > 500:
                    myThrottle.rect.centery = 500