from bottle import route, run, template, request, redirect
from app.controllers.application import render
from datetime import date
import random

mensagens = [
    {"id": 1, "texto": "Acredite em si mesmo!", "categoria": "motivacional", "favorita": True, "data_agendada": "2025-06-27"},
    {"id": 2, "texto": "Tudo tem seu tempo certo.", "categoria": "reflexiva", "favorita": False, "data_agendada": ""},
    {"id": 3, "texto": "Confie em Deus e siga!", "categoria": "espiritual", "favorita": True, "data_agendada": ""}
]

def buscar_mensagem(id):
    return next((m for m in mensagens if m["id"] == id), None)

@route("/")
@route("/mensagens")
def mensagens_index():
    q = request.query.q or ""
    categoria = request.query.categoria or ""
    filtradas = [m for m in mensagens if q.lower() in m["texto"].lower()]
    if categoria:
        filtradas = [m for m in filtradas if m["categoria"] == categoria]
    return render("mensagens", mensagens=filtradas, total=len(filtradas), q=q, categoria=categoria)

@route("/nova", method=["GET", "POST"])
def nova():
    if request.method == "POST":
        texto = request.forms.get("texto")
        categoria = request.forms.get("categoria")
        favorita = True if request.forms.get("favorita") else False
        data_agendada = request.forms.get("data_agendada") or ""
        novo_id = max([m["id"] for m in mensagens], default=0) + 1
        mensagens.append({"id": novo_id, "texto": texto, "categoria": categoria, "favorita": favorita, "data_agendada": data_agendada})
        redirect("/mensagens")
    return render("nova")

@route("/ver/<id:int>")
def ver(id):
    m = buscar_mensagem(id)
    return render("ver", m=m)

@route("/editar/<id:int>", method=["GET", "POST"])
def editar(id):
    m = buscar_mensagem(id)
    if request.method == "POST":
        m["texto"] = request.forms.get("texto")
        m["categoria"] = request.forms.get("categoria")
        m["favorita"] = True if request.forms.get("favorita") else False
        m["data_agendada"] = request.forms.get("data_agendada") or ""
        redirect("/mensagens")
    return render("editar", m=m)

@route("/deletar/<id:int>")
def deletar(id):
    global mensagens
    mensagens = [m for m in mensagens if m["id"] != id]
    redirect("/mensagens")

@route("/favoritas")
def favoritas():
    favoritas = [m for m in mensagens if m["favorita"]]
    return render("favoritas", mensagens=favoritas)

@route("/hoje")
def hoje():
    hoje_str = str(date.today())
    m = next((m for m in mensagens if m["data_agendada"] == hoje_str), None)
    return render("hoje", m=m)

@route("/aleatoria")
def aleatoria():
    if mensagens:
        m = random.choice(mensagens)
    else:
        m = None
    return render("aleatoria", m=m)

run(debug=True, host="localhost", port=8080)
