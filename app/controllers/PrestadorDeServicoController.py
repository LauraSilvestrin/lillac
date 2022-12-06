from flask import request, redirect, render_template
from app import app
from app import db

from app.model.PrestadorDeServico import PrestadorDeServico
from app.model.Servico import Servico


@app.route("/cadastro/prestador", methods=["POST"])
def createPrestador():

    prestador = {
        "titulo":request.form["titulo"],
        "numero":request.form["numero"],
        "email":request.form["email"],
        "descricao":request.form["descricao"]
        
    }

    try:

        prestadorDeServico = PrestadorDeServico(prestador["titulo"], prestador["numero"], prestador["email"], prestador["descricao"])
        
        db.session.add(prestadorDeServico)
        db.session.commit()
        
        return redirect("/homepage")

    except Exception as e:  
        print(e)
        return redirect("/homepage")


@app.route("/servicos/prestador", )
def showPrestador():
    
    consulta = PrestadorDeServico.query.all()
    tipo = "prestador"
    lista = []
    
    for i in consulta:
        lista.append(i.toJson())
        
    print(lista)    

    return render_template(f"{tipo}.html", lista=lista)
