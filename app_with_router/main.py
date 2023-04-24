from fastapi import FastAPI
from book_router import book_router
from film_router import film_router
import uvicorn

app = FastAPI()
app.include_router(book_router, prefix="/book")
app.include_router(film_router, prefix="/film")


@app.get('/')
def index():
    return "Book or Film?"

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)