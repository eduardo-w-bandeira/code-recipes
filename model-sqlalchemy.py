from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Doxa(Base):
    __tablename__ = 'Doxa'
    order = Column(Integer, primary_key=True)
    abbrev = Column(String)
    chapter = Column(Integer)
    verse = Column(Integer)
    typpe = Column(String)
    text = Column(String)
    revision = Column(String)


engine = create_engine('sqlite:///bla.sqlite3')
Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
ses = Session()
