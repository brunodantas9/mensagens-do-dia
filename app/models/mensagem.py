
class Mensagem:
    def __init__(self, id, texto, categoria, favorita=False, data_agendada=None, criado_em=None):
        self.id = id
        self.texto = texto
        self.categoria = categoria
        self.favorita = favorita
        self.data_agendada = data_agendada
        self.criado_em = criado_em
