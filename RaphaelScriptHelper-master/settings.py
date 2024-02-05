#图片匹配置信度，0-1之间，默认0.93，如果匹配出错误目标则提高置信度，如果要模糊匹配或高置信度无法匹配则降低置信度
accuracy = 0.8

#缓存文件存放地址，以/结尾
cache_path = './cache/'

#随机延时范围[randomDelayMin,randomDelayMax]，单位秒
randomDelayMin = 0.2
randomDelayMax = 0.5

#点击偏移范围，[0,x]
touchPosRange = 3

#点击延迟范围，[0,x]
touchDelayRange = 15

#滑屏所需时长范围[slideMinVer,slideMaxVer]，单位毫秒 (滑屏操作不能太快，建议最小值设置在500ms以上)
slideMinVer = 500
slideMaxVer = 3000
