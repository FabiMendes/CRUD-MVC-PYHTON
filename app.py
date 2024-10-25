from flask import Flask
from models import db
from controllers.aluno_controller import aluno_blueprint
from controllers.turma_controller import turma_blueprint
from controllers.professor_controller import professor_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///escola.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados
db.init_app(app)

# Registrar os blueprints
app.register_blueprint(aluno_blueprint, url_prefix='/alunos')
app.register_blueprint(turma_blueprint, url_prefix='/turmas')
app.register_blueprint(professor_blueprint, url_prefix='/professores')

# Criar as tabelas do banco de dados
with app.app_context():
    db.create_all()

@app.route('index.html')
def index():
    return "Bem-vindo ao sistema escolar!"

if __name__ == '__main__':
    app.run(debug=True)
