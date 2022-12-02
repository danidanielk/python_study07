# 인설트 방법
from cx_Oracle import connect

# 1.dB연결
con=connect("danieldb/1@192.168.123.102:1521/xe") #cx_oracle 로 임포트

# 2.data 확보
n= input("커피 이름: ")
p= int(input("가격: "))
b= input("원두 이름: ")

# 3.spl문 작성
sql = "insert into coffee values(coffee_seq.nextval,'%s',%d,'%s')"%(n,p,b)

# 4.db관련 작업(sql문을 서버로전송 , 실행, 결과 받기):총괄객체
cur = con.cursor()#자바의 pstmt 역할

# 5.수행(sql문을 서버로 전송, 실행, 결과받기)
cur.execute(sql)

# 6.결과처리 (영향받은 행이 하나면?)
if cur.rowcount ==1:
    print("Success")
    con.commit()    # commit 을해야 서버에 반영 

con.close()