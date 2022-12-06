from flask import request, redirect, render_template
from app import app
from app import db

from app.model.ferramenta import Ferramenta

@app.route("/cadastro/ferramenta/", methods=["POST"])
def createFerramenta():

    ferramenta = {
        "titulo":request.form["titulo"],
        "descricao":request.form["descricao"],
        "link":request.form["link"],
        "empresa":request.form["empresa"]
        
    }

    try:

        ferramenta = Ferramenta(ferramenta["titulo"], ferramenta["descricao"], ferramenta["link"], ferramenta["empresa"])
        
        db.session.add(ferramenta)
        db.session.commit()
        
        return redirect("/homepage")

    except Exception as e:  
        print(e)
        return redirect("/homepage")

@app.route("/servicos/ferramenta", )
def mostrarFerramenta():
    
    consulta = Ferramenta.query.all()
    tipo = "ferramenta"
    lista = []
    
    for i in consulta:
        lista.append(i.toJson())
        
    print(lista)    

    return render_template(f"{tipo}.html", lista=lista)


