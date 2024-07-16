from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String


class Base(DeclarativeBase):
    """Main Database"""


db = SQLAlchemy(model_class=Base)


class FavVideoGames(db.Model):
    """Table of my favourite video games"""

    __tablename__ = "My Favourite Video Games"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer)
    developer: Mapped[str] = mapped_column(String)
    genre: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    rating: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String)
    cover_art: Mapped[str] = mapped_column(String)
