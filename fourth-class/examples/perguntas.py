perguntas= {
        'pergunta 1' : { 'pergunta': 'Quanto é 2+2',
            'respostas': {'a':'1', 'b':'2', 'c':'3','d':'4'},
            'resposta_certa': 'd'
    },
        'pergunta 2' : { 
                'pergunta': 'Quanto é 2*3',
                'respostas': {'a':'6', 'b':'2', 'c':'3','d':'4'},
                'resposta_certa': 'a'
        },
        'pergunta 3' : { 
                'pergunta': 'Quanto é 8/4',
                'respostas': {'a':'1', 'b':'2', 'c':'3','d':'4'},
                'resposta_certa': 'b'
        },
        'pergunta 4' : { 
                'pergunta': 'Quanto é 8-6',
                'respostas': {'a':'1', 'b':'3', 'c':'2','d':'4'},
                'resposta_certa': 'c'
        }
}
print()
respostas_certas=0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print()
          
    print('respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    resposta_usuario = input('Sua resposta:')
    print()
    
    if resposta_usuario == pv['resposta_certa']:
        print ('Você acertou!!!')
        respostas_certas += 1
    else:
        print ('Você errou!')
    print()

    qtd_perguntas= len(perguntas)
    porcentagem_acerto = respostas_certas/qtd_perguntas *100

print(f'Você acertou {respostas_certas} respostas !')
