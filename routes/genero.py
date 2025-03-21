from flask import request
from app import app,db
from models.genero import *
from sqlalchemy import exc


@app.route("/genero/",methods=['GET'])
def listarGeneros():
    try:
        mensaje=None
        generos=Genero.query.all()
        listarGeneros=[]
        for g in generos:
            genero={
                "idGenero":g.idGenero,
                "genero":g.genNombre
            }
            listarGeneros.append(genero)
    except exc.SQLAlchemyError as error:
        mensaje=str(error)
    
    return {"mensaje":mensaje,"generos":listarGeneros}