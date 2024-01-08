import requests
from datetime import datetime
import time

# Author: caseylee

def send_weibo_qun(group_id, msg, annotations, source):
    # 指定url
    url = 'https://api.weibo.com/webim/groupchat/send_message.json'
    # UA 伪装：把 User-Agent 封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Cookie': '',	# 你的 cookie，记得填一下
        'Referer': 'https://api.weibo.com/chat',
        'Authority': 'api.weibo.com',
        'Path': '/webim/groupchat/send_message.json',
        'Scheme': 'https',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    # 处理 url 携带的参数：封装到字典中
    data = {
        'setTimeout':50,
        'content':msg,
        'id':group_id,  # 1. 群号
        'media_type':0,
        'annotations': annotations,	# 2. 这个也填一下
        'is_encoded':0,
        'source': source # 3. 还有这个
    }
    # 发起请求
    response = requests.post(url=url, data=data, headers=headers)
    # 获取响应数据
    page_text = response.text
    print(page_text)
    # 持久化存储
    fileName = 'weibo_chat.json'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName + '保存成功。')

if __name__ == "__main__":

    msg = '看看行不行' # 1. 消息内容
    group_id = '' # 2. 打卡群号
    annotations = '' # 3. annotations
    source = '' # 4. source
    send_weibo_qun(group_id, msg, annotations, source)
    time.sleep(120) # 延迟 2 min，否则一次性发出多条消息

    # 我没写 12 点
    alarm_hour = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
    print("设置成功正在运行...")
    while(True):
        now = datetime.now()
        current_hour = now.strftime("%I")
        current_minute = now.strftime("%M")
        current_seconds = now.strftime("%S")
        current_period = now.strftime("%p")
        # 整点进来
        if(current_hour in alarm_hour):
            if('00' == current_minute):
                if('00' == current_seconds):
                    # 10:00 PM 夜猫
                    if('PM' == current_period and '10' == current_hour):
                        msg = '猫来' # 1. 消息内容
                        group_id = '' # 2. 打卡群号
                        annotations = '' # 3. annotations
                        source = '' # 4. source
                        send_weibo_qun(group_id, msg, annotations, source)
                        time.sleep(120) # 延迟 2 min，否则一次性发出多条消息
                    # 5:00 AM 早鸟
                    elif('AM' == current_period and '05' == current_hour):
                        msg = '早鸟' # 1. 消息内容
                        group_id = '' # 2. 打卡群号
                        annotations = '' # 3. annotations
                        source = '' # 4. source
                        send_weibo_qun(group_id, msg, annotations, source)
                        time.sleep(120) # 延迟 2 min，否则一次性发出多条消息
                    else:	# 持久化 cookie
                        msg = '现在是 ' + str(now)
                        group_id = '' # 2. 打卡群号
                        annotations = '' # 3. annotations
                        source = '' # 4. source
                        send_weibo_qun(group_id, msg, annotations, source)
                        time.sleep(120) # 延迟 2 min，否则一次性发出多条消息