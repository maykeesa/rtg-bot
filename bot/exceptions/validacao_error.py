class ValidacaoError(Exception):
    mensagem_origem = None

    def __init__(self, titulo, mensagem):
        self.titulo = titulo
        super().__init__(mensagem)
