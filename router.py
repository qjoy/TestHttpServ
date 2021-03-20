#   coding:utf-8   #强制使用utf-8编码格式
import os

import time
from flask import Flask
from flask import request

from User import UserData

userdict = {}

app = Flask(__name__)

@app.route('/ngrok/xuexi')
def xuexi():
    # 获取用户数据
    user = request.args.get("user")
    curtime = int(time.time())
    curuserlt = userdict.get(user, 0)
    if (curuserlt != 0):
        if (curtime - curuserlt < 3*60*60):
            info = "您请求及时学习太频繁了，上次学习是在:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(curuserlt));
            print(info)
            return info
    else:
        userdict[user] = curtime
    os.system("python /Users/alexq/Library/Mobile\ Documents/com~apple~CloudDocs/code/daily/DailyXueXiWork/main1.py")
    return '即刻学习完成'

@app.route('/ngrok/dakanow')
def ngrok():
    # 获取用户数据
    user = request.args.get("userdaka")
    curtime = int(time.time())
    curuserlt = userdict.get(user, 0)
    if (curuserlt != 0):
        if (curtime - curuserlt < 3 * 60 * 60):
            info = "您请求及时打卡太频繁了，上次打卡请求是在:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(curuserlt));
            print(info)
            return info
    else:
        userdict[user] = curtime
    os.system("export ANDROID_HOME=/Users/alexq/Library/Android/sdk")
    os.system("export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools")
    os.system("nohup appium &")
    os.system("python3 /Users/alexq/Library/Mobile\ Documents/com~apple~CloudDocs/code/daily/DailyHengTai/main_daka_now.py")
    return '立即打卡已执行'

if __name__ == '__main__':
    app.run()