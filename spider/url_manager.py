#coding=utf-8
# Created by feizi at 2016/2/25

#url管理器
class UrlManager(object):
    #构造函数（初始化待爬取的url列表，和已爬取的url列表）
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    #添加一条待爬取的url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            #该url既不在待爬取url中也不在已爬取url列表中
            self.new_urls.add(url)

    #添加待爬取的url列表(批量添加)
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            #循环添加
            self.add_new_url(url)

    #判断是否有带爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    #获取一条待爬取的url
    def pop_new_url(self):
        #从待爬取的url列表中取出一条url，pop()出栈，先取出再移除
        new_url = self.new_urls.pop()
        #取出一条待爬取的url之后，需要对该条url进行标记，添加进已爬取的url列表中，表示已经爬取过,避免重复爬取
        self.old_urls.add(new_url)
        #返回待爬取的url
        return new_url
