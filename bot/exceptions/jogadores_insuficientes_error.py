from bot.exceptions.validacao_error import ValidacaoError

class JogadoresInsuficientesError(ValidacaoError):
    def __init__(self, minimo, informados):
        self.minimo = minimo
        self.informados = informados
        super().__init__(
            "Jogadores insuficientes",
            f"São necessários {minimo} jogadores únicos, separados por vírgula. Você informou apenas {informados}.",
        )
