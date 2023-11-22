
from models import *
from logs import logger
from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

engine = create_engine("postgresql://postgres:zrxroot@localhost:5432/CookChefBot")
connection = engine.connect()

def create_user(user_id):
    with Session(autoflush=False, bind=engine) as session:
        existing_user = session.query(User).filter_by(user_id=user_id).first()

        if existing_user is None:
            new_user = User(user_id=user_id)
            session.add(new_user)
            
            try:
                session.commit()
            except IntegrityError as e:
                session.rollback()
                logger.error(f'User user_id {user_id} ↔ Произошла ошибка при создании записи:', e)
        else:
            pass
