from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, relationship, backref
from sqlalchemy import Column, Integer, String, Date, ARRAY, Float
from sqlalchemy import create_engine, ForeignKey
from orders.order import Order
engine = create_engine('postgresql://postgres:12345@127.0.0.1:5432/cafe')
connection = engine.connect()
Base = declarative_base()
Session = session.sessionmaker(bind=engine)
session = Session()


class MenuItems(Base):
    __tablename__ = 'menu_items'
    id = Column('menu_id', Integer(), primary_key=True)
    menu_items = relationship(Order, backref='menu_items', lazy=True)
    name = Column(String(30))
    price = Column(Float)
    category = Column(String(30))


Base.metadata.create_all(engine)

menu_item1 = MenuItems(
    id=1, name='margarita', price=250, category='pizza')
session.add(menu_item1)
session.commit()
print(menu_item1.id)
