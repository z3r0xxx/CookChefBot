
import random
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
                logger.info(f'User user_id {user_id} ↔ Запись успешно создана')
            except IntegrityError as e:
                session.rollback()
                logger.error(f'User user_id {user_id} ↔ Произошла ошибка при создании записи:', e)
        else:
            logger.info(f'User user_id {user_id} ↔ Запись уже существует!')


def get_recipes():
    with Session(autoflush=False, bind=engine) as session:
        existing_recipes = session.query(Recipe).all()
        if existing_recipes is not None:
            return existing_recipes
        else:
            return None


def get_random_recipe():
    all_recipes = get_recipes()
    
    return random.choice(all_recipes)


def get_products_in_recipe(recipe_id):
    with Session(autoflush=False, bind=engine) as session:
        existing_recipe = session.query(Recipe).filter_by(id=recipe_id).first()

        result = []
        for p in existing_recipe.products.split(" "):
            product = session.query(Product).filter_by(id=int(p)).first()
            result.append(product)

    return result


def get_recipe_(recipe_id):
    with Session(autoflush=False, bind=engine) as session:
        existing_recipe = session.query(Recipe).filter_by(id=recipe_id).first()

    return existing_recipe


def add_rate_to_recipe(recipe_id):
    with Session(autoflush=False, bind=engine) as session:
        existing_recipe = session.query(Recipe).filter_by(id=recipe_id).first()
        existing_recipe.rate = existing_recipe.rate + 1

        try:
            session.commit()
            logger.info(f'Recipe recipe_id {recipe_id} ↔ Запись успешно обновлена')
        except IntegrityError as e:
            session.rollback()
            logger.error(f'Recipe recipe_id {recipe_id} ↔ Произошла ошибка при обновлении записи:', e)
