from fastapi import APIRouter, Depends
from app.schemas import User, ShowUser, UpdateUser
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models
from typing import List

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

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

@router.patch('/{user_id}')
def actualizar_usuario(user_id:int, updateUsuer:UpdateUser, db:Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id)
    if not usuario.first():
        return {"Respuesta" :  "usuario no encontrado!!"}
    usuario.update(updateUsuer.dict(exclude_unset=True))
    db.commit()
    return {"Respuesta " : "Usuario actualizado correctamente!" }