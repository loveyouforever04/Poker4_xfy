# test

import time
# import our modules
from display.menu import *
from machine.std_mach import *
from dealer.mike import*
# Phase 1-----------------------------------------------------------------------
# 打印开始界面
dsp_start()
time.sleep(1)  # 延迟3秒
# Phase 2-----------------------------------------------------------------------
# 打印选择游戏玩法界面
game_type = dsp_choice_game()

deck = []
make_deck_by_type(game_type,deck)
print(deck)
# Phase 4-----------------------------------------------------------------------
# 预先准备4+1个位置放牌
player_a = []
player_b = []
player_c = []
player_d = []
player_dumy = []  # 放置预留牌的位置

# 按游戏类型发牌
if game_type == 1:
    deal_to_multi_players(deck, player_a, player_b, player_c)
    record_deck_csv(player_a, '争上游01副牌.csv')
    record_deck_csv(player_b, '争上游02副牌.csv')
    record_deck_csv(player_c, '争上游03副牌.csv')

if game_type == 2:
    deal_to_multi_players(deck, player_a, player_b, player_c, player_d)
    record_deck_csv(player_a, "桥牌01.csv")
    record_deck_csv(player_b, "桥牌02.csv")
    record_deck_csv(player_c, "桥牌03.csv")
    record_deck_csv(player_d, "桥牌04.csv")

if game_type == 3:
    deal_to_multi_players_remain(deck, 3,player_dumy,player_a, player_b, player_c)
    record_deck_csv(player_a, "三人斗地主-牌01.csv")
    record_deck_csv(player_b, "三人斗地主-牌02.csv")
    record_deck_csv(player_c, "三人斗地主-牌03.csv")
    record_deck_csv(player_dumy, "三人斗地主-牌预留.csv")

if game_type == 4:
    deal_to_multi_players_remain(deck, 8,player_dumy,player_a, player_b, player_c)
    record_deck_csv(player_a, "四人斗地主-牌01.csv")
    record_deck_csv(player_b, "四人斗地主-牌02.csv")
    record_deck_csv(player_c, "四人斗地主-牌03.csv")
    record_deck_csv(player_dumy, "四人斗地主-牌预留.csv")

deck_no = dsp_show_deck(game_type)
if deck_no == 0:
    dsp_end()
    exit()
elif(deck_no>1 and deck_no <= 4)or deck_no == 9 :

    filename = 'no_such_a_file.csv'
    if game_type == 1:

         if deck_no >= 1 and deck_no <= 3:
             filename = '争上游%02d副牌.csv'%(deck_no)
    if game_type == 2 :
         if deck_no >= 1 and deck_no <= 4:
             filename = '桥牌%02d副牌.csv'%(deck_no)
    if game_type == 3 :

         if deck_no >= 1 and deck_no <= 3:
             filename = '三人斗地主%02d副牌.csv'%(deck_no)
         elif deck_no == 9:
             filename = '三人斗地主—预留牌.csv'
    if game_type == 4 :
         if deck_no >= 1 and deck_no <= 4:
             filename = '四人斗地主%02d副牌.csv'%(deck_no)
         elif deck_no == 9:
             filename = '四人斗地主—预留牌.csv'
    if filename!='no_such_a_file.csv':
          my_deck = []
          read_deck_csv(filename,my_deck)
          show_deck_para(my_deck)
    else:
          dsp_end()
          print('异常退出！挑选了不存在的牌')
else:
    dsp_end()
    print('正常退出')
