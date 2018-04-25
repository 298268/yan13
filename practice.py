import requests
from bs4 import BeautifulSoup
import re
import xlwt
import json
def produceSource():
    list1=[]
    for i in range(10):
        url="https://movie.douban.com/top250?start="+str(i*25)
        list1.append(url)
    return list1
def spider(url):
    proxy={"http":"http://183.159.86.7:18118"}
    req=requests.get(url,{"User-Agent":"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0"})
    soup=BeautifulSoup(req.text,"html.parser")
    list1=soup.find_all("div",attrs={"class":"item"})
    for i in list1:
        rank=i.find("em").text
        name=i.find_all("span","title")
        cname=name[0].text
        ename=name[-1].text
        if len(name)==1:
            ename="None"
        else:ename=name[-1].text[3:].strip()

        year=i.find("p",attrs={"class":""}).text
        year=re.findall(r"[0-9]+",year)[0]

        try:
            comments=i.find("span","inq").text

        except BaseException:
            comments="NULL"
        dic[rank] = [cname, ename, year, comments]
def writeInfo(dic,path):
    book=xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet=book.add_sheet("豆瓣最受欢迎电影",cell_overwrite_ok=True)
    col=(u'name',u"englishname",u"year","comment")
    for i in range(0,4):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        data=dic[str(i+1)]
        for j in range(0,4):
            sheet.write(i+1,j,data[j])
    book.save(path)


if __name__ == '__main__':
    dic={}
    for url in produceSource():
            print(url)
            spider(url)
    # with open("aaa.txt","w",encoding="utf-8") as f1:
    #     for i in dic.keys():
    #         f1.write("*"*50+"\n"+i+"\n")
    #         for j in dic[i]:
    #             f1.write(j+"\n")

    # python2可以用file替代open
    writeInfo(dic,"133.xls")


