from bs4 import BeautifulSoup as bs
import requests
import configparser as cp
import os
import json

cnf=cp.ConfigParser()
cnf.read(os.path.realpath(os.path.join(os.path.dirname( os.path.realpath(__file__)),os.path.pardir,"config.ini")),"UTF-8")

convert_rate = lambda s:None if s=="-" else s

def GetTaiwanBank():
    result =[]
    bank_code=4
    url="https://rate.bot.com.tw/xrt"
    para={"Lang":"zh-TW"}
    agent=json.loads( cnf.get("crawler","AGENT_CHROME"))
    req = requests.get(url,params=para,headers=agent)
    
    page = bs( req.text,"html.parser")
    
    tbl = page.find("table",class_="table table-striped table-bordered table-condensed table-hover")
    result
    for tr in tbl.find_all("tr"):
        col=0
        row={}
        for td in tr.find_all("td"):            
            if col == 0:
                row["Code"]=bank_code
                row["Currency"]=td.find("div",style="text-indent:30px;").string.strip()[-4:-1]
            elif col == 1:                 
                row["BuyCash"]=convert_rate(td.string)
            elif col == 2: 
                row["SoldCash"]=convert_rate(td.string)
            elif col == 3: 
                row["Buy"]=convert_rate(td.string) 
            elif col == 4: 
                row["Sold"]=convert_rate(td.string)
            col += 1
        if row:
            result.append(row)

    return result
    
