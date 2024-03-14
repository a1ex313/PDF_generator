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


class Records(Base):
    __tablename__ = 'records'

    id = Column(Integer(), primary_key=True)
    month = Column(String(200))
    day = Column(String(200))
    user = Column(String(200))
    device = Column(String(200))


url = "postgresql+psycopg2://root:1111@localhost/db_pdf"


def createdb():
    if not database_exists(url):
        print("БД не существует")
        create_database(url)
        engine = create_engine(url)
        Base.metadata.create_all(engine)


def insertdata(month, day, user, device):
    engine = create_engine(url)
    record = Records(
        month=month,
        day=day,
        user=user,
        device=device
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


    records = session.query(Records).all()
    for record in records:
        print(record.id, record.month, record.day, record.user, record.device)
    session.close()

def get_data_conn():
    conn = psycopg2.connect(
        dbname="db_pdf",
        user="root",
        password="1111",
        host="localhost"
    )

    # Создание объекта курсора
    cur = conn.cursor()

    # Выполнение SQL-запроса
    cur.execute("SELECT * FROM records")

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
    for i in range(100):
        insertdata("Март", "12", "Джон", "Телефон")
        insertdata("Март", "09", "Джек", "Планшет")
        insertdata("Март", "18", "Джордж", "Ноутбук")
        insertdata("Февраль", "29", "Павел", "Микроволновка")
        insertdata("Февраль", "26", "Петр", "Холодильник")
        insertdata("Январь", "02", "Петр", "Телефон")
    #getdata()
    #get_data_conn()
