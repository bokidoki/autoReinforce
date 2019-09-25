import os
import shutil

dir = "./tar"
tarDir = "./signed"

def rename():
    print("============开始重命名============")
    apks = os.listdir(dir)
    for apk in apks:
        nameSpaces = apk.split("_")
        name = nameSpaces[0]
        apkname = name.split("-")[0] + "-" + nameSpaces[len(nameSpaces) - 1]
        os.rename(dir + "/" + apk, dir + "/" + apkname)
    print("============重命名结束============")

def extractTarget():
    print("============开始提取文件============")
    dirs = os.listdir(tarDir)
    if not os.path.exists("tar"):
        os.mkdir("tar")
    for dir in dirs:
        apks = os.listdir(tarDir + "/" + dir)
        for apk in apks:
            if apk.endswith(dir + ".apk"):
                path = tarDir + "/" + dir + "/" + apk
                # 读取apk渠道
                print("============输出渠道信息============")
                cmd = "java -jar walle-cli-all.jar show {0}".format(path)
                os.system(cmd)
                shutil.move(path, "./tar")
    print("============提取文件完成============")

def findFile(fileSuffix):
    files = os.listdir()
    for i in range(0, len(files)):
        file = files[i]
        if file.endswith(fileSuffix):
            return file


