from urllib import request
from urllib import error
import os

import re

from bs4 import BeautifulSoup
from lxml import etree
import xlwt

# from mysql.connector import connect




ZHAOBFIELDS = ['招标', '采购', '投标', '竞选', '谈判', '询价', '竞价', '议标', '购置', '购买', '磋商', '单一来源', '议价', '变更', '更正', '单一', '出让', '比选', '遴选', '答疑', '澄清', '交易', '招租', '比价', '竞租', '邀标', '拍卖', '拍租', '转让', '标段']
ZHONGBFIELDS = ['中标','中选','成交','结果','废标','合同','流标','终止','中止','失败','验收']


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "Referer": "http://jtj.gz.gov.cn/"
}

def zhaobiao(s):
    zhaob = re.findall(r'招标|采购|投标|竞选|谈判|询价|竞价|议标|购置|购买|磋商|单一来源|议价|变更|更正|单一|出让|比选|遴选|答疑|澄清|交易|招租|比价|竞租|邀标|拍卖|拍租|转让|标段', s)
    zhongb = re.findall(r'中标|中选|成交|结果|废标|合同|流标|终止|中止|失败|验收|候选人', s)
    if bool(zhaob) and not bool(zhongb):
        return True
    return False
    

def getListFild(url):

    req = request.Request(url, headers=HEADERS)

    try:
        response = request.urlopen(req, timeout=5)
    except error.HTTPError:
        raise "请求错误"
    text = str(response.read(), 'utf-8')

    return text

def parseListZB(text):
    list_message = {}
    ## BeautifulSoup
    # soup = BeautifulSoup(text, "html.parser")

    # li_list = soup.find('ul', class_='News_list').find_all('li')

    # for li in li_list:
    #     print(li.span.text.replace('\t', ''))
    #     print(li.a['href'])
    #     print(li.a['title'])

    ## css选择器
    # li_list = BeautifulSoup.select('.News_list li')
    # for li in li_list:
    #     time = li.select('span')[0].text
    #     url = li.select('a')[0]['href']
    #     title = li.select('a')[0]['title']
    #     print(time.replace('\t', ''))
    #     print(url)
    #     print(title)

    ## xpath
    html = etree.HTML(text)
    list_li = html.xpath('//ul[@class="News_list"]/li')
    for li in list_li:
        fields = {}
        time = li.xpath('./span/text()')[0].replace('\t', '')
        url = li.xpath('./a/@href')[0]
        title = li.xpath('./a/@title')[0]
        fields['time'] = time
        fields['url'] = url
        fields['title'] = title
        list_message[url] = fields

    return list_message



def getContent(list_message):
    zb_last_message = []
    for message in list_message.values():
        field_message = {}
        url = message['url']
        title = message['title']
        time = message['time']
        if zhaobiao(title):
            req = request.Request(url, headers=HEADERS)
            rsp = request.urlopen(req, timeout=5)
            last_content = parseContent(rsp.read())
            field_message['url'] = url
            field_message['title'] = title
            field_message['time'] = time
            field_message['content'] = last_content
            zb_last_message.append(field_message)
    return zb_last_message


def parseContent(pend_content):
    html = etree.HTML(pend_content)
    content = html.xpath('//div[@class="info_cont"]')[0]
    last_content = etree.tostring(content, encoding='utf-8').decode('utf-8')    # 设置编码
    return last_content

TABLE_FIELDS = ['序号', '标题', '时间', '内容']

def save_db(zb_last_message, excel_name):
    if os.path.isfile(excel_name):
        os.remove(excel_name)
    
    book = xlwt.Workbook()
    sheet = book.add_sheet('message')

    for uid, field in enumerate(TABLE_FIELDS):
        sheet.write(0, uid, field)


    for uid, message in enumerate(zb_last_message):
        uid += 1
        sheet.write(uid, 0, uid)
        sheet.write(uid, 1, message['title'])
        sheet.write(uid, 2, message['time'])
        sheet.write(uid, 3, message['content'])

    book.save(excel_name)


def main():
    url = "http://jtj.gz.gov.cn/zwgg/ywgg/cgxm/zbgg/"
    text = getListFild(url)
    list_message = parseListZB(text)
    zb_last_message = getContent(list_message)
    save_db(zb_last_message, '广州市交通运输局网站.xls')



if __name__ == "__main__":
    main()