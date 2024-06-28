from fastapi import APIRouter, Depends
from app.schemas import User, UserId, ShowUser
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models
from typing import List

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

usuarios = []

@router.get('/', response_model=List[ShowUser])
def obtener_usuarios(db:Session = Depends(get_db)):
    data = db.query(models.User).all()
    return data

@router.post('/')
def crear_usuario(user:User, db:Session = Depends(get_db)):
    
    usuario = user.dict()
    nuevo_usuario = models.User(
        username=usuario["username"],
        password=usuario["password"],
        nombre=usuario["nombre"],
        apellido=usuario["apellido"],
        direccion=usuario["direccion"],
        telefono=usuario["telefono"],
        correo=usuario["correo"],
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return {"Respuesta" : "Usuario creado satisfactoriamente!!"}

@router.delete('/{user_id}')
def eliminar_usario(user_id:int, db:Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id)
    if not usuario.first():
        return {"Resupuesta" : "usuario no encontrado"}
    usuario.delete(synchronize_session=False)
    db.commit()
    return {"Respuesta" : "usuario eliminado correctamente"}


@router.get('/{user_id}', response_model=ShowUser)
def obtener_usuario(user_id:int, db:Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id).first()
    if not usuario:
        return {"Respuesta" : "usuario no encontrado"}
    return usuario


@router.post('/obtener_usuario')
def obtener_usuario_2(user_id:UserId):
    for user in usuarios:
        if user["id"] == user_id.id:
            return {"usuario":user}
    return {"Respuesta":"Usuario no encontrado"}


@router.put('/{user_id}')
def actualizar_usuario(user_id:int, updateUsuer:User):
    for index,user in enumerate(usuarios):
        if user["id"] == user_id:
            usuarios[index]["id"] = updateUsuer.dict()["id"]
            usuarios[index]["nombre"] = updateUsuer.dict()["nombre"]
            usuarios[index]["apellido"] = updateUsuer.dict()["apellido"]
            usuarios[index]["direccion"] = updateUsuer.dict()["direccion"]
            usuarios[index]["telefono"] = updateUsuer.dict()["telefono"]
            return {"Respuesta " : "Usuario actualizado correctamente!!" }
    return {"Respuesta " : "Usuario no encontrado" }