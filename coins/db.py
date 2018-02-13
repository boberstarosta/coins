from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from . import settings


engine = create_engine(settings.DATABASE_PATH)
Session = sessionmaker(bind=engine)


def get_session():
    return Session()
