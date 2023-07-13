from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Veiaco(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    valor = db.Column(db.Float)

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        
    def to_dict(self):
        return{
            "id" : self.id, 
            "nome" : self.nome,
            "valor" : self.valor
        }
