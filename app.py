from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)


user,password,host,database="root","sena","localhost","peliculas"

cadenConexion= f'mysql+pymysql://{user}:{password}@{host}/{database}'

app.config["SQLALCHEMY_DATABASE_URI"]=cadenConexion
db = SQLAlchemy(app)

if __name__=='__main__':
    from routes.genero import *
    from routes.peliculas import *
    
    
    with app.app_context():
        db.create_all()
        
        
    app.run(port=5555,debug=True)