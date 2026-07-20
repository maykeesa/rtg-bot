from bot.exceptions.validacao_error import ValidacaoError

class JogadoresExcedentesError(ValidacaoError):
    def __init__(self, maximo, informados):
        self.maximo = maximo
        self.informados = informados
        super().__init__(
            "Jogadores em excesso",
            f"São permitidos no máximo {maximo} jogadores únicos, separados por vírgula. Você informou {informados}.",
        )
