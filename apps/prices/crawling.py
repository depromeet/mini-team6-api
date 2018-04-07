import json
import datetime

from bs4 import BeautifulSoup
import requests

def crawling_result():
    #crawling
    url = 'http://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%84%9C%EC%9A%B8%20%EC%B1%84%EC%86%8C%EB%A5%98%20%EC%86%8C%EB%A7%A4%EA%B0%80'
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url, headers={"USER-AGENT":u_a})
    soup = BeautifulSoup(response.text, 'html.parser')

    #parsing date
    date = soup.find("span",{"class":"more"})
    result_date = date.text.split(" ")[0]
    result_date = result_date.replace('.',"-")[:-1]

    #parsing contents
    contents = soup.find("div",{"class": "detail"})
    contents_table = contents.find("table",{"class":"list_over"})
    contents_table_tbody = contents_table.find("tbody")

    tr_all = contents_table_tbody.findAll("td")

    cnt = 0
    result = []
    component = {}
    name = ''

    for c in tr_all:
        if cnt % 4 == 0:
            component["name"]=c.text

        elif cnt % 4 == 1:
            name_list = c.text.split("/")
            component["unit"]= name_list[1].strip()

        elif cnt % 4 == 2:
            component["price"]= int(c.text.replace(',',''))

        elif cnt % 4 == 3:
            component["date"]=result_date
            result.append(component)
            component ={}

        cnt = cnt + 1
        
    return result