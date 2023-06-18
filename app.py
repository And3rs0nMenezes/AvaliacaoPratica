from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista inicial de alunos
alunos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listar-alunos')
def listar_alunos():
    return render_template('listar_alunos.html', alunos=alunos)

@app.route('/adicionar-aluno', methods=['GET', 'POST'])
def adicionar_aluno():
    if request.method == 'POST':
        matricula = request.form['matricula']
        NomeAluno = request.form['NomeAluno']

        aluno = {
                'NomeAluno': NomeAluno,
                'matricula': matricula
        }
        alunos.append(aluno)

        return redirect(url_for('listar_alunos'))
    return render_template('adicionar_alunos.html')

@app.route('/editar-alunos/<int:id>', methods=['GET', 'POST'])
def editar_aluno(id):
    aluno = alunos[id]

    if request.method == 'POST':
        aluno['NomeAluno'] = request.form['NomeAluno']
        aluno['matricula'] = request.form['matricula']

        return redirect(url_for('listar_alunos'))
    return render_template('editar_alunos.html', id=id, aluno=aluno)

@app.route('/excluir-aluno/<int:id>', methods=['POST'])
def excluir_aluno(id):
    del alunos[id]
    return redirect(url_for('listar_alunos'))

if __name__ == '__main__':
    app.run(debug=True)
