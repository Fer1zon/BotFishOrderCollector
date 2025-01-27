from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import ForeignKey





class Model(DeclarativeBase):
    pass



class Fish(Model):
    __tablename__ = "fish"
    id : Mapped[int] = mapped_column(primary_key=True)
    type_ : Mapped[str]
    title : Mapped[str]

class Basket(Model):
    __tablename__ = "basket"

    id : Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column(nullable=False)
    fish_id : Mapped[int] = mapped_column(ForeignKey("fish.id"), nullable=False)
    title : Mapped[str]
    count : Mapped[float]