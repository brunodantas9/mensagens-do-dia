from bottle import route, run, template, request, redirect
from app.models.mensagem import Mensagem
from app.controllers.application import render

@route('/')
@route('/mensagens')
def mensagens_index():
    q = request.query.q or ""
    categoria = request.query.categoria or ""

    mensagens = Mensagem.listar()
    filtradas = [
        m for m in mensagens if
        (q.lower() in m.texto.lower()) and
        (m.categoria == categoria or not categoria)
    ]
    return render("mensagens", mensagens=filtradas, total=len(filtradas), q=q, categoria=categoria)

@route('/nova')
def nova_mensagem_form():
    return render("nova")

@route('/nova', method='POST')
def nova_mensagem_submit():
    texto = request.forms.get('texto')
    categoria = request.forms.get('categoria')
    favorita = True if request.forms.get('favorita') else False

    nova = Mensagem(texto=texto, categoria=categoria, favorita=favorita)
    nova.salvar()
    redirect('/mensagens')

@route('/ver/<id:int>')
def ver_mensagem(id):
    m = Mensagem.buscar(id)
    if m:
        return render("ver", m=m)
    redirect('/mensagens')

@route('/editar/<id:int>')
def editar_mensagem_form(id):
    m = Mensagem.buscar(id)
    if m:
        return render("editar", m=m)
    redirect('/mensagens')

@route('/editar/<id:int>', method='POST')
def editar_mensagem_submit(id):
    texto = request.forms.get('texto')
    categoria = request.forms.get('categoria')
    favorita = True if request.forms.get('favorita') else False

    Mensagem.atualizar(id, texto, categoria, favorita)
    redirect('/mensagens')

@route('/deletar/<id:int>')
def deletar_mensagem(id):
    Mensagem.deletar(id)
    redirect('/mensagens')

@route('/favoritas')
def favoritas():
    mensagens = Mensagem.listar()
    favoritas = [m for m in mensagens if m.favorita]
    return render("favoritas", mensagens=favoritas)

@route('/aleatoria')
def aleatoria():
    m = Mensagem.aleatoria()
    if m:
        return render("aleatoria", m=m)
    redirect('/mensagens')

@route('/hoje')
def hoje():
    m = Mensagem.mensagem_do_dia()
    if m:
        return render("hoje", m=m)
    redirect('/mensagens')


