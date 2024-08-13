from unidecode import unidecode
import random

def rodar_quiz():

    perguntas = [
        {'pergunta': 'Qual time tem o escudo mais bonito do mundo?', 'resposta': 'Botafogo'},
        {'pergunta': 'Qual o maior planeta do sistema solar?', 'resposta': 'Júpiter'},
        {'pergunta': 'Quantos continentes existem no mundo?', 'resposta': '7'},
        {'pergunta': 'Quem pintou a Mona Lisa?', 'resposta': 'Leonardo da Vinci'},
        {'pergunta': 'Qual o elemento químico representado pelo símbolo "O"?', 'resposta': 'Oxigênio'},
        {'pergunta': 'Qual é o menor país do mundo?', 'resposta': 'Vaticano'},
        {'pergunta': 'Em que ano começou a Segunda Guerra Mundial?', 'resposta': '1939'},
        {'pergunta': 'Qual é o maior oceano da Terra?', 'resposta': 'Oceano Pacífico'},
        {'pergunta': 'Quantos graus tem um ângulo reto?', 'resposta': '90'},
        {'pergunta': 'Qual é o país mais populoso do mundo?', 'resposta': 'China'},
        {'pergunta': 'Qual a capital da França?', 'resposta': 'Paris'},
        {'pergunta': 'Quem foi o primeiro homem a pisar na Lua?', 'resposta': 'Neil Armstrong'},
        {'pergunta': 'Quem é o autor de "Dom Quixote"?', 'resposta': 'Miguel de Cervantes'},
        {'pergunta': 'Qual a fórmula química da água?', 'resposta': 'H2O'},
        {'pergunta': 'Em que continente está localizado o Egito?', 'resposta': 'África'},
        {'pergunta': 'Quem escreveu "Romeu e Julieta"?', 'resposta': 'William Shakespeare'},
        {'pergunta': 'Quantos anos tem um milênio?', 'resposta': '1000'},
        {'pergunta': 'Qual é o animal terrestre mais rápido do mundo?', 'resposta': 'Guepardo'},
        {'pergunta': 'Qual é o rio mais longo do mundo?', 'resposta': 'Rio Nilo'},
        {'pergunta': 'Quem descobriu o Brasil?', 'resposta': 'Pedro Álvares Cabral'},
        {'pergunta': 'Em que ano foi proclamada a independência do Brasil?', 'resposta': '1822'},
        {'pergunta': 'Qual é o planeta mais próximo do Sol?', 'resposta': 'Mercúrio'},
        {'pergunta': 'Qual a capital da Espanha?', 'resposta': 'Madri'},
        {'pergunta': 'Qual é a montanha mais alta do mundo?', 'resposta': 'Monte Everest'},
        {'pergunta': 'Qual o nome do cientista que formulou a teoria da relatividade?', 'resposta': 'Albert Einstein'},
        {'pergunta': 'Qual é o país com a maior extensão territorial do mundo?', 'resposta': 'Rússia'},
        {'pergunta': 'Qual o nome do autor de "O Pequeno Príncipe"?', 'resposta': 'Antoine de Saint-Exupéry'},
        {'pergunta': 'Qual é a moeda oficial do Japão?', 'resposta': 'Iene'},
        {'pergunta': 'Quem pintou o teto da Capela Sistina?', 'resposta': 'Michelangelo'},
        {'pergunta': 'Qual é a maior floresta tropical do mundo?', 'resposta': 'Floresta Amazônica'},
        {'pergunta': 'Quem inventou a lâmpada elétrica?', 'resposta': 'Thomas Edison'},
        {'pergunta': 'Qual é o país de origem do samba?', 'resposta': 'Brasil'},
        {'pergunta': 'Quem foi o primeiro presidente do Brasil?', 'resposta': 'Deodoro da Fonseca'},
        {'pergunta': 'Qual é o símbolo químico do ouro?', 'resposta': 'Au'},
        {'pergunta': 'Quantos lados tem um hexágono?', 'resposta': '6'},
        {'pergunta': 'Qual é o nome do famoso físico britânico que estudou buracos negros?', 'resposta': 'Stephen Hawking'},
        {'pergunta': 'Qual é a capital do Canadá?', 'resposta': 'Ottawa'},
        {'pergunta': 'Qual é o nome do maior deserto do mundo?', 'resposta': 'Saara'},
        {'pergunta': 'Quem escreveu a série de livros "Harry Potter"?', 'resposta': 'J.K. Rowling'},
        {'pergunta': 'Em que ano ocorreu a queda do Muro de Berlim?', 'resposta': '1989'},
        {'pergunta': 'Qual é a capital da Austrália?', 'resposta': 'Camberra'},
        {'pergunta': 'Qual é o maior país da América do Sul?', 'resposta': 'Brasil'},
        {'pergunta': 'Quem foi o autor de "A Divina Comédia"?', 'resposta': 'Dante Alighieri'},
        {'pergunta': 'Qual é o nome do processo de conversão de vapor de água em água líquida?', 'resposta': 'Condensação'},
        {'pergunta': 'Em que país está localizada a Grande Muralha?', 'resposta': 'China'},
        {'pergunta': 'Qual é o nome do planeta conhecido como o "Planeta Vermelho"?', 'resposta': 'Marte'},
        {'pergunta': 'Quem pintou "A Última Ceia"?', 'resposta': 'Leonardo da Vinci'},
        {'pergunta': 'Qual é o nome do escritor de "O Senhor dos Anéis"?', 'resposta': 'J.R.R. Tolkien'},
        {'pergunta': 'Qual é o órgão responsável por filtrar o sangue no corpo humano?', 'resposta': 'Rim'},
        {'pergunta': 'Qual é o nome da rainha britânica que reinou por mais tempo?', 'resposta': 'Rainha Elizabeth II'},
        {'pergunta': 'Qual é a linguagem de programação mais utilizada atualmente?', 'resposta': 'Python'},
        {'pergunta': 'Quem é conhecido como o "Rei do Rock"?', 'resposta': 'Elvis Presley'},
        {'pergunta': 'Qual é o nome do maior osso do corpo humano?', 'resposta': 'Fêmur'},
        {'pergunta': 'Quem foi o líder do movimento dos direitos civis nos Estados Unidos?', 'resposta': 'Martin Luther King Jr.'},
        {'pergunta': 'Qual é a capital da Itália?', 'resposta': 'Roma'},
        {'pergunta': 'Quem pintou "A Noite Estrelada"?', 'resposta': 'Vincent van Gogh'},
        {'pergunta': 'Qual é o planeta mais quente do sistema solar?', 'resposta': 'Vênus'},
        {'pergunta': 'Quem escreveu "1984"?', 'resposta': 'George Orwell'},
        {'pergunta': 'Qual é o idioma mais falado no mundo?', 'resposta': 'Chinês mandarim'},
        {'pergunta': 'Qual é o símbolo químico do ferro?', 'resposta': 'Fe'},
        {'pergunta': 'Em que ano a primeira Guerra Mundial começou?', 'resposta': '1914'},
        {'pergunta': 'Quem é conhecido como o "Pai da Medicina"?', 'resposta': 'Hipócrates'},
        {'pergunta': 'Qual é o nome do maior animal terrestre?', 'resposta': 'Elefante africano'},
        {'pergunta': 'Qual é o nome do famoso explorador que descobriu a América?', 'resposta': 'Cristóvão Colombo'},
        {'pergunta': 'Qual é o maior continente do mundo?', 'resposta': 'Ásia'},
        {'pergunta': 'Em que ano foi inventado o telefone?', 'resposta': '1876'},
        {'pergunta': 'Qual é a capital da Alemanha?', 'resposta': 'Berlim'},
        {'pergunta': 'Quem pintou "Guernica"?', 'resposta': 'Pablo Picasso'},
        {'pergunta': 'Qual é o nome do cientista que descobriu a penicilina?', 'resposta': 'Alexander Fleming'},
        {'pergunta': 'Qual é a moeda oficial da Rússia?', 'resposta': 'Rublo'},
        {'pergunta': 'Em que país está localizada a Torre Eiffel?', 'resposta': 'França'},
        {'pergunta': 'Qual é o nome do processo de conversão de água em gelo?', 'resposta': 'Solidificação'},
        {'pergunta': 'Qual é o maior estado do Brasil em população?', 'resposta': 'São Paulo'},
        {'pergunta': 'Quem é o autor de "O Morro dos Ventos Uivantes"?', 'resposta': 'Emily Brontë'},
        {'pergunta': 'Qual é a principal fonte de energia do nosso planeta?', 'resposta': 'Sol'},
        {'pergunta': 'Qual é a maior cidade do mundo em população?', 'resposta': 'Tóquio'},
        {'pergunta': 'Quem é conhecido como o "Rei do Pop"?', 'resposta': 'Michael Jackson'},
        {'pergunta': 'Qual é o nome do famoso físico que formulou as leis do movimento?', 'resposta': 'Isaac Newton'},
        {'pergunta': 'Qual é a capital do Brasil?', 'resposta': 'Brasília'},
        {'pergunta': 'Quem escreveu "A Odisséia"?', 'resposta': 'Homero'},
        {'pergunta': 'Qual é o maior país da América do Norte?', 'resposta': 'Canadá'},
        {'pergunta': 'Qual é a língua oficial do Egito?', 'resposta': 'Árabe'},
        {'pergunta': 'Quem foi o primeiro presidente dos Estados Unidos?', 'resposta': 'George Washington'},
        {'pergunta': 'Qual é a unidade básica de medida de massa no sistema internacional?', 'resposta': 'Quilograma'},
        {'pergunta': 'Quem pintou "A Criação de Adão"?', 'resposta': 'Michelangelo'},
        {'pergunta': 'Qual é o nome do processo de conversão de água líquida em vapor?', 'resposta': 'Evaporação'},
        {'pergunta': 'Qual é o maior estado do Brasil em área?', 'resposta': 'Amazonas'},
        {'pergunta': 'Em que ano foi fundado o Facebook?', 'resposta': '2004'},
        {'pergunta': 'Quem é conhecido como o "Pai da Computação"?', 'resposta': 'Alan Turing'},
        {'pergunta': 'Qual é a capital do México?', 'resposta': 'Cidade do México'},
        {'pergunta': 'Quem escreveu "O Conde de Monte Cristo"?', 'resposta': 'Alexandre Dumas'},
        {'pergunta': 'Qual é o nome do maior rio do mundo?', 'resposta': 'Rio Amazonas'},
        {'pergunta': 'Em que ano ocorreu a Revolução Francesa?', 'resposta': '1789'},
        {'pergunta': 'Qual é o nome da primeira mulher a ganhar um Prêmio Nobel?', 'resposta': 'Marie Curie'},
        {'pergunta': 'Qual é o nome do maior lago do mundo?', 'resposta': 'Lago Cáspio'},
        {'pergunta': 'Em que país está localizada a Torre de Pisa?', 'resposta': 'Itália'},
        {'pergunta': 'Qual é a capital da Índia?', 'resposta': 'Nova Deli'},
        {'pergunta': 'Qual é o nome do processo de conversão de gelo em água líquida?', 'resposta': 'Fusão'},
        {'pergunta': 'Qual é o nome do maior vulcão ativo do mundo?', 'resposta': 'Mauna Loa'},
        {'pergunta': 'Em que ano foi criada a Organização das Nações Unidas?', 'resposta': '1945'},
        {'pergunta': 'Qual é o significado da sigla do jogo GTA?', 'resposta': 'Grand Theft Auto'},
        {'pergunta': 'Qual time tem o maior número de títulos da UEFA Champions League?', 'resposta': 'Real Madrid'}
    ]
     
    random.shuffle(perguntas)

    print('==#' * 30)
    print('Bem vindo ao Veio porque Quiz! Responda as perguntas corretamente para ganhar pontos.')
    print('==#' * 30)

    pontuacao = 0

    while perguntas:
        perg_atual = perguntas.pop(0)
        pergunta = perg_atual['pergunta']
        resp_correta = perg_atual['resposta']

        resp_usuario = input(pergunta + ' ')

        if unidecode(resp_usuario.upper()) == unidecode(resp_correta.upper()):
            print('Resposta CORRETA!\n')
            pontuacao += 1
        else:
            print(f'Resposta ERRADA. O correto é: {resp_correta}\n')
            print('FIM DE JOGO!')
            break

    print(f'Você acertou {pontuacao} de {len(perguntas)} perguntas!')

rodar_quiz()