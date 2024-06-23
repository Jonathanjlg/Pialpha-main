from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela

class Tecnico(db.Model):
    __tablename__ = "tecnico"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome  = db.Column(db.String(80))
    cpf = db.column(db.String(20))
    telefone  = db.Column(db.String(20))
    email  = db.Column(db.String(30))
    senha  = db.Column(db.String(30))
    confirma_senha  = db.Column(db.String(30))
    fk_tecnico_id= db.Column(db.Integer,db.ForeignKey('tecnico.id'))