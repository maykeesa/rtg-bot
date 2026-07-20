class ValidacaoError(Exception):
    def __init__(self, titulo, mensagem):
        self.titulo = titulo
        super().__init__(mensagem)
