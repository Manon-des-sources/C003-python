# coding=utf-8
#!python3

# =======================================================================
"""
来源：第14章习题
问题：bank account
接口：
"""

# =======================================================================
# globals 

# -----------
# 创建一个蓝图
class BankAccount:                      # 类   class = BankAccount
    def __init__(self, name, ID, money):# 属性 attribure
        self.name  = name
        self.ID    = ID
        self.money = money

    def __str__(self):                  # 方法 method
        msg = "This is " + name + '\'s' + "Bank account." + "\r\n" \
              "ID = " + str(ID) + ', '                    + "\r\n" \
              "monye = " + str(money)
        return msg

    def balance(self):                  # 方法 查看余额
        print("money = " + self.money)

    def putMoneyIn(self, money):        # 方法 存钱
        if money > 0：
            self.money += money
        else:
            print("money should be above 0")
    
    def pullMoneyOut(self, money):      # 方法 取钱
        if self.money >= money:
            self.money -= money
            return self.money
        else:
            print('There\'s only ' + self.money + '$ left.' )
            return 0

# -----------
# 创建一个蓝图
class InterestAccount(BankAccount):     # 类   class = InterestAccount
    def __init__(self):
        BankAccount.__init__(self)      # 属性 继承BankAccount 的__init__() 方法
        self.interest = 0               # 属性 私有属性

    def interest(self):                 # 方法 显示利息
        print("interest = " + self.interest)

    def addInterest(self, race):        # 方法 增加利息
        self.interest = self.money * race
        BankAccount.putMoneyIn(self.interest)

# ----------------------
# 由蓝图创建多个实例(对象)
myAccount  = BankAccount('chenchen', 0001, 1000.00)
myInterest = InterestAccount()

# -------------------------------
# 使用属性数据、操作对象

