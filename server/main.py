from fastapi import FastAPI, status
from routes import auth
app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
def index():
    return {"message":"Hello world"}

app.include_router(auth.router)