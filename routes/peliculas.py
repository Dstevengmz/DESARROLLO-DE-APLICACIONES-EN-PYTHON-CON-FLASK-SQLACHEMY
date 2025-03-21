from flask import request
from app import app,db
from models.genero import *
from models.pelicula import *
from sqlalchemy import exc


@app.route("/pelicula/",methods=['GET'])
def listarPeliculas():
    try:
        mensaje=None
        if request.method=="GET":
            peliculas=Pelicula.query.all()
            listarPeliculas=[]
            for p in peliculas:
                pelicula={
                    "idPelicula":p.idPelicula,
                    "codigo":p.pelCodigo,
                    "titulo":p.pelTitulo,
                    "protagonista":p.pelProtagonista,
                    "duracion":p.pelDuracion,
                    "genero":{
                        "idGenero":p.genero.idGenero,
                        "nombre":p.genero.GenNombre
                    },
                    "foto":p.pelFoto
                }
                listarPeliculas.append(pelicula)
            else:
                mensaje="Tarea no permitida"
                
    except exc.SQLAlchemyError as error:
        
        mensaje=str(error)
    
    return {"mensaje":mensaje,"Peliculas":listarPeliculas}