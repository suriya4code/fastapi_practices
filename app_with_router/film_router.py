from fastapi import APIRouter

tag_name = 'Film'
film_router = APIRouter()

@film_router.get('/', tags=[tag_name])
def films():
    return {"name": "Avatar",
    "genere": "Sci-Fi",
    "description": "Sci-Fi fantasy movie."}