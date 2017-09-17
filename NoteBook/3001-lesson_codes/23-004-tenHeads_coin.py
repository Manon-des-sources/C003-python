# coding=utf-8
#!python3

# =======================================================================
"""
来源：
问题：投骰子、看看连续10次投出面朝上的几率
接口：
说明：
"""
# =======================================================================
# modules section
import random

coin = ['heads', 'tails']
heads_in_row = 0
ten_heads_in_row = 0
ten_heads_index = []

for i in range(100 * 100 *100):
    if random.choice(coin) == 'heads':
        heads_in_row += 1
    else:
        heads_in_row = 0
    
    if heads_in_row >= 16:
        ten_heads_in_row += 1
        heads_in_row = 0
        ten_heads_index.append(i)   # 记住是哪些时刻得到的

print('We got 10 heads in a row', ten_heads_in_row, 'times')
print('when', ten_heads_index)