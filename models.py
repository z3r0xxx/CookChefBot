from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer())
    total_messages: Mapped[int] = mapped_column(Integer(), default=0)
    role: Mapped[str] = mapped_column(String())

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, user_id={self.user_id!r}, total_messages={self.total_messages!r}, role={self.role!r})"


class Recipe(Base):
    __tablename__ = "recipes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String())
    text: Mapped[str] = mapped_column(String())
    rate: Mapped[int] = mapped_column(Integer())
    products: Mapped[str] = mapped_column(String())
    image_path: Mapped[str] = mapped_column(String())

    def __repr__(self) -> str:
        return f"Recipe(id={self.id!r}, title={self.title!r}, text={self.text!r}, rate={self.rate!r}, products={self.products!r}, image_path={self.image_path!r})"


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String())
    calories: Mapped[int] = mapped_column(Integer()) 
    fats: Mapped[int] = mapped_column(Integer())
    carbohydrates: Mapped[int] = mapped_column(Integer())
    proteins: Mapped[int] = mapped_column(Integer())

    def __repr__(self) -> str:
        return f"Product(id={self.id!r}, title={self.title!r}, calories={self.calories!r}, fats={self.fats!r}), carbohydrates={self.carbohydrates!r}), proteins={self.proteins!r})"
