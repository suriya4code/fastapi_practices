from sqlalchemy.orm import Session

from database import SessionLocal


class Database:
    def __init__(self):
        self._session = SessionLocal()

    def get_session(self) -> Session:
        return self._session


db = Database()


def get_db() -> Session:
    try:
        yield db.get_session()
    finally:
        db.get_session().close()