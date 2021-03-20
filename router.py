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
    pypath = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))) + os.sep + 'DailyXueXiWork' + os.sep + 'main1.py'
    print(pypath)
    os.system("python " + pypath)
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
    pypath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + 'DailyHengTai' + os.sep + 'main_daka_now.py'
    os.system("nohup appium &")
    print(pypath)
    os.system("python " + pypath)
    return '立即打卡已执行'

if __name__ == '__main__':
    app.run()