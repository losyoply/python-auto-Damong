import RaphaelScriptHelper as gamer
import multiprocessing
import testDict as rd
import settings
# 適用(804,764)金陵

gamer.deviceType=1

gamer.deviceID='127.0.0.1:62001'
#現有axe數量 #非裝備狀態的斧頭數量，也就是如果現在身上有斧頭，斧頭總數減一
axe=0


while 1:
    if gamer.find_pic(rd.tooless_hand):
        gamer.touch(rd.search_chicken_wuo)
        #print(axe)
        if axe<=0:
            break
        else:
            gamer.find_pic_touch(rd.gray_axe)
            axe=axe-1
    # if gamer.find_pic_touch(rd.gray_axe):
    #     pass
    else:
        gamer.touch(rd.search_chicken_wuo)
    gamer.delay(7)

