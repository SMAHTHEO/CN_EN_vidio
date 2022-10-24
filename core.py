

# 引入lib
from translate import Translator
import os
# 翻译引入
import urllib
import hashlib
import random
import requests
import time


# 翻译
def Trans(content, fromLang='auto', toLang='zh'):

    apiurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    appid = 'addid'
    secretyKey = 'keys'
    salt = str(random.randint(32768, 65536))
    sign = appid + content + salt + secretyKey
    sign = hashlib.md5(sign.encode('utf-8')).hexdigest()
    apiurl = apiurl + '?appid=' + appid + '&q=' + urllib.parse.quote(content) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + salt + '&sign=' + sign
    try:
        res = requests.get(apiurl)
        json_res = res.json()
        print(json_res)
        En = str(json_res['trans_result'][0]['dst'])
        return En
    except Exception as e:
        return '翻译失败：----'

# 为文件内字母开头的行进行翻译
def Transfile(file):
    with open(file+".txt","r") as f:
        with open(file+"X.txt","w") as a:
            line = f.readline()
            while line!="":
                if line[0] in Chr:
                    lineCN = Trans(line)
                    a.write(lineCN+"\n")
                a.write(line)
                line = f.readline()
# 定义数据
Chr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#core
Transfile("L1V2")




