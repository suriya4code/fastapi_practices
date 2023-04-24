from fastapi import FastAPI


apiv1 = FastAPI()

@apiv1.get('/')
def index():
    return {"Name": "Version1"}