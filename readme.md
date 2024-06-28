# Dos formas de ejecutar fastapi
    1.- desde la terminal uvicorn main:app
    2.- Agregar las lineas de cofigo 
        if __name__ == '__main__':
            uvicorn.run("main:app", port=8000)
        y luego correr main.py
    