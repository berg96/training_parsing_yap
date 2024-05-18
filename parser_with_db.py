# Импортируйте все нужные библиотеки.
import requests
from bs4 import BeautifulSoup
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declared_attr, declarative_base, Session

PEP_URL = 'https://peps.python.org/'


class PreBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)


class Pep(Base):
    type_status = Column(String(2))
    number = Column(Integer, unique=True)
    title = Column(String(200))
    authors = Column(String(200))

    def __repr__(self):
        return f'PEP {self.pep_number} {self.name}'

# Создайте модель Pep для таблицы pep в декларативном стиле ORM.
# Атрибуты модели:
# 1. id, целочисленное значение, primary key
# 2. type_status, строка с максимальной длиной 2 символа
# 3. number, целочисленное значение, уникальное
# 4. title, строка с максимальной длиной 200 символов
# 5. authors, строка с максимальной длиной 200 символов


engine = create_engine('sqlite:///sqlite.db')

# Ваш код - здесь:
# создайте таблицу в БД;
# загрузите страницу PEP_URL;
# создайте объект BeautifulSoup;
# спарсите таблицу построчно и запишите данные в БД.
Base.metadata.create_all(engine)
session = Session(engine)
response = requests.get(PEP_URL)
soup = BeautifulSoup(response.text, features='lxml')
tr_tags = soup.select('#numerical-index tbody tr')
for tr_tag in tr_tags:
    td_tags = tr_tag.find_all('td')
    session.add(
        Pep(
            type_status=td_tags[0].text,
            number=int(td_tags[1].text),
            title=td_tags[2].text,
            authors=td_tags[3].text
        )
    )
session.commit()
