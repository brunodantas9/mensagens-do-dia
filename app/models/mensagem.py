import json
from datetime import datetime
from pathlib import Path

ARQUIVO = Path(__file__).parent.parent / 'data' / 'mensagens.json'

class Mensagem:
    def __init__(self, id, texto, categoria, data=None, favorita=False):
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

    @classmethod
    def ler_arquivo(cls):
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
            json.dump([m.para_dict() for m in mensagens], f, ensure_ascii=False, indent=2)

    @classmethod
    def listar(cls):
        return cls.ler_arquivo()

    @classmethod
    def buscar(cls, id):
        mensagens = cls.ler_arquivo()
        for m in mensagens:
            if m.id == id:
                return m
        return None

    @classmethod
    def adicionar(cls, texto, categoria):
        mensagens = cls.ler_arquivo()
        novo_id = 1 if not mensagens else max(m.id for m in mensagens) + 1
        nova = Mensagem(novo_id, texto, categoria)
        mensagens.append(nova)
        cls.salvar_arquivo(mensagens)

    @classmethod
    def editar(cls, id, texto, categoria):
        mensagens = cls.ler_arquivo()
        for m in mensagens:
            if m.id == id:
                m.texto = texto
                m.categoria = categoria
                break
        cls.salvar_arquivo(mensagens)

    @classmethod
    def deletar(cls, id):
        mensagens = cls.ler_arquivo()
        mensagens = [m for m in mensagens if m.id != id]
        cls.salvar_arquivo(mensagens)

    @classmethod
    def marcar_como_favorita(cls, id):
        mensagens = cls.ler_arquivo()
        for m in mensagens:
            if m.id == id:
                m.favorita = not m.favorita
                break
        cls.salvar_arquivo(mensagens)

    @classmethod
    def favoritas(cls):
        return [m for m in cls.ler_arquivo() if m.favorita]

    @classmethod
    def aleatoria(cls):
        import random
        mensagens = cls.ler_arquivo()
        return random.choice(mensagens) if mensagens else None

    @classmethod
    def do_dia(cls):
        hoje = datetime.now().strftime('%Y-%m-%d')
        mensagens = [m for m in cls.ler_arquivo() if m.data == hoje]
        return mensagens[0] if mensagens else None


