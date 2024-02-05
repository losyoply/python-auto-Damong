import RaphaelScriptHelper as gamer
import multiprocessing
import testDict as rd
import settings


gamer.deviceType=1

gamer.deviceID='127.0.0.1:62001'

x=112
gamer.touch(rd.string_change)
gamer.touch((1474,x))
gamer.delay(4)

while x<=300:
    x+=118
    if x>=300:
        x=112
    gamer.touch(rd.search_chicken_wuo)
    if gamer.find_pic_touch(rd.gray_hoe):
        pass
    gamer.delay(8)
    gamer.touch(rd.string_change)
    gamer.touch((1474,x))
    gamer.delay(4)

