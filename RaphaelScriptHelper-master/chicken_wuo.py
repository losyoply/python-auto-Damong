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

while x<=1000:
    x+=118
    if x>=1000:
        x=112
    gamer.touch(rd.search_chicken_wuo)
    gamer.delay(9)
    gamer.touch(rd.string_change)
    gamer.touch((1388,x))
    gamer.delay(4)

