from bottle import Bottle, static_file, run, template, request, redirect
from app.controllers.application import render
from app.data.mensagens import carregar_mensagens, salvar_mensagens
import os

app = Bottle()

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='app/static')

@app.route('/mensagens')
def mensagens_index():
    mensagens = carregar_mensagens()
    q = request.query.q.strip() if request.query.q else ''
    categoria = request.query.categoria.strip() if request.query.categoria else ''
    filtradas = [
        m for m in mensagens
        if (q.lower() in m.texto.lower() if q else True)
        and (m.categoria == categoria if categoria else True)
    ]
    return render("mensagens", mensagens=filtradas, total=len(filtradas), q=q, categoria=categoria)

if __name__ == "__main__":
    run(app, host='localhost', port=8080, debug=True, reloader=True)

