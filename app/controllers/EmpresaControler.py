from flask import request, redirect, render_template
from app import app
from app import db

from app.model.Empresa import Empresa

@app.route("/cadastro/empresa/", methods=["POST"])
def createEmpresa():

    empresa = {
        "titulo":request.form["titulo"],
        "descricao":request.form["descricao"],
        "endereco":request.form["endereco"],
        "cnpj":request.form["cnpj"]
    }

    try:

        empresa = Empresa(empresa["titulo"], empresa["descricao"], empresa["endereco"], empresa["cnpj"])
        
        db.session.add(empresa)
        db.session.commit()
        
        return redirect("/homepage")

    except Exception as e:  
        print(e)
        return redirect("/homepage")

@app.route("/servicos/empresa", )
def showEmpresa():
    
    consulta = Empresa.query.all()
    tipo = "empresa"
    lista = []
    
    for i in consulta:
        lista.append(i.toJson())
        
    print(lista)    

    return render_template(f"{tipo}.html", lista=lista)