from random import choice

jokes = [
"Bot viciado só cai eu de sup",
"Já reclamaram do sorteio hoje?",
"Gostaria de abençoar todos e dizer que a gente é um time, não uma família",
"Vai deixar seu irmão morrer? vou",
"Hoje o RNG tá do seu lado ou não?",
"Sempre tem alguém reclamando da lane, sempre",
"Perdeu a lane? Só counter-picka na próxima",
"Jungle que não gankeia é só um bot de menu",
"First blood é sempre culpa do sup",
"Se o time tá ruim, é o sorteio. Se o time tá bom, é talento",
"GG ez só se ganhar",
"Voice chat: onde amizades morrem mais rápido que o nexus",
"Surrender aos 20 é só carinho",
"Se flamar não builda dano, pelo menos builda ódio",
"Sorteio não escolhe covarde, escolhe quem vai de off role",
"Reportar não bane, mas alivia"
]

def choice_joke():
    choiced = choice(jokes)

    return choiced

