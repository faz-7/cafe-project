from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine, ForeignKey

engine = create_engine('postgresql://postgres:12345@127.0.0.1:5432/cafe')
connection = engine.connect()
Base = declarative_base()
Session = session.sessionmaker(bind=engine)
session = Session()


class Users(Base):
    __tablename__ = 'users'
    id = Column('user_id', Integer(), primary_key=True)
    first_name = Column(String(15))
    last_name = Column(String(15))
    phone = Column(String(11))
    email = Column(String(100))
    password = Column(String(50))


Base.metadata.create_all(engine)

user1 = Users(
    id=1, first_name='ali', last_name='mohammadi', phone='09821345123', email='ali@123a.com', password='12345')
session.add(user1)
session.commit()
print(user1.id)
