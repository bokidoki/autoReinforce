import os, sys

apkPath = "./signed"
output = "./tar"

def writeChannel():
    print("============重新写入渠道============")
    channelDir = os.listdir(apkPath)
    if (not os.path.exists(output)):
        os.mkdir(output)
    for apk in channelDir:
        if("signed" in apk):
            path = apkPath + "/" + apk
            channelCmd = "java -jar walle-cli-all.jar batch -f channel {0} {1}".format(path, output)
            os.system(channelCmd)
    print("============写入渠道完成============")