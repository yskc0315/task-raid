from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DB接続用クラス（engine, SessionLocalのみ持つ）
DATABASE_URL = "sqlite:///task_raid.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)