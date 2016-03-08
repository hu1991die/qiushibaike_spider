#coding=utf-8
# Created by feizi at 2016/2/25

#html页面下载器
import urllib2

class HtmlDoenLoader(object):
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'
        #初始化headers
        self.headers = {'User-Agent': self.user_agent}

    #下载html页面内容
    def download(self, url):
        if url is None:
            return None

        try:
            #构建请求的request
            request = urllib2.Request(url, headers=self.headers)
            #利用urlopen获取页面代码
            response = urllib2.urlopen(request)
            if response.getcode() != 200:
                return None

            #将页面转化为utf-8编码
            return response.read().decode('utf-8')

        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u'连接糗事百科失败,错误原因',e.reason
                return None
