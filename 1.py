import re # 导入正则
import requests # 导入requests
from lxml import etree # 导入lxml的etree

# 用来存放学校信息，设置为全局变量
info_list = []

class University():
    def info(self):
        # 设置请求头
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        }
        # 请求数据
        response = requests.get('http://www.qianmu.org/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D', headers=headers)
        # 将数据转换成lxml类型
        html = etree.HTML(response.text)
        data_list = html.xpath('//div[@id="content"]/table//tr/td[1]//text()')
        for i in range(1, len(data_list) ): # data_list用来计算列的长度
            ranking = str(html.xpath('//div[@id="content"]/table//tr[%s]//td[1]//text()' % (str(i))))[2:-2] # 学校排名
            name_Chinese = str(html.xpath('//div[@id="content"]//tr[%s]/td[2]//text()' % (str(i))))[2:-2] # 学校的中文名
            name_English = str(html.xpath('//div[@id="content"]//tr[%s]/td[3]//text()' % (str(i))))[2:-2] # 学校的英文名
            address = str(html.xpath('//div[@id="content"]//tr[%s]/td[4]//text()' % (str(i))))[2:-2] # 学校的地址
            # 应为地址有的前面会有‘\\xa0’，所以设置消除其的正则表达式
            re_add = re.findall(r'^\\xa0(.*)', address) # 消除‘\\xa0’的正则表达式
            if re_add:
                info_list.append([ranking, name_Chinese, name_English, str(re_add)[2:-2] ])
            else:
                info_list.append([ranking, name_Chinese, name_English, address])

    # 输出学校信息查看
    def Output(self):
        for value in info_list:
            print(value)
# 主函数
if __name__ == '__main__':
    # 创建对象
    a = University()
    # 调用对象方法,获取信息并存储在info_list里
    a.info()
    # 调用对象方法输出学校信息
    a.Output()