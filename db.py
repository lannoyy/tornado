from sqlalchemy import create_engine


engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@tornado_db:5432",
    pool_size=20
)
engine.connect()
