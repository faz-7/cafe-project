from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, relationship, backref
from sqlalchemy import Column, Integer, String, Date, ARRAY, Float
from sqlalchemy import create_engine, ForeignKey

engine = create_engine('postgresql://postgres:12345@127.0.0.1:5432/cafe')
connection = engine.connect()
Base = declarative_base()
Session = session.sessionmaker(bind=engine)
session = Session()


class Order(Base):
    __tablename__ = 'orders'
    id = Column('menu_id', Integer(), primary_key=True)
    menu_item_id = Column(Integer(), ForeignKey('menu_items.id'), nullable=False)
    number = Column(Integer())
    status = Column(String(50))
    time_stamp = Column(String(50))


Base.metadata.create_all(engine)

order1 = Order(
    id=1, number=1, menu_item_id=1, status='new order', time_stamp='tete')
session.add(order1)
session.commit()
print(order1.id)
