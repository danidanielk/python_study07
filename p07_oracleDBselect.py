from cx_Oracle import connect


#원두를 검색해서 커피종류의 개수와 평균가격 구하기
b=input("원두 : ")
con=connect("danieldb/1@192.168.123.102:1521/xe")
sql="select count(*), avg(c_price) from coffee where c_type = '%s'"%b
cur=con.cursor()
cur.execute(sql)
for i in cur:
    print(i)
con.close()