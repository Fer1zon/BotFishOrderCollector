from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped





class Model(DeclarativeBase):
    pass



class User(Model):
    __tablename__ = "users"

    user_id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str]
