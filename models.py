from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

# テーブル定義用クラス
Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    difficulty = Column(Integer)
    completed = Column(Boolean)
    exp = Column(Integer)