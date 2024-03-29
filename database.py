from sqlalchemy import String, Boolean, Column, Uuid
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

    id = Column(String, nullable= False, primary_key=True)
    usado = Column(Boolean, nullable=False)

    def __init__(self):
        self.id = str(uuid4())
        self.usado = False