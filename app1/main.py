from fastapi import FastAPI
import uvicorn

from api1 import apiv1
from api2 import apiv2


app = FastAPI()

app.mount("/api/v1", apiv1)
app.mount("/api/v2", apiv2)

@app.get('/')
def index():
    return "Hello"

if __name__ == "__main__":
    uvicorn.run("main:app",port=5000, reload=True)