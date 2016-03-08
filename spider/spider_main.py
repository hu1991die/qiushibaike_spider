#coding=utf-8
# Created by feizi at 2016/2/25
import datetime

from spider import url_manager
from spider import html_downloader
from spider import html_parser
from spider import html_outputer

#spider entrance入口
class SpiderMain(object):
    #构造器中初始化加载系统模块
    def __init__(self):
        #url管理器
        self.urlManager = url_manager.UrlManager()
        #页面下载器
        self.downLoader = html_downloader.HtmlDoenLoader()
        #页面数据解析器
        self.parser = html_parser.HtmlParser()
        #页面渲染器
        self.outputer = html_outputer.HtmlOutputer()

    #爬虫调度抓取
    def craw(self, root_url):
        #计数
        count = 1
        #将页面中待爬取的url列表添加进URL管理器中存放
        self.urlManager.add_new_url(root_url)

        #开始时间
        start_time = datetime.datetime.now()

        #循环爬取页面（如果待爬取url列表不为空，则一直循环爬取）
        while self.urlManager.has_new_url():
            #捕获异常信息
            try:
                #获取待爬取的URL链接
                new_url = self.urlManager.pop_new_url()
                print 'at present, it craws %d : %s ' % (count, new_url)

                #爬取url对应的html页面内容
                html_content = self.downLoader.download(new_url)
                #解析html页面内容，获取有效数据以及新的url链接
                new_urls, new_datas = self.parser.parse(new_url, html_content, count)
                #将新的url添加进url管理器中，等待下一次爬取
                self.urlManager.add_new_urls(new_urls)
                #采集数据信息
                self.outputer.collect_data(new_datas)
                #写文件
                self.outputer.writeTxt(new_datas)

                #总共35页
                if count == 36:
                    break
                count = count + 1
            except:
                print 'craw qiushibaike information failed...'
        end_time = datetime.datetime.now()
        print '总共耗时：%s 秒' % (end_time - start_time).seconds

        #将采集到的信息输出到一个新的html页面中
        self.outputer.output_html()

#爬虫入口
if __name__ == "__main__":
    root_url = "http://www.qiushibaike.com/"
    spider = SpiderMain()
    spider.craw(root_url)