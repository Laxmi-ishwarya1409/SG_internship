from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db_url = "sqlite:///todo.db"

engine = create_engine(db_url,echo = True)

Base = declarative_base()

session = sessionmaker(bind=engine)


def get_db():
    db = session()
    try:
        yield db

    finally:
        db.close()