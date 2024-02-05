import RaphaelScriptHelper as gamer
import multiprocessing
import testDict as rd
import settings

gamer.deviceType=1

gamer.deviceID='127.0.0.1:62001'

def bangPai():
    gamer.touch(rd.huoDong)
    gamer.touch(rd.bangPai)
    gamer.touch(rd.bangPai2)
    while True:
        if gamer.find_pic_touch(rd.bangPai3):
            gamer.touch((1438,683))
            break
    while True:
        if gamer.find_pic(rd.buy):
            gamer.touch(rd.buy2)
            gamer.touch(rd.buy3)
            break
    while True:
        if gamer.find_pic_touch(rd.give):
            break
    while True:
        if gamer.find_pic(rd.share):
            gamer.touch(rd.NPCtalk)
            break

def shili():
    gamer.touch(rd.huoDong)
    gamer.touch(rd.bangPai)
    gamer.touch(rd.shili)

bangPai()
shili()