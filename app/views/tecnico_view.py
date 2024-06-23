from app import app
from flask import render_template, redirect, url_for, request
from app.forms import tecnico_form
from app.models import tecnico_model # Corrigir importação do modelo Cliente
from app import db

@app.route("/cadtecnico", methods=["POST", "GET"])
def cadastrar_tecnico():
    form = tecnico_form.TecnicoForm()
    if form.validate_on_submit():
        nome = form.nome.data
        cpf = form.cpf.data
        telefone = form.telefone.data
        email = form.email.data
        
        tecnico = tecnico_model.Tecnico(nome=nome, cpf=cpf, telefone=telefone, email=email)
        
        try:
            db.session.add(tecnico)
            db.session.commit()
            if request.method == 'POST':
             return redirect(url_for('listar_tecnico'))  # Redireciona para a lista de clientes após o cadastro
        except Exception as e:
            print(f"Erro ao cadastrar tecnico: {str(e)}")
    
    return render_template("tecnico/form_tecnico.html", form=form, editar=False)