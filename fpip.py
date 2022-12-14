#fastpip
#version 1.1

import sys
import os
pathornot = os.system("python -V")
if pathornot == 0:
    py=""
else:
    print("WARNING: These computer didn't add an environment variable!")
    py="py -m "
mirrors={"tsinghua":"https://pypi.tuna.tsinghua.edu.cn/simple",
        "ustc":"https://mirrors.ustc.edu.cn/pypi/web/simple",
        "douban":"https://pypi.doubanio.com/simple",
        "aliyun":"https://mirrors.aliyun.com/pypi/simple",
        "bfsu":"https://mirrors.bfsu.edu.cn/pypi/web/simple/",
        "pku":"https://mirrors.pku.edu.cn/pypi/simple/"}
abouttext='''
Use mirroring to quickly download Pypi packages in China.
在中国利用镜像快速下载Pypi的包
Default Mirror: Tsinghua University Open source software mirror(tsinghua)
默认镜像：清华大学开源软件镜像站（tsinghua）
Optional Mirror:
可选镜像：
Tsinghua University Open source software mirror(tsinghua)
清华大学开源软件镜像站(tsinghua)
USTC Open Source Software Mirror(ustc)
中国科学技术大学开源软件镜像站(ustc)
Douban Mirror(douban)
豆瓣镜像站(douban)
Alibaba Open Source Mirror Site(aliyun)
阿里巴巴开源软件镜像站(aliyun)
BFSU Open Source Mirror(bfsu)
北京外国语大学开源镜像站(bfsu)
Peking University Open source Mirror(pku)
北京大学开源镜像站(pku)
'''
helptext='''
help:[COMMAND]
fpip install xxx        |    Download from Tsinghua Mirror
fpip install xxx ustc   |    Download from USTC Mirror
fpip version            |    Viewing the Current Version
fpip about              |    About How to use It
fpip list               |    Viewing the Installation List
fpip help               |    Show This message'''
cmd=sys.argv
if len(cmd) == 1:
    exit()
elif cmd[1] == "install" and len(cmd)==3:
    os.system(py+"pip install "+cmd[2]+" -i https://pypi.tuna.tsinghua.edu.cn/simple")
elif cmd[1] == "install" and cmd[3] in mirrors:
    os.system(py+"pip install "+cmd[2]+" -i "+mirrors[cmd[3]])
elif cmd[1] == "-V" or cmd[1] == "--version" or cmd[1] == "version":
    print("Fast pip for China:")
    print("version 1.1.0208635\n")
    os.system(py+"pip -V")
elif cmd[1] == "list":
    os.system("pip list")
elif cmd[1] == "about":
    print(abouttext)
elif cmd[1] == "help" or cmd[1] == "--help":
    print(helptext)
else:
    print("Wrong Command")
    print(helptext)