from flask import request
from app import app,db
from models.genero import *
from models.pelicula import *
from models.genero import *
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
                        "nombre":p.genero.genNombre
                    },
                    "foto":p.pelFoto
                }
                listarPeliculas.append(pelicula)
            else:
                mensaje="Tarea no permitida"
                
    except exc.SQLAlchemyError as error:
        
        mensaje=str(error)
    
    return {"mensaje":mensaje,"Peliculas":listarPeliculas}

@app.route("/pelicula/",methods=['POST'])
def addPelicula():
    try:
        mensaje=None
        estado=False
        if request.method=='POST':
            datos=request.get_json()
            genero=Genero.query.get(int(datos['genero']))
            pelicula=Pelicula(
                pelCodigo=datos['codigo'],
                pelTitulo=datos['titulo'],
                pelProtagonista=datos['protagonista'],
                pelDuracion=datos['duracion'],
                pelResumen=datos['resumen'],
                pelFoto=datos['foto'],
                # pelGenero=datos['genero']
                genero=genero)
            db.session.add(pelicula)
            db.session.commit()
            estado=True
            mensaje="Pelicula agregado correctamente"
        else:
            mensaje="Tarea no permitida"
    except exc.SQLAlchemyError as error:
        db.session.rollback()
    return {"estado":estado,"mensaje":mensaje}


@app.route("/pelicula/", methods=['PUT'])
def updatePelicula():
    try:
        mensaje = None
        estado = False
        if request.method == 'PUT':
            datos = request.get_json()
            
            pelicula = Pelicula.query.get(datos['id'])
            
            if pelicula:
                # pelicula.pelCodigo = datos['codigo'],
                # pelicula.pelTitulo = datos['titulo'],
                # pelicula.pelProtagonista = datos['protagonista'],
                pelicula.pelDuracion = datos['duracion']
                # pelicula.pelResumen = datos['resumen'],
                # pelicula.pelFoto = datos['foto'],
                # genero = Genero.query.get(int(datos['genero']))
                # pelicula.genero = genero
                db.session.commit()
                estado = True
                mensaje = "Película actualizada correctamente"
            else:
                mensaje = "Película no encontrada"
        else:
            mensaje = "Tarea no permitida"
    except exc.SQLAlchemyError as error:
        db.session.rollback()
    return {"estado": estado, "mensaje": mensaje}



