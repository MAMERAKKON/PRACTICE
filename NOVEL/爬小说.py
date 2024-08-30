# 怎么发送
import requests
from lxml import etree
from lxml.doctestcompare import strip

with open('斗罗大陆.text', 'w') as f:
    f.truncate(0)
# 发送给谁
url = 'https://dl.131437.xyz/book/douluodalu1/1.html'
# 伪装自己
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
while True:

    # 发送请求
    resp = requests.get(url, headers = headers)

    # 设置编码
    resp.encoding = 'utf-8'

    # 响应信息
    # print(resp.text)

    e = etree.HTML(resp.text)
    body = e.xpath('//div[@class = \'m-post\']/p/text()')

    title = e.xpath('string(//div[@class = \'entry-tit\']/h1)')
    print(title)
    # print(body)
    newbody = ''
    for i in body:
        i = i.strip()
        i += '\n'
        newbody += i

    url = 'https://dl.131437.xyz' + e.xpath('//tbody/tr/td[2]/a/@href')[0]
    print(url)
    # 保存

    with open('斗罗大陆.text', 'a', encoding='utf-8') as f:
        f.write(title + '\n\n' + newbody + '\n\n\n\n')

    if url == 'https://dl.131437.xyz/book/douluodalu1/10.html':
        break