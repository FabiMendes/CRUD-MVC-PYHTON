from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Professor

professor_blueprint = Blueprint('professores', __name__)

@professor_blueprint.route('/')
def listar_professores():
    professores = Professor.query.all()
    return render_template('professores.html', professores=professores)

@professor_blueprint.route('/adicionar', methods=['GET', 'POST'])
def adicionar_professor():
    if request.method == 'POST':
        nome = request.form['nome']
        disciplina = request.form['disciplina']
        novo_professor = Professor(nome=nome, disciplina=disciplina)
        db.session.add(novo_professor)
        db.session.commit()
        return redirect(url_for('professores.listar_professores'))
    return render_template('professor_view.html')

@professor_blueprint.route('/deletar/<int:id>')
def deletar_professor(id):
    professor = Professor.query.get(id)
    db.session.delete(professor)
    db.session.commit()
    return redirect(url_for('professores.listar_professores'))
