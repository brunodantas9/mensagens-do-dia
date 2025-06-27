
from app.models.mensagem import Mensagem
from datetime import date, datetime

mensagens = []
id_counter = 1

def adicionar(texto, categoria, favorita=False, data_agendada=None):
    global id_counter
    criado_em = datetime.now()
    msg = Mensagem(id_counter, texto, categoria, favorita, data_agendada, criado_em)
    mensagens.append(msg)
    id_counter += 1

def listar():
    return mensagens

def buscar_por_id(id):
    for m in mensagens:
        if m.id == id:
            return m
    return None

def deletar(id):
    global mensagens
    mensagens = [m for m in mensagens if m.id != id]

def atualizar(id, texto, categoria, favorita=False, data_agendada=None):
    m = buscar_por_id(id)
    if m:
        m.texto = texto
        m.categoria = categoria
        m.favorita = favorita
        m.data_agendada = data_agendada

# Mensagens iniciais
adicionar("Você é mais forte do que imagina.", "motivação", favorita=True)
adicionar("Respire fundo. Vai ficar tudo bem.", "calma")
adicionar("Cada passo conta, continue avançando.", "superação")
adicionar("Você consegue! Basta acreditar.", "motivação", favorita=True)
adicionar("Permita-se recomeçar quantas vezes forem necessárias.", "superação")
