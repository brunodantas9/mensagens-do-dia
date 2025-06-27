from bottle import Bottle, run, request, redirect
from app.controllers.application import Application
from app.data.mensagens import *
from datetime import date
from bottle import route, run, template, request, redirect


app = Bottle()
ctl = Application()


@app.route("/static/<filepath:path>")
def static(filepath):
    return bottle.static_file(filepath, root="./app/static")


@app.route("/")
@app.route("/mensagens")
def mensagens():
    q = request.query.get("q", "")
    categoria = request.query.get("categoria", "")
    filtradas = mensagem.filtrar(q, categoria)
    return ctl.render("mensagens", mensagens=filtradas, total=len(filtradas), q=q, categoria=categoria)


@app.route("/nova", method=["GET", "POST"])
def nova():
    if request.method == "POST":
        texto = request.forms["texto"]
        categoria = request.forms["categoria"]
        favorita = "favorita" in request.forms
        data_agendada = request.forms.get("data_agendada") or None
        if data_agendada:
            data_agendada = date.fromisoformat(data_agendada)
        adicionar(texto, categoria, favorita, data_agendada)
        return redirect("/mensagens")
    return ctl.render("nova")


@app.route("/ver/<id:int>")
def ver(id):
    m = buscar_por_id(id)
    return ctl.render("ver", m=m)


@app.route("/editar/<id:int>", method=["GET", "POST"])
def editar(id):
    m = buscar_por_id(id)
    if request.method == "POST":
        texto = request.forms["texto"]
        categoria = request.forms["categoria"]
        favorita = "favorita" in request.forms
        data_agendada = request.forms.get("data_agendada") or None
        if data_agendada:
            data_agendada = date.fromisoformat(data_agendada)
        atualizar(id, texto, categoria, favorita, data_agendada)
        return redirect("/mensagens")
    return ctl.render("editar", m=m)


@app.route("/deletar/<id:int>")
def deletar_mensagem(id):
    deletar(id)
    return redirect("/mensagens")


@app.route("/favoritas")
def favoritas():
    favoritas = [m for m in listar() if m.favorita]
    return ctl.render("favoritas", mensagens=favoritas)


@app.route("/aleatoria")
def aleatoria():
    import random
    todas = listar()
    m = random.choice(todas) if todas else None
    return ctl.render("aleatoria", m=m)


@app.route("/hoje")
def hoje():
    hoje = date.today()
    agendadas = [m for m in listar() if m.data_agendada == hoje]
    m = agendadas[0] if agendadas else None
    return ctl.render("hoje", m=m)


if __name__ == "__main__":
    run(app, host="localhost", port=8080, debug=True)
