import psycopg2

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import database_exists, create_database


Base = declarative_base()


class BcData(Base):
    __tablename__ = 'data_bc'

    id = Column(Integer(), primary_key=True)
    fst_param = Column(Integer)
    sec_param = Column(Integer)
    trd_param = Column(Integer)

url = "postgresql+psycopg2://root:1111@localhost/db_barchart"


def createdb():
    if not database_exists(url):
        print("БД не существует")
        create_database(url)
        engine = create_engine(url)
        Base.metadata.create_all(engine)


def insertdata(data1, data2, data3):
    engine = create_engine(url)
    record = BcData(
        fst_param=data1,
        sec_param=data2,
        trd_param=data3
    )

    session = sessionmaker(bind=engine)
    session = Session(bind=engine)
    session.add(record)
    session.commit()
    session.close()


def getdata():
    engine = create_engine(url)
    session = sessionmaker(bind=engine)
    session = Session(bind=engine)


    records = session.query(BcData).all()
    for record in records:
        print(record.fst_param, record.sec_param, record.trd_param)
    session.close()

def get_data_conn():
    conn = psycopg2.connect(
        dbname="db_barchart",
        user="root",
        password="1111",
        host="localhost"
    )

    # Создание объекта курсора
    cur = conn.cursor()

    # Выполнение SQL-запроса
    cur.execute("SELECT * FROM data_bc")

    # Получение результатов запроса
    rows = cur.fetchall()

    # Преобразование результатов в список
    data_list = [list(row) for row in rows]
    print(data_list)

    # Закрыть курсор и соединение
    cur.close()
    conn.close()

if __name__ == "__main__":
    createdb()
    # insertdata(1, 2, 3)
    # insertdata(4, 10, 7)
    # insertdata(3, 15, 15)
    # insertdata(12, 13, 2)
    # insertdata(8, 11, 23)




    #getdata()
    get_data_conn()
