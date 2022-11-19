from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session
from sqlalchemy import Column, Integer, String, Date, ARRAY
from sqlalchemy import create_engine, ForeignKey

engine = create_engine('postgresql://postgres:12345@127.0.0.1:5432/cafe')
connection = engine.connect()
Base = declarative_base()
Session = session.sessionmaker(bind=engine)
session = Session()


class Tables(Base):
    __tablename__ = 'tables'
    id = Column('table_id', Integer(), primary_key=True)
    position = Column(ARRAY(Integer))


Base.metadata.create_all(engine)

table1 = Tables(
    id=1, position=[1, 1])
session.add(table1)
session.commit()
print(table1.id)
