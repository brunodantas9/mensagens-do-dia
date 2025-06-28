import json
import random
from datetime import datetime
from pathlib import Path
from datetime import date


ARQUIVO = Path(__file__).parent.parent / 'data' / 'mensagens.json'


class Mensagem:
    def __init__(self, id, texto, categoria, favorita=False, data_agendada=None, criado_em=None):
        self.id = id
        self.texto = texto
        self.categoria = categoria
        self.data = data or datetime.now().strftime('%Y-%m-%d')
        self.favorita = favorita

    def para_dict(self):
        return {
            "id": self.id,
            "texto": self.texto,
            "categoria": self.categoria,
            "data": self.data,
            "favorita": self.favorita
        }

    def salvar(self):
        mensagens = Mensagem.listar()
        mensagens.append(self)
        Mensagem.salvar_arquivo(mensagens)

    @classmethod
    def listar(cls):
        if not ARQUIVO.exists():
            return []
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            try:
                dados = json.load(f)
                return [Mensagem(**m) for m in dados]
            except json.JSONDecodeError:
                return []

    @classmethod
    def salvar_arquivo(cls, mensagens):
        with open(ARQUIVO, 'w', encoding='utf-8') as f:
            json.dump([m.para_dict() for m in mensagens],
                      f, ensure_ascii=False, indent=2)

    @classmethod
    def buscar(cls, id):
        for m in cls.listar():
            if m.id == id:
                return m
        return None

    @classmethod
    def atualizar(cls, id, texto, categoria, favorita):
        mensagens = cls.listar()
        for m in mensagens:
            if m.id == id:
                m.texto = texto
                m.categoria = categoria
                m.favorita = favorita
        cls.salvar_arquivo(mensagens)

    @classmethod
    def deletar(cls, id):
        mensagens = [m for m in cls.listar() if m.id != id]
        cls.salvar_arquivo(mensagens)

    @classmethod
    def aleatoria(cls):
        mensagens = cls.listar()
        return random.choice(mensagens) if mensagens else None

    @classmethod
    def mensagem_do_dia(cls):
        hoje = datetime.now().strftime('%Y-%m-%d')
        for m in cls.listar():
            if m.data == hoje:
                return m
        return None
