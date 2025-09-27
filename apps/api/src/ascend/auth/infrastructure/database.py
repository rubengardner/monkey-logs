from sqlmodel import create_engine, Session
from contextlib import contextmanager

# In a real application, this would come from an environment variable
DATABASE_URL = "postgresql://user:password@localhost:5432/ascend_db"

engine = create_engine(DATABASE_URL)


@contextmanager
def get_session():
    with Session(engine) as session:
        yield session
