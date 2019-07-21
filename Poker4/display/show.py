# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   按金字塔形显示一副牌牌
# ------------------------(max to 80 columns)-----------------------------------

# 引用Python的模块
import sys
import codecs
import os

# 引用自己的模块
sys.path.append('..')
from display.menu import clear_menu


def read_deck(game_type, deck_no):
    '将一副牌的文件，读取到一个列表内'

    # 读取文件内容至一个列表
    filename = 'no_such_a_file.txt'
    if game_type == 1:
        if deck_no >= 1 and deck_no <= 3:
            filename = '争上游%02d副牌.txt' % (deck_no)
    if game_type == 2:
        if deck_no >= 1 and deck_no <= 4:
            filename = '桥牌%02d副牌.txt' % (deck_no)
    if game_type == 3:
        if deck_no >= 1 and deck_no <= 3:
            filename = '三人斗地主%02d副牌.txt' % (deck_no)
        elif deck_no == 9:
            filename = '三人斗地主-预留牌.txt'
    if game_type == 4:
        if deck_no >= 1 and deck_no <= 4:
            filename = '四人斗地主%02d副牌.txt' % (deck_no)
        elif deck_no == 9:
            filename = '四人斗地主-预留牌.txt'

    out_path = os.getcwd() + '\\OutputDecks\\' + filename
    # print(out_path)

    # read deck from a file
    f = codecs.open(out_path, "r", "utf-8")
    fdata = f.readlines()
    f.close

    # 去除列表中的 '\n' 或 '\t'
    deck_out = []
    for card in fdata:
        deck_out.append(card[:-1])
    print('--debug: deck file is %s' % (deck_out))

    return deck_out


def show_deck_para(deck):
    '用并排的方式显示一副扑克牌（假设扑克牌已经排好序）'

    clear_menu()

    print('**********************************')
    print('***       我挑的牌如下         ***')
    pre_card = ''
    cur_card = ''
    for card in deck:
        cur_card = card[:-1]
        if cur_card != pre_card:
            print('\n%s ' % (card), end='')
        else:
            print('%s ' % (card), end='')
        pre_card = cur_card

    print('\n\n**********************************')
    print('*****        总计 %d 张牌      ***' % (len(deck)))

    return
