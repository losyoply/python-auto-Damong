import RaphaelScriptHelper as gamer
import multiprocessing
import testDict as rd
import settings

gamer.deviceType=1

gamer.deviceID='127.0.0.1:62001'

def xuan():
    gamer.touch(rd.huoDong)
    gamer.touch(rd.xuanShang)

    while True:
        if gamer.find_pic(rd.have_xuan):
            gamer.touch(rd.go)
            break
    

    while True:
        if gamer.find_pic(rd.car):
            gamer.touch(rd.fish_btn)
            break
    gamer.delay(5)
    #gamer.delay(5)
    gamer.touch(rd.fish_task_column)

    while True:
        if gamer.find_pic(rd.need_skip):
            gamer.delay(1)
            gamer.touch(rd.skip_btn)
            gamer.delay(1)
            if gamer.find_pic(rd.fish_finish):
                gamer.touch(rd.exit)
                gamer.touch(rd.cueDing)
                gamer.delay(4)
                break

for i in range(0,100):
    xuan()
