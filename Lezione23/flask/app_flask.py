from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/info')
def info():
    return{
        'app':'Libreria API',
        'versione':'1.0'
    }

@app.route('/libri/<int:libro_id>')
def get_libro(libro_id):
    return {
        'id':libro_id,
        'title':f'Libro {libro_id}'
}

#
@app.route('/ricerca')
def ricerca():
    termine = request.args.get('q', '')
    return {
        'query': termine,
        'risultati':[]
    }

@app.route('/libri', methods= ['GET','POST'])
def gestisci_libri():
    if request.method == 'GET':
        return {'libri':[]}
    
    elif request.method == 'POST':
        return
