from fastapi import FastAPI


apiv2 = FastAPI()

@apiv2.get('/')
def index():
    return {"Name": "Version2"}