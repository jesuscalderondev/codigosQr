from sqlalchemy import String, Boolean, Column, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from uuid import uuid4

url = "sqlite:///database.db"

engine = create_engine(url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Codigo(Base):

    __tablename__ = "Codigos"

    id = Column(String, nullable= False, primary_key=True)
    usado = Column(Boolean, nullable=False)
    boleto = Column(String, nullable=False)
    vendido = Column(Boolean, nullable=False)

    def __init__(self, boleto):
        self.id = str(uuid4())
        self.usado = False
        self.boleto = boleto
        self.vendido = False