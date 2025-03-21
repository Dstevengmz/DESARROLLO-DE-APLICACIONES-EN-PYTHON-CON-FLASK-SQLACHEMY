from flask import request
from app import app,db
from models.genero import *
from sqlalchemy import exc
from flask import session
from app import db


@app.route("/genero/",methods=['GET'])
def listarGeneros():
    try:
        mensaje=None
        generos=Genero.query.order_by(Genero.idGenero).all()
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




@app.route("/genero/",methods=['POST'])
def addGenero():
    try:
        mensaje=None
        estado=False
        if request.method=='POST':
            datos=request.get_json()
            
            genero=Genero(genNombre=datos['genero'])
            db.session.add(genero)
            db.session.commit()
            estado=True
            mensaje="Genero agregado correctamente"
        else:
            mensaje="Tarea no permitida"
    except exc.SQLAlchemyError as error:
        db.session.rollback()
    return {"estado":estado,"mensaje":mensaje}