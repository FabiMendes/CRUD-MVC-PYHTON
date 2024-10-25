from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Turma, Professor

turma_blueprint = Blueprint('turmas', __name__)

@turma_blueprint.route('/')
def listar_turmas():
    turmas = Turma.query.all()
    return render_template('turma_view.html', turmas=turmas)

@turma_blueprint.route('/adicionar', methods=['GET', 'POST'])
def adicionar_turma():
    if request.method == 'POST':
        descricao = request.form['descricao']
        professor_id = request.form['professor_id']
        ativo = 'ativo' in request.form
        nova_turma = Turma(descricao=descricao, professor_id=professor_id, ativo=ativo)
        db.session.add(nova_turma)
        db.session.commit()
        return redirect(url_for('turmas.listar_turmas'))
    professores = Professor.query.all()
    return render_template('adicionar_turma.html', professores=professores)

@turma_blueprint.route('/deletar/<int:id>', methods=['POST'])
def deletar_turma(id):
    turma = Turma.query.get(id)
    db.session.delete(turma)
    db.session.commit()
    return redirect(url_for('turmas.listar_turmas'))
