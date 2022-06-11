from cgitb import handler
from urllib import response
import requests
import json

header1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'}

data1 = {'code':'','email':'xiaofuniubi111@163.com','passwd':'kitholt1017'}

ciaoci_data = {'code':'','email':'915695510@qq.com','passwd':'12345678'}

data = {
  "appToken":"AT_nO357WOXXdyue688KNQCkBLSmNyJcdWI",
  "content": 'dd，每日的科学上网流量fran已经帮你领取啦',
  "summary":"fran提醒你，今日的每日流量到账啦！",
  "contentType":1,
  "topicIds":[ 
      5147
  ]
}

response1 = requests.post(url= 'https://ovo.ecyjc.com/auth/login', headers = header1, data = data1)
response2 = requests.post(url='https://ovo.ecyjc.com/user/checkin',headers=header1,cookies=response1.cookies)

c_response = requests.post(url= 'https://ovo.ecyjc.com/auth/login', headers = header1, data = ciaoci_data)
c_response = requests.post(url='https://ovo.ecyjc.com/user/checkin',headers=header1,cookies=c_response.cookies)


print(response2.status_code)
print("ciaoci",c_response.status_code)



if(c_response.status_code == 200):
    result = requests.post(url = 'http://wxpusher.zjiecode.com/api/send/message', headers = {'Content-Type':'application/json'}, data = json.dumps(data))
    print(result.text)
