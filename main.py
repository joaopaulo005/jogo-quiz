from unidecode import unidecode

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
    ]
     
    pontuacao = 0

    for item in perguntas:
        print(item['pergunta'])
        resposta_player = input('Sua resposta: ')

        if unidecode(resposta_player.upper()) == unidecode(item['resposta'].upper()):
            print('Resposta Correta!\n')
            pontuacao += 1
        else:
            print(f'Resposta errada. O correto é: {item["resposta"]}\n')

    print(f'Você acertou {pontuacao} de {len(perguntas)} perguntas!')

rodar_quiz()