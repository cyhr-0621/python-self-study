# 获取源代码
def gethtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.106.400 QQBrowser/10.9.4626.400'
    }
    try:
        response = requests.get(url, headers=headers)
        html = response.text
        # 获取网页内容
        return html
    except RequestException as e:
        print('request is error!', e)


def writeHtml(html):
    with open('html.txt', 'w', encoding='utf-8') as f:
        f.write(html)
        print("ok")


def readHtml():
    with open('html.txt', 'r', encoding='utf-8') as f:
        html = f.read()
        return html

    # 使用xpath方法，解析原代码，获取目标数据


def parsePage(html):
    htmlNew = etree.HTML(html)
    result = htmlNew.xpath('//*[@id="rankList"]/tr/td/strong/text()|\
                            //*[@id="rankList"]/tr[position()>1]/td[2]/text()|\
                            //*[@id="rankList"]/tr[position()>1]/td/a/text()')
    pos = 0
    for i in range(100):
        if i == 0:
            yield result[i:4]
        else:
            yield result[pos:pos + 4]
        pos += 4
