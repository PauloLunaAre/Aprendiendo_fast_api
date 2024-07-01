
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#User Model
class User(BaseModel): #Schema
    username:str
    password:str
    nombre:str
    apellido:str
    direccion:Optional[str]
    telefono:int
    correo:str
    creacion:datetime = datetime.now()

class UpdateUser(BaseModel): #Schema
    username:str = None
    password:str = None
    nombre:str = None
    apellido:str = None
    direccion:str = None
    telefono:int = None
    correo:str = None

class ShowUser(BaseModel):
    username:str
    nombre:str
    correo:str
    class Config():
        from_attributes = True