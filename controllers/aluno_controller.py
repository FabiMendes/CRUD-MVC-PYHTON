from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Aluno, Turma

aluno_blueprint = Blueprint('alunos', __name__)

@aluno_blueprint.route('/')
def listar_alunos():
    alunos = Aluno.query.all()
    return render_template('aluno_view.html', alunos=alunos)

@aluno_blueprint.route('/adicionar', methods=['GET', 'POST'])
def adicionar_aluno():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        turma_id = request.form['turma_id']
        data_nascimento = request.form['data_nascimento']
        nota_primeiro_semestre = request.form['nota_primeiro_semestre']   
        nota_segundo_semestre = request.form['nota_segundo_semestre']
        media_final = (float(nota_primeiro_semestre) + float(nota_segundo_semestre)) / 2
        novo_aluno = Aluno(nome=nome, idade=idade, turma_id=turma_id, data_nascimento=data_nascimento,
                           nota_primeiro_semestre=nota_primeiro_semestre,
                           nota_segundo_semestre=nota_segundo_semestre, media_final=media_final)
        db.session.add(novo_aluno)
        db.session.commit()
        return redirect(url_for('alunos.listar_alunos'))
    turmas = Turma.query.all()
    return render_template('adicionar_aluno.html', turmas=turmas)

@aluno_blueprint.route('/deletar/<int:id>', methods=['POST'])
def deletar_aluno(id):
    aluno = Aluno.query.get(id)
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for('alunos.listar_alunos'))
