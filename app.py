from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    inversor = request.form.get('inversor')
    modulo_fv = request.form.get('modulo_fv')
    quantidade = request.form.get('quantidade')
    cidade = request.form.get('cidade')

    return f"""
    <h1>Dados Recebidos</h1>
    <p><strong>Inversor:</strong> {inversor}</p>
    <p><strong>Módulo FV:</strong> {modulo_fv}</p>
    <p><strong>Quantidade:</strong> {quantidade}</p>
    <p><strong>UF:</strong> {cidade}</p>
    <p><strong>Cidade:</strong> {cidade}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
