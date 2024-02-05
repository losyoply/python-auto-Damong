import RaphaelScriptHelper as gamer
import multiprocessing
import testDict as rd
import settings
# 適用雪盧書院楓樹(江南)

gamer.deviceType=1

gamer.deviceID='127.0.0.1:62001'
# #現有axe數量 #非裝備狀態的斧頭數量，也就是如果現在身上有斧頭，斧頭總數減一
# axe=0



x=112
gamer.touch(rd.string_change)
gamer.touch((1474,x))
gamer.delay(4)

while x<=850:
    x+=118
    if x>=850:
        x=112
    gamer.touch(rd.search_chicken_wuo)
    if gamer.find_pic_touch(rd.blue_axe):
        pass
    gamer.delay(8)
    gamer.touch(rd.string_change)
    gamer.touch((1388,x))
    gamer.delay(4)

