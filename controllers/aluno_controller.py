from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Aluno

aluno_blueprint = Blueprint('alunos', __name__)

@aluno_blueprint.route('/')
def listar_alunos():
    alunos = Aluno.query.all()
    return render_template('alunos.html', alunos=alunos)

@aluno_blueprint.route('/adicionar', methods=['GET', 'POST'])
def adicionar_aluno():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        novo_aluno = Aluno(nome=nome, idade=idade)
        db.session.add(novo_aluno)
        db.session.commit()
        return redirect(url_for('alunos.listar_alunos'))
    return render_template('aluno_view.html')

@aluno_blueprint.route('/deletar/<int:id>')
def deletar_aluno(id):
    aluno = Aluno.query.get(id)
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for('alunos.listar_alunos'))
