from bot.exceptions.validacao_error import ValidacaoError

class InscricaoExpiradaError(ValidacaoError):
    def __init__(self, mensagem_origem):
        self.mensagem_origem = mensagem_origem
        super().__init__(
            "Inscrições encerradas",
            "Não juntou 10 jogadores a tempo. Use o comando novamente para tentar de novo.",
        )
