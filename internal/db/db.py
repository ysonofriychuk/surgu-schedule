# https://pythonru.com/biblioteki/vvedenie-v-sqlalchemy

from sqlalchemy import create_engine

from internal.db.entity.user import Base

engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/sqlalchemy_tuts")


Base.metadata.create_all(engine)

