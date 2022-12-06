from flask import request, redirect, render_template
from app import app, db, session

from app.model.Usuario import Usuario

@app.route("/usuarios/create", methods=["POST"])
def create():
    
    usuario = {
        "nome":request.form["nome"],
        "email":request.form["email"],
        "senha":request.form["senha"],
        "tipo": request.form["tipoUsuario"]
    }
    
    try:
        user = Usuario( usuario["nome"], usuario["email"], usuario["senha"], usuario["tipo"])
        
        db.session.add(user)
        db.session.commit()
        
        session["nome"] = user.toJson()["nome"]
        session["email"] = user.toJson()["email"]
        session["tipo"] = user.toJson()["tipo"]
        
        return redirect("/homepage")

    except Exception as e:  
        print(e)
        return redirect("/cadastro")  

@app.route("/usuarios/read", methods=["POST"])
def read():
    usuario = {
        "email":request.form["email"],
        "senha":request.form["senha"]
    }   
     
    try:
        user = Usuario.query.filter_by(email=usuario["email"]).first() # Consulta o banco de dados utilizando a chave "email" e retorna o primeiro objeto encontrado
        dic_user = user.toJson() # Tranforma o objeto retornado em uma condição {chave : valor} que pode ser lida pelo backend
        
        if user and dic_user["senha"] == usuario["senha"]:
            
            session["nome"] = dic_user["nome"]
            session["email"] = dic_user["email"]
            session["senha"] = dic_user["senha"]
            session["tipo"] = dic_user["tipo"]
        
            return redirect("/search")
       
        raise Exception
        
    except Exception as e:
        print(e)
        return redirect("/login")

@app.route("/editarNome", methods=["POST"])
def editarNome():
    body = {
        "nome" : request.form["nome"],
        "senha" : request.form["senha"]
    }
    try:
        user = Usuario.query.filter_by(email=session["email"]).first()
        
        senha = body["senha"]
        
        if senha == user.toJson()["senha"]:
            session["nome"] = body["nome"]
            user.nome = body["nome"]
            
            db.session.add(user)
            db.session.commit()
            
            return redirect("/")
        else:
            print("senha errada")
        raise Exception
    
    except Exception as e:
        print(e)
        return redirect('/edit/nome')
    

@app.route("/editarEmail", methods = ["POST"])
def editarEmail():
    body = {
        "email" : request.form["email"],
        "senha" : request.form["senha"]
    }
    try:
        user = Usuario.query.filter_by(email=session["email"]).first()
        senha = body["senha"]
        
        if senha == user.toJson()["senha"]:
            session["email"] = body["email"]
            user.email = body["email"]
            
            db.session.add(user)
            db.session.commit()
            
            return redirect("/")
        else:
            print("senha errada")
        raise Exception
    
    except Exception as e:
        print(e)
        return redirect('/edit/email')
    
@app.route("/editarSenha", methods = ["POST"])
def editarSenha():
    body = {
        "novaSenha" : request.form["novaSenha"],
        "senha" : request.form["senha"]
    }
    try:
        user = Usuario.query.filter_by(email=session["email"]).first()
        senha = body["senha"]
        
        if senha == user.toJson()["senha"]:
            session["senha"] = body["novaSenha"]
            user.senha = body["novaSenha"]
            
            db.session.add(user)
            db.session.commit()
            
            return redirect("/")
        else:
            print("senha errada")
        raise Exception
    
    except Exception as e:
        print(e)
        return redirect('/edit/senha')