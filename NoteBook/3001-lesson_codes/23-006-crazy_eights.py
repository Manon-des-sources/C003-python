# coding=utf-8
#!python3

# =======================================================================
"""
来源：
问题：纸牌游戏 Crazy Eights
接口：
说明：
1、玩家数 = 2
2、每个玩家有5 张牌
3、初始玩家从剩下的牌中翻开一张牌、开始游戏

游戏规则：
1、每一轮、玩家必须做出的操作选择：
   出一张牌、它要和翻开的牌的花色相同
   出一张牌、它要和翻开的牌的点数相同
   出一张8、花色无要求

2、如果玩家出一张8，他就可以‘叫花色’，也就是他可以选择一个花色，下一个玩家必须根据这个花色出牌
3、如果玩家无法出牌、必须从剩下的牌中抽一张到自己的手上
4、如果玩家出光了手中的牌、他就赢了，将会根据另一个玩家手里的牌来计分：
   每个8 得50分
   每个花牌(J,Q,K)得10分
   每个A得1分
   其他牌按照牌的点数计分
5、整副牌都发完了、游戏结束，玩家根据对方剩余的牌来计分
6、如果玩累了、可以直接结束游戏，结算得分
"""
# =======================================================================
# modules section
import random

# 纸牌的属性
# 花色
list_suit  = ('SuitError','Diamonds','Hearts','Spades','Clubs')
# 名字
list_rank  = ('RankError','Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')
# 分值
list_value = (-1,  1,1,1,1, 1,1,1,1, 1,1,  10,10,10)

# =========
# 纸牌的蓝图
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

# 创建一副牌
deck = []
for suit_id in range(1, 5):
    for rank_id in range(1, 14):
        new_card = Card(suit_id, rank_id)
        if  new_card.rank_id == 8:
            new_card.value = 50
        deck.append(new_card)

# 玩家手中的牌
def player_getCards():
    p_hand = []
    for card in range(0, 5):
        a = random.choice(deck)
        p_hand.append(a)
        deck.remove(a)


# 游戏初始状态
def init_card():
    # 翻出来的第一张牌
    chosen_card = random.choice(deck)
    deck.remove(chosen_card)
    up_card = chosen_card
    print('Up card:', up_card.short_name)
    # 第一张牌的花色就是当前花色、玩家出的牌要么是这个花色、要么点数是这张牌的点数
    # 如果玩家除了一张8、他可以‘叫花色’、以改变当前花色，所以当前花色和chosen_card.suit不一定一样
    active_suit = chosen_card.suit
    print('Suit:', active_suit)

# 显示玩家手中的牌
def player_showCards():
    print('\r\nYour hand:', end='')
    for card in p_hand:
        print(card.short_name, end=',')
    print('Up card:', up_card.short_name)
    if up_card.rank == 8:
        print('Suit:', active_suit)
        

# 出牌为8、可以重新选择花色
def get_new_suit():
    global active_suit
    got_suit = False
    while got_suit == False:
        suit = input('Pick a suit: ')
        if  suit.lower() == 'd':
            active_suit = 'Diamonds'
            got_suit    = True
        elif suit.lower() == 's':
            active_suit = 'Spades'
            got_suit    = True
        elif suit.lower() == 'h':
            active_suit = 'Hearts'
            got_suit    = True
        elif suit.lower() == 'c':
            active_suit = 'Clubs'
            got_suit    = True
        else:
            print('Not a valid suit. Try again. ', end='')
    print('You picked', active_suit)

# 检查玩家手中的牌
def get_player_choice():
    print('what would you like to do?')
    response = input("Type a card to play or 'Draw' to take a card:\t")
    # 抽牌、或出牌
    while valid_play == False:
        selected_card = None
        while selected_card == None:
            if response.lower == 'draw':
                valid_play = True
                if len(deck) > 0:
                    card = random.choice(deck)
                    p_hand.append(card)
                    deck.remove(card)
                    print('You draw', card.short_name)
                else:
                    print('There are no cards left in the deck')
                    blocked |= 0x01
                return
            else:
                for card in p_hand:
                    if response.upper() == card.short_name:
                        selected_card = card
                if selected_card == None:
                    response = input('You do not have that card. Try again:')
        # 检查出牌的合法性
        if selected_card.rank == 8:
            valid_play = True
            is_eight   = True
        elif selected_card.suit == active_suit:
            valid_play = True
        elif selected_card.rank == up_card.rank:
            valid_play = True
        
        if valid_play == False:
            response = input('That is not a legal play. Try again:')
    # 出牌
    p_hand.remove(selected_card)
    up_card = selected_card
    active_suit = up_card.suit
    print('You played', selected_card.short_name)

# 人类玩家
def player_turn():
    global deck, p_hand, blocked, up_card, active_suit
    valid_play = False
    is_eight   = False
    print('\nYour hand: ', end='')
    player_showCards()
    get_player_choice()

# 计算机玩家
# 策略： 1、有8、就尽量出8、且选择手中花色最多的那个8  
#       2、否则出一张牌、出分值最大的牌
#       3、否则抽牌
def computer_turn():
    global c_hand, deck, up_card, active_suit, blocked
    options = []
    for card in c_hand:
        if card.rank == 8:
            c_hand.remove(card)
            up_card = card
            print('Computer played ', card.short_name)
            # 统计每种花色的剩余牌数，数量最多的花色定义为‘长花色’
            suit_totals = [0,0,0,0]
            for suit in range(1, 5):
                for card in c_hand:
                    if card.suit_id == suit:
                        suit_totals[suit-1] += 1
            long_suit = 0
            for i in range(4):
                if suit_totals[i] > long_suit:
                    long_suit = i
            
            if long_suit == 0:
                active_suit = 'Diamonds'
            if long_suit == 1:
                active_suit = 'Hearts'
            if long_suit == 2:
                active_suit = 'Spades'
            if long_suit == 3:
                active_suit = 'Clubs'
            print(' Computer changed suit to ', active_suit)
            return
        # 可以出那些牌
        else:
            if card.suit == active_suit:
                options.append(card)
            elif card.rank == up_card.rank:
                options.append(card)
    # 选择分值最高的牌
    if len(options) > 0:
        best_play = options[0]
        for card in options:
            if card.value > best_play.value:
                best_play = card
        c_hand.remove(best_play)
        up_card = best_play
        active_suit = up_card.suit
        print(' Computer played ', best_play.short_name)
    else:
        if len(deck) > 0:
            next_card = random.choice(deck)
            c_hand.append(new_card)
            deck.remove(next_card)
            print(' Computer drew a card')
        else:
            print(' Computer is blocked')
            blocked |= 0x02
    print('Computer has %i cards left' % (len(c_hand)))

# 计分
done = False
p_total = c_total = 0
while done == False:
    game_over = False
    blocked   = 0
    init_card()
    while game_over == False:
        player_turn()
        if len(p_hand) == 0:
            game_over = True
            print('\nYou won')
            p_points = 0
            for card in c_hand:
               p_points += card.value
            p_total += p_points
            print("You got %i points for computer's hand" % p_points) 
        if game_over == False:
            computer_turn()
        if len(c_hand) == 0:
            game_over  = True
            print('\r\nComputer won')
            c_points = 0
            for card in p_hand:
                c_points += card.value
            c_total += c_points
            print("Computer got %i points for your hand" % c_points)
        # 双方都无法继续出牌、游戏结束
        if blocked == 0x03:
            game_over = True
            print('Both players blocked, GAME OVER.')
            player_points = 0
            for card in c_hand:
                p_points += card.value
            p_total += p_points
            c_points = 0
            for card in p_hand:
                c_points += card.value
            c_total += c_points
            print("You got %i points for computer's hand" % p_points)
            print("Computer got %i points for your hand" % c_points)
        
        play_again = input('Play again (Y/N)? ')
        if play_again.lower().startswith('n'):
            done = False
            print('\nSo for, you have %i points' % p_total)
            print('and the computer has %i points' % c_total)
        else:
            done = True
    
    print('\nFinal Score:')
    print('You: %i\tComputer: %i' % (p_total, c_total)