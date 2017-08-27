# coding=utf-8
#!python3

# =======================================================================
"""
来源：代码清单 14-5
问题：热狗店
接口：
"""

# =======================================================================
# globals 

# -----------
# 创建一个蓝图
class Hotdog:                           # 蓝图

    def __init__(self):
        self.cooked_level  = 0          # 属性 1 = 熟透程度值
        self.cooked_string = 'Raw'      # 属性 2 = 熟透程度描述
        self.condiments    = []         # 属性 3 = 配料表

    def __str__(self):                  # 方法 __str__
        msg = 'hot dog'
        if len(self.condiments) > 0:
            msg += 'with'
        for i in self.condiments:
            msg += i + ', '
        msg = msg.strip(', ')
        msg = self.cooked_string + ' ' + msg + '.'
        return msg

    def cook(self, time):               # 方法 烤制
        self.cooked_level = self.cooked_level + time
        if self.cooked_level > 8:
            self.cooked_string = 'Charcoal'
        elif self.cooked_level > 5:
            self.cooked_string = 'Well-done'
        elif self.cooked_level > 3:
            self.cooked_string = 'Medium'
        else:
            self.cooked_string = 'Raw'
    
    def addCondiment(self, condiment):  # 方法 添加配料
        self.condiments.append(condiment)
# ----------------------
# 由蓝图创建多个实例(对象)
myDog = Hotdog()

# -------------------------------
# 使用属性数据、操作对象
print(Hotdog)
print(myDog)

print("Cooking hot dog for 4 minutes ...")
myDog.cook(4)
print(myDog)

print("Cooking hot dog for 3 minutes ...")
myDog.cook(3)
print(myDog)


