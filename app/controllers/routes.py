from sqlalchemy import null
from app import app, session
from app.model.Empresa import Empresa
from app.model.ferramenta import Ferramenta
from app.model.PrestadorDeServico import PrestadorDeServico
from app.connector import consultar
from flask import render_template, redirect, request


@app.route("/homepage", methods=["GET"])
@app.route('/')
def index():
    if "email" in session:
        return render_template('homepage.html', tipo = session["tipo"])
    return render_template("homepage.html")

@app.route('/login')
def login():
    if "email" not in session:
        return render_template('login.html')
    return redirect("/homepage")

@app.route("/logout")
def logout():
    if "email" in session:
        del session["email"]
    return redirect("/homepage")

@app.route('/usuarios/edit')
def edit():
    if "email" in session:
        return render_template("editarPerfil.html", usuario = session)
    return redirect("/cadastro")

@app.route("/edit/nome")
def editNome():
    return render_template("editNome.html", usuario = session)

@app.route("/edit/email")
def editEmail():
    return render_template("editEmail.html", usuario = session)

@app.route("/edit/senha")
def editSenha():
    return render_template("editSenha.html", usuario = session)

@app.route('/cadastro')
def cadastro():
    if "email" not in session:
        return render_template('cadastro.html')
    return redirect("/homepage")  

@app.route('/cadastrarFerramenta')
def cadastrarFerramentas():

    return render_template('cadastroDeFerramentas.html')

    redirect("/homepage")
    
@app.route('/cadastrarEmpresa')
def cadastrarEmpresas():

    return render_template('cadastroDeEmpresas.html')

    redirect("/homepage")

@app.route('/cadastrarPrestador')
def cadastrarPrestador():

    return render_template('cadastroDePrestadores.html')

    redirect("/homepage")
    
from app.controllers import UsuarioControler

from app.controllers import ServicoControler

from app.controllers import FerramentaControler

from app.controllers import EmpresaControler

from app.controllers import PrestadorDeServicoController


@app.route("/search")
def search():
    if "email" in session:

        if request.args:
            
            search = {
                "search":request.args.get("search")
            }   
            
            buscaPrestadoresDeServico = consultar( "SELECT * FROM prestadoresdeservico where titulo like '%" + search["search"] + "%';")

            
            
            return render_template('search.html', lista = buscaPrestadoresDeServico)
            
        return render_template('search.html', tipo = session["tipo"])
