import reforcer
import signer
import channel
import tools
import os
import sys

path = sys.argv[0]
if path != "main.py":
    index = path.index("main.py")
    dir = path[0 : index]
    os.chdir(dir)
# 加固
done = reforcer.reforce()
if done:
    # 签名
    signer.autoSign()
    # 签名后会洗掉渠道信息，需要重新写入
    channel.writeChannel()
    # 重命名
    tools.rename()
else:
    print("============加固失败============")