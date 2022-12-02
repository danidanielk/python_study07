# 파일로부터 데이터를 읽어와서  프로그램에서 활용하기 위함
# 프로그램에서 만들어낸 데이터를 파일 형태로 저장하기 위함

# 파일 열기 -> 작업(읽기, 쓰기) -> 파일 꼭 닫기 필수.

# txt파일 / csv파일 두종류로 데이터를 다루는 작업을 합니다.




# # 1. 파일에 내용 쓰기 write
# file = open("C:/Users/NT731QCJ-K582D/Desktop/test/pythonFile/test.txt","w",encoding="UTF-8") 
# #역슬래시를 슬래시로 바꾸기  //  w모드는 덮어쓰기 모드임.
# file.write("안녕하요")
# print("업로드 완료")
# file.close()


# # 2. 파일에 내용 추가 append
# file = open("C:/Users/NT731QCJ-K582D/Desktop/test/pythonFile/test.txt","a",encoding="UTF-8")
# file.write("안녕하하요")
# print("업로드 완료")
# file.close() 


# 3. 파일 내용 읽어오기 read
# 3-1. 파일 전체 읽어오기
file=open("C:/Users/NT731QCJ-K582D/Desktop/test/pythonFile/test.txt","r",encoding="UTF-8")
data= file.read()
print(data)
file.close()

# 3-2. 파일 한줄씩 읽어오기.
# file=open("C:/Users/NT731QCJ-K582D/Desktop/test/pythonFile/test.txt","r",encoding="UTF-8")
# while True: 
    # data=file.readline()
    # print(data)
    # if data =="":
        # break
# file.close
