import prettytable as pt
import requests
import json
from 买票 import buy_ticket

print('这是一个12306查询，自动购票程序，请根据引导使用！\n'
      '__________________________________________________________________________________')

city = open('city.json', encoding='utf-8')
city_json = json.loads(city.read())

# 输入查询并返回城市代码
dpt_city = input('请输入出发城市：')
arv_city = input('请输入到达城市：')
dpt_date = input('请输入出发日期：')
'''dpt_city = '上海'
arv_city = '武汉'
dpt_date = '2024-09-02' '''
dpt_city_code = city_json[dpt_city]
arv_city_code = city_json[arv_city]

# 获取查询地址
url = f'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={dpt_date}&leftTicketDTO.from_station={dpt_city_code}&leftTicketDTO.to_station={arv_city_code}&purpose_codes=ADULT'

# 发送请求 模拟浏览器对url地址发送请求
headers = {'Cookie':'_uab_collina=172464248648296557720455; JSESSIONID=D8500A0FFFC70B63A6CF90AA9CD8D8A2; tk=fFDSf_stFCfm3Q8Ld7uyg2UJndKCA8nt77uAIjo4BgFByG_3ozD1D0; BIGipServerotn=1540948234.64545.0000; BIGipServerpassport=921174282.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u6B66%u6C49%2CWHN; _jc_save_fromDate=2024-09-01; _jc_save_toDate=2024-08-26; _jc_save_wfdc_flag=dc; uKey=683c16c203c70959e74d7f9331e9a5dd31df5a98aeb5f13f65274816ffa5f90a','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

resp = requests.get(url=url, headers=headers)

# 创建查询结果表格
info = {}

tb = pt.PrettyTable()
tb.field_names = ['序号',
                  '车次',
                  '出发时间',
                  '到达时间',
                  '时长',
                  '商务特等座',
                  '一等座',
                  '二等座',
                  '无座',
                  '是否当天到达']

a = 0
info_table = []
for i in resp.json()['data']['result']:
    element = i.split('|')
    train_num = element[3] # 车次
    dpt_time = element[8] # 出发时间
    arv_time = element[9] # 到达时间
    duration = element[10] # 时长
    bus_pro = element[32] # 商务特等
    primary = element[31] # 一等座
    secondary = element[30] # 二等座
    none = element[26] # 无座
    next_day = '次日到达'
    if dpt_time[:1] < arv_time[:1]:
        next_day = '当日到达'
    info = {'车次': train_num,
            '出发时间': dpt_time,
            '到达时间': arv_time,
            '时长': duration,
            '商务特等座': bus_pro,
            '一等座': primary,
            '二等座': secondary,
            '无座': none,
            '是否当天到达': next_day}
    a += 1
    info_table.append([a, train_num, dpt_time, arv_time, duration, bus_pro, primary, secondary, none, next_day])
    tb.add_row([a, train_num, dpt_time, arv_time, duration, bus_pro, primary, secondary, none, next_day])
print(tb)

# 录入后续购票信息
ticket_num = 0
seat = ''

def ticket_to_choose(n): # 判断班次是否有余票
    if info_table[n][7] != '' and info_table[n][7] != '无':
        return True
    return False

def choose_train(): # 获取乘客购票意象
    num = int(input('您要做第几班列车？：')) - 1

    while True:
        if ticket_to_choose(num):
            break
        num = int(input('这班车已经没有余票，请重新选择：')) -1

    ticket_num = num + 1

    seat = input('请选择座位：窗 A B C 过道 D F\n'
                 '*如果本次列车剩余席位无法满足您的选座需求，系统将自动为您分配席位：')

    check = input(f'请确认您选择的班次：出发站：{dpt_city}，到达站:{arv_city}，\n'
          f'出发时间:{dpt_date} {info_table[num][2]}， 座位：{seat}座\n'
          f'Y/n：')
    if check == 'n':
        choose_train()
    print('正在为您自动购票，请稍后...')
    buy_ticket(dpt_city, arv_city, dpt_date, seat, ticket_num) # 运行购票程序

choose_train()
