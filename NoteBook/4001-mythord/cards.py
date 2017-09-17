# coding=utf-8
#!python3

# =======================================================================
"""
来源：
问题：纸牌的蓝图
接口：
说明：
"""
# =======================================================================
# modules section
import random

# 纸牌的属性
# 花色
list_suit  = ('SuitError','Diamond','Hearts','Spades','Clubs')
# 名字
list_rank  = ('RankError','Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')
# 点数
list_value = (-1,  1,1,1,1, 1,1,1,1, 1,1,  10,10,10)
class Card:
    def __init__(self, suit_id, rank_id):
        self.suit_id = int(suit_id)
        self.rank_id = int(rank_id)

        # 纸牌的名字和分值
        if  1 <= self.rank_id <= 13:
            self.rank  = list_rank[self.rank_id]
            self.value = list_value[self.rank_id]
        else:
            self.rank  = list_rank[0]
            self.value = list_value[0]

        # 纸牌的花色
        if  1 <= self.suit_id <= 4:
            self.suit = list_suit[self.suit_id]
        else:
            self.suit = list_suit[0]
        
        # 纸牌的短名
        self.short_name = self.suit[0] + self.rank[0]
        if  self.rank == '10':
            self.short_name = self.suit[0] + self.rank

        # 纸牌的完整名字
        self.long_name = self.suit + ' of ' + self.rank
    
    def __str__(self):
        msg = """This is a class of a card\r\nUse this class to build a deck\r\n"""
        print(msg)

if __name__ == '__main__':
    Card(1, 1).__str__()
    # 创建一副牌
    deck = []
    for suit_id in range(1, 5):
        for rank_id in range(1, 14):
            deck.append(Card(suit_id, rank_id))

    # 输出整副牌
    print('card.rank_id\t', 'card.shor_name\t', 'value\t', 'card.long_name')
    for card in deck:
        print(card.rank_id, '\t\t', card.short_name, '\t\t', card.value, '\t', card.long_name)