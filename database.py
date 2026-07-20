from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# DB接続用クラス（engine, SessionLocalのみ持つ）
DATABASE_URL = "sqlite:///task_raid.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()