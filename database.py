from sqlalchemy import TEXT, Integer, Column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from uuid import uuid4

url = "sqlite:///database.db"

engine = create_engine(url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Codigo(Base):

    __tablename__ = "codigos_qr"

    id = Column(TEXT, nullable= False, primary_key=True)
    usado = Column(Integer, nullable=False)

    def __init__(self):
        self.id = str(uuid4())
        self.usado = 0