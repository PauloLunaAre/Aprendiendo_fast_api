from fastapi import FastAPI
import uvicorn
from app.routers import user, auth
from app.db.database import Base, engine

app = FastAPI()
app.include_router(user.router)
app.include_router(auth.router)

#Correr de forma automatica el servidor
if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True)