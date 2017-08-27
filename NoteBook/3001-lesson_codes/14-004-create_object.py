# coding=utf-8
#!python3

# =======================================================================
"""
来源：代码清单 14-4
问题：创建一个蓝图 和 对象 的标准方法
接口：
"""

# =======================================================================
# globals 

# -----------
# 创建一个蓝图
class Ball:                             # 类   class = Ball
    def __init__(self, color, size, direction):
        self.color     = color          # 方法 method = __init__
        self.size      = size           # 操作 创建并初始化了属性 attribute
        self.direction = direction

    def __str__(self):                  # 方法 method = __str__
        msg = "Hi, I'm a " + self.size + " " + self.color + " ball!"
        return msg                      # 操作 初始化一个局部变量来返回一个字符串

    def bounce(self):                   # 方法 method = bounce
        if self.direction == "down":    # 操作 修改了属性 attribute
            self.direction = "up"

# ----------------------
# 由蓝图创建多个实例(对象)
myBall  = Ball('green', 'small', 'down') # 实例 instance = myBall
herBall = Ball('red', 'small', 'up')     # 实例 instance = herBall

# -------------------------------
# 使用方法 method 来操作对象 object
print("my ball is", myBall.size)
print("my ball is", myBall.color)
print("my ball is going", myBall.direction)
print()
print("play ...")
myBall.bounce()
print("my ball is going", myBall.direction)
