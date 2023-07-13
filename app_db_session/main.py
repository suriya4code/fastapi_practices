from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from dependencies import get_db


app = FastAPI()


@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    # You can use the `db` session to perform database operations
    # For example, query the list of users from the database
    users = db.query(User).all()
    return users