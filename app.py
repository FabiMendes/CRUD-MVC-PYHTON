from flask import Flask, render_template
from models import db
from controllers.aluno_controller import aluno_blueprint
from controllers.professor_controller import professor_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///escola.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Registrar Blueprints (rotas)
app.register_blueprint(aluno_blueprint, url_prefix='/alunos')
app.register_blueprint(professor_blueprint, url_prefix='/professores')

# Criar tabelas ao iniciar o app
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    print("Acessou a rota principal")  # Adicione esta linha
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
