from database import engine
from models import Base

# テーブル作成用クラス
Base.metadata.create_all(binde=engine)