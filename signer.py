import sys, os
import tools

targetDir = "./legu"
signedDir = "./signed"

def autoSign():
    print("============开始签名============")
    files = os.listdir(targetDir)
    for file in files:
        if not os.path.isdir(file):
            if(not os.path.exists(signedDir)):
                os.system("mkdir {0}".format("signed"))
            fileName= targetDir +"/"+file
            zipalignName=signedDir+ "/" +file.split('.apk')[0] + '_zipalign.apk'
            command='zipalign -v -p 4 {0} {1}'.format(fileName, zipalignName)
            os.system(command)
            jks = tools.findFile("jks")
            if(not jks) :
                raise Exception("pls put jks doc in root")
            key_alias = 'bonadeTravel'
            ks_pass = 'bonadetravel888'
            key_pass = 'bonadetravel888'
            apkName=zipalignName.split('.apk')[0]+'_signed.apk'
            command='apksigner sign --ks {0} --ks-key-alias {1} --ks-pass pass:{2} --key-pass pass:{3} --out {4} {5}'.format(jks, key_alias, ks_pass, key_pass, apkName, zipalignName)
            os.system(command)
    print("============签名完成============")