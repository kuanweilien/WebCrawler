from Database.Connection import Con
from Database.DML import DML as Dml
from Database.Type import SqlType as St
from WebCrawler import ExchangeRate as Er
import schedule
import time



def ExchangeRate():
    
    # delete today data
    d = "DELETE FROM TB_EXCHANGE_RATE WHERE RATE_DATE=(SELECT DATE(NOW())); "
    dp=""
    x = Dml(Con(),St.DELETE,d,dp)
    y = x.execute()

    # insert taiwan bank exchange rate 
    i = """INSERT INTO TB_EXCHANGE_RATE(ROW_ID,BANK_CODE,RATE_DATE,CURRENCY,BUY_RATE,SOLD_RATE,CASH_BUY_RATE,CASH_SOLD_RATE)
                                VALUES ((SELECT NEXTVAL(SQ_EXCHANGE_RATE)) ,%s,(SELECT DATE(NOW())),%s,%s,%s,%s,%s );"""
    datas = Er.GetTaiwanBank()
    for row in datas:
        para=(row["Code"],row["Currency"],row["Buy"],row["Sold"],row["BuyCash"],row["SoldCash"])
        print(para)
        dml = Dml(con=Con(),sqlType=St.INSERT,sqlStr= i,para= para)
        dml.execute()
        dml.dispose()

ExchangeRate()

# while True:
#     schedule.run_pending()
#     time.sleep(1)


