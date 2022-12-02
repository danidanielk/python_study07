# (톰캣서버 설치 전임) 오라클 DB와 연동하고 
# cx_Oracle.py 를 설치해야함
# 시작 -> cmd -> pip install cx_oracle +엔터-> 설치 완료.
from cx_Oracle import connect

#sqlplus로 접속할 때 사용하는 주소가 필요함.
#    sqlplus [id]/[pw]@[ip]:[prit]/[sid]
#    sqlplus danieldb/1@192.168.123.102:1521/xe

#혹시 모르니 (접속안될수도있으니 트라이캐치)
try:
    #cx_oracle 로 임포트
    c=connect("danieldb/1@192.168.123.102:1521/xe")
    print("연결성공")
except Exception as e:
    print(e)
c.close()