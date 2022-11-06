#임포트
import os
import sys
import csv
import django

#환경변수 세팅(뒷부분은 프로젝트명.settings로 설정한다.)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "b4after.settings")
django.setup()

# model import
from books.models import Book

#읽어들일 csv 디렉토리를 각 변수에 담는다.
CSV_PATH = r"C:\Users\gudql\Desktop\B4AFTER\B4AFTER-Back-\books\csv\test_books.csv"

# 카테고리 분류해주는 함수(데이터셋 변경으로 인해 사용X)
# def categories(n):
#     if n == '0':
#         c = '총류'
#     elif n == '1':
#         c = '철학, 심리학, 윤리학'
#     elif n == '2':
#         c = '종교'
#     elif n == '3':
#         c = '사회 과학'
#     elif n == '4':
#         c = '자연 과학'
#     elif n == '5':
#         c = '기술 과학'
#     elif n == '6':
#         c = '예술'
#     elif n == '7':
#         c = '언어'
#     elif n == '8':
#         c = '문학'
#     elif n == '9':
#         c = '역사, 지리, 관광'
#     else:
#         c = '기타'

#     return c

#함수 정의하기 (row부분엔 해당 table의 row명을 적어준다.)
def insert_Book():
    with open(CSV_PATH,"rt",encoding='UTF8') as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for book in data_reader:
            if book:
                isbn = book[2]
                book_title = book[4]
                book_author = book[5]
                year_of_publication = book[6]
                book_publisher = book[7]
                img_l = book[8]
                summary = book[9]
                category = book[11]
                
                #데이터 추출이 잘 되었는지 확인용
                # li = [isbn, book_title, book_author, year_of_publication, book_publisher, img_l, summary, category]
                # print(li)

                # 중복방지용 try/except 구문
                try:
                    Book.objects.create(isbn = isbn, book_title = book_title, book_author = book_author, year_of_publication = year_of_publication, book_publisher = book_publisher, img_l = img_l, summary = summary, category = category)
                except:
                    continue
                
    # DB 업데이트 완료시 메시지 출력
    print('PRODUCT DATA UPLOADED SUCCESSFULY!')
    
insert_Book()