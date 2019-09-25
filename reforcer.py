import os
import sys
import signer
import tools

sid = ""
skey = ""
downloadDir = "./legu"
bash = "java -Dfile.encoding=utf-8 -jar ms-shield.jar -sid {sid} -skey {skey} -uploadPath {uploadPath} -downloadPath {downloadPath}"

def reforce():
    print("============开始加固============")
    tar = tools.findFile("apk")
    if(not tar):
        raise Exception("didn't find apk, do you put it in root?")
    apk = tar
    if not os.path.exists(downloadDir):
        os.mkdir(downloadDir)
    if len(sid) > 0 and len(skey) > 0:
        cmd = bash.format(sid=sid, skey=skey, uploadPath=apk, downloadPath=downloadDir)
        os.system(cmd)
        print("============加固完成============")
        return True
    else:
        raise Exception("pls set sid & skey value in reforcer.py")