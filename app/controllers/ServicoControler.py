from flask import request, redirect, render_template
from app import app
from app import db

from app.model.Usuario import Usuario
from app.model.Servico import Servico
from app.model.ferramenta import Ferramenta

@app.route("/cadastro/servico/", methods=["POST"])
def createServico():

    Servico = {
        "titulo":request.form["titulo"],
        "descricao":request.form["descricao"],
        "endereco":request.form["endereco"],
        "numero":request.form["numero"]
        
    }


@app.route("/servicos/<servico>")
def mostrarServico(servico):
    consulta = Servico.query.filter_by(tipo=servico).all()
    tipo = servico
    lista = []
    
    for i in consulta:
        lista.append(i.toJson())
        
    print(lista)    

    return render_template(f"{tipo}.html", lista=lista)
