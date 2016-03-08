#coding=utf-8
# Created by feizi at 2016/2/25

#html页面信息渲染器
class HtmlOutputer(object):
    #构造函数
    def __init__(self):
        self.datas = []

    #采集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    #写文件
    def writeTxt(self, new_data):
        f = file('spider.txt', 'w+')
        try:
            count = 1
            for data in self.datas:
                for i in range(len(data['url'])):
                    f.writelines('------------------------------------------第%d个--------------------------------------------\n' % count)

                    f.writelines('url链接:%s \n' % (data['url'][i]))
                    f.writelines('段子作者:%s \n' % (data['author'][i].encode('utf-8')))
                    f.writelines('段子内容:%s \n' % (data['content'][i].encode('utf-8').strip('\n')))
                    f.writelines("{0}{1}{2}".format('投票数:', data['vote'][i], '\n'))
                    f.writelines('{0}{1}{2}'.format('评论数:', data['comment'][i], '\n'))

                    count = count + 1
        except Exception,ex:
            print Exception,":",ex
        f.close()

    #html页面渲染
    def output_html(self):
        #定义一个open输出对象，使用写write模式
        fout = open('output.html', 'w')

        fout.write("<!DOCTYPE html>")
        fout.write("""<html lang="en">""")
        fout.write("""<head><meta charset="UTF-8"><title>python爬取糗事百科页面</title></head>""")
        fout.write("""<html lang="en">""")
        fout.write("<body>")
        fout.write("<table>")
        fout.write("<tr>")
        fout.write("<th>url链接</th>")
        fout.write("<th>段子作者</th>")
        fout.write("<th>段子内容</th>")
        fout.write("<th>投票数</th>")
        fout.write("<th>评论数</th>")
        fout.write("</tr>")

        #python 默认的编码格式为ascii，这里需要进行转码
        for data in self.datas:
            for i in range(len(data['url'])):
                fout.write("<tr>")
                fout.write("<td>%s</td>" % data['url'][i])
                fout.write("<td>%s</td>" % data['author'][i].encode('utf-8'))
                fout.write("<td>%s</td>" % data['content'][i].encode('utf-8'))
                fout.write("<td>%s</td>" % data['vote'][i])
                fout.write("<td>%s</td>" % data['comment'][i])
                fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()