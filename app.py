from flask import Flask

app = Flask(__name__)

# Definir um rota raiz (pagina inicial) e a função que será executada ao requisitar
@app.route('/')
def hello_world():
    return 'Hello World'


app.run(debug=True)