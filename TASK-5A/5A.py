from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
start_time=time.time()
Base = declarative_base()
engine = create_engine('postgresql://postgres:admin@localhost:5432/postgres', echo = True)
Session = sessionmaker(bind = engine)
session = Session()

class login(Base):
    __tablename__ = 'login_table'
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    password = Column(String(100), nullable=False)

class finding(Base):
    __tablename__="finding_table"
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    password = Column(String(100), nullable=False)

def Generator(i):
  list1 = []
  for i in range(i):
    fake=Faker()
    list2=[]
    list2.append(fake.email())
    list2.append(fake.password())
    list1.append(list2)
  return list1
Base.metadata.create_all(engine)
Generator(1000)

session.commit()

end_time=time.time()
print(end_time-start_time)
