# Usa o Bottle para rodar um servidor HTTP em localhost:8082 para o Python
# Exibe 'Hello' + nome salvo na collections 'db.names'

from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
