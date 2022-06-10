import yiban
def main_handler():
	#支持多人打卡
	information=[
		#格式：账号,密码,deviceData（具体查看说明文档）,,【微信提醒token（可省略，获取方式见介绍文档）,提醒类型（可省略)，0不提醒，1仅失败，2全部提醒】
		[ "13823278862", "frank1017", '{"appVersion":"5.0.9","deviceModel":"HUAWEI:ELE-AL00","systemVersion":"10","uuid":"ffffffff-8557-78bc-0033-c5870033c587"}', "Mozilla/5.0 (Linux; Android 10; ELE-AL00 Build/HUAWEIELE-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 yiban_android/5.0.9", "0"]
		#支持多人打卡,打卡地址为昨天的地址
	]
	
	for i in range(len(information)):
		yiban.person(*information[i])
main_handler()
