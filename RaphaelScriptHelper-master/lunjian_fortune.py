import RaphaelScriptHelper as gamer
import multiprocessing
import testDict as rd
import settings

gamer.deviceType=1

gamer.deviceID='127.0.0.1:62001'

def lunjian():
    while True:
        if  gamer.find_pic(rd.BaoXiang):
            gamer.touch(rd.piPei2)
        elif gamer.find_pic(rd.face):
            gamer.touch(rd.huoDong)
            gamer.touch(rd.fenZheng)
            gamer.touch(rd.piPei)
        else:
            continue
        while(1):
            if gamer.find_pic(rd.zhunBei):
                gamer.touch(rd.exit)
                gamer.touch(rd.cueDing)
                break
            gamer.touch(rd.cueRen) #試著瘋狂點及確認直到退出

        gamer.delay(17)

def fortune():
    gamer.touch(rd.huoDong)
    gamer.touch(rd.yoLi)
    gamer.touch(rd.fortune)
    while(1):
        if gamer.find_pic(rd.fortune_arrive):
            gamer.touch(rd.fortune_start)
            gamer.touch(rd.fortune_pay)
            gamer.touch(rd.fortune_luoBi)
            gamer.touch(rd.fortune_accept)
            gamer.touch(rd.fortune_accept2)
            gamer.touch(rd.fortune_accept2)
            break

#fortune()
lunjian()
