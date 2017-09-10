# coding=utf-8
#!python3

# =======================================================================
"""
来源：
问题：
接口：
说明：
"""
# =======================================================================
# modules section
import sys
import pygame


pygame.init()
pygame.mixer.init()

# 创建一个窗口(播放声音、动画等都必须启动pygame)
# pygame窗口退出就表示pygame本身也退出、也就无法再运行任何pygame的内置方法
screen = pygame.display.set_mode([640, 480])
# 等待初始化ok、窗口建立ok后再运行其他模块
pygame.time.delay(1000)

# # 创建一个wav声音对象(适合短小的声音)
sound_file = 'sounds\\Ahoy.wav'
Aboy = pygame.mixer.Sound(sound_file)
Aboy.set_volume(0.2)    # 40% 音量 

# 创建一个mps声音对象(适合较大的声音)
sound_file = 'sounds\\bg_music.mp3'
pygame.mixer.music.load(sound_file)
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(1)      # 参数为重复播放的次数、负数表示一直循环播放(get_busy()用于返回True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # 检测music播放进度
    if pygame.mixer.music.get_busy() == False:
        Aboy.play()
        pygame.time.delay(7500)
        sys.exit()
