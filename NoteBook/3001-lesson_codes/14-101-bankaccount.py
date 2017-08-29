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

    def showMoney(self):                # 方法 查看余额
        print("money = " + str(self.money))

    def putMoneyIn(self, money):        # 方法 存钱
        if money > 0:
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
    def __init__(self, name, ID, money):# 属性 继承BankAccount 的__init__() 方法
        BankAccount.__init__(self, name, ID, money) # 必须带上self 参数，
                                                    # 于是这个子类就有了公共类的那些属性数据
                                                    # 创建利息账户的时候，会自动创建银行账户、并初始化这个账户
        self.interest = 0               # 属性 私有属性

    def showInterest(self):             # 方法 显示利息
        print("interest = " + str(self.interest))

    def addInterest(self, race):        # 方法 增加利息
        self.interest = self.money * race
        BankAccount.putMoneyIn(self, self.interest)
        BankAccount.showMoney(self)     # 访问我的银行账户(__init__()方法里面已经初始化了这个银行账户)

    def showMoney(self):                # 方法 显示余额
        BankAccount.showMoney(self)

# ---------------------
# 由蓝图创建多个实例(对象)
myInterest = InterestAccount('chenchen', 1001, 1000.00)

# -------------------
# 使用属性数据、操作对象
myInterest.showInterest()
myInterest.addInterest(0.2)
myInterest.showInterest()
myInterest.showMoney()



