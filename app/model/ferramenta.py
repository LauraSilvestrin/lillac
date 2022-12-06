from app import db

class Ferramenta(db.Model):
    __tablename__ = "ferramentas"
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String())
    descricao = db.Column(db.String())
    link = db.Column(db.String())
    empresa = db.Column(db.String())
    
    def __init__(self, titulo, descricao, link, empresa):
        self.titulo = titulo
        self.descricao = descricao
        self.link = link
        self.empresa = empresa
        
    def toJson(self):
        return {"id":self.id, "titulo":self.titulo, "descricao":self.descricao, "link":self.link, "empresa":self.empresa}

