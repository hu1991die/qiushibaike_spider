#coding=utf-8
# Created by feizi at 2016/2/25

#html解析器
import re
import urlparse

from bs4 import BeautifulSoup

class HtmlParser(object):
    #解析html
    def parse(self, page_url, html_content, count):
        if page_url is None or html_content is None:
            return

        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup, count)
        new_datas = self._get_new_data(page_url, soup)

        return new_urls, new_datas

    #获取页面中下一页的url链接
    def _get_new_urls(self, page_url, soup, count):
        #定义一个集合
        new_urls = set()

        #http://www.qiushibaike.com/8hr/page/19
        new_url = '/8hr/page/' + str(count)
        new_full_url = urlparse.urljoin(page_url, new_url)
        new_urls.add(new_full_url)

        return new_urls

    #获取页面中的有效数据
    def _get_new_data(self, page_url, soup):
        #定义字典，
        res_data = {}

        #定义url、author、content、vote、comment列表
        url_list = []
        author_list = []
        content_list = []
        vote_list = []
        comment_list = []

        root_nodes = soup.find_all('div', class_='article block untagged mb15')
        if root_nodes is None and len(root_nodes) > 0:
            return

        #循环遍历根节点
        for root_node in root_nodes:
            #url
            url_list.append(page_url)

            #author
            author_node = root_node.find('div', class_='author clearfix')
            h2_node = author_node.find('h2')
            author_list.append(h2_node.get_text())

            #content
            content_node = root_node.find('div', class_='content')
            content_list.append(content_node.get_text())

            #vote
            vote_node = root_node.find('span', class_='stats-vote')
            vote_i_node = vote_node.find('i', class_='number')
            vote_list.append(vote_i_node.get_text())

            #comment
            comment_node = root_node.find('span', class_='stats-comments')
            comment_i_node = comment_node.find('i', class_='number')
            comment_list.append(comment_i_node.get_text())

        res_data['url'] = url_list
        res_data['author'] = author_list
        res_data['content'] = content_list
        res_data['vote'] = vote_list
        res_data['comment'] = comment_list

        return res_data