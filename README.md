# 项目说明

本项目采用腾讯乐固加固和美团walle渠道工具，请将channel打出的apk包放入apk目录下，请将你的签名文件放在根目录下。

```cmd
# 执行
python main.py
```

在tar目录下提取渠道包

## 文件说明

reforcer.py 加固  
请将乐固的sid和skey填入该文件对应的位置
signer.py 签名  
tools.py 工具类(重命名)  

## 渠道配置

在channel文件中配置渠道信息，一个渠道占一行

## 其它

bonade_travel.jks 签名文件  
ms-shield.jar 乐固加固脚本  
walle-cli-all.jar walle命令行工具

## tips

该脚本采用乐固加固，在360市场不能通过，建议将release包先进行360加固，在重新签名后上传360应用市场
