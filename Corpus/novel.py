from bs4 import BeautifulSoup
import requests
import sys


class Download(object):
    def __init__(self):
        self.server = 'http://www.bbiqugew.com'
        self.target = 'http://www.bbiqugew.com/book/69/'
        self.names = []
        self.urls = []
        self.nums = 0
    def get_urls(self):
        req = requests.get(url=self.target)
        req.encoding = 'gbk'
        html = req.text
        div_bf = BeautifulSoup(html, 'html.parser')
        div = div_bf.find_all('div', id='list')
        a_bf = BeautifulSoup(str(div[0]), 'html.parser')
        a = a_bf.find_all('a')
        self.nums = len(a[2:])
        for each in a[2:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self, target):
        req = requests.get(url=target)
        req.encoding = 'gbk'
        html = req.text
        bf = BeautifulSoup(html, 'html.parser')
        texts = bf.find_all('div', id='content')
        texts = texts[0].text.replace('\xa0' * 8, '\n\n')
        return texts

    def writer(self, name, path, text):
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n')


if __name__ == "__main__":
    dl = Download()
    dl.get_urls()
    print('开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '全能奇才.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" % float(i / dl.nums) + '\r')
        sys.stdout.flush()
    print('下载完成')