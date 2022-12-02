# 셀렉트
from cx_Oracle import connect

con=connect("danieldb/1@192.168.123.102:1521/xe")
sql= "select * from coffee order by c_price"

#db 총괄객체 만들기
cur=con.cursor()

#sql문 수행 이렇게하면  slect의 결과가 cur에 튜플로 들어가게 됨.
cur.execute(sql)

for i,ii,iii,iiii in cur:
    print(i,ii,iii,iiii)
con.close()