import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import requests

audio = sr.Recognizer()
maquina = pyttsx3.init()
##API_KEY = "20ffd144fd1b6b8a3cfbd9d58787b4fd"



def executa_comando():
    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'Paula' in comando:
                comando = comando.replace('Paula', '')
                maquina.say(comando)
                maquina.runAndWait()
                
    except:
        print('Microfone não está funcionando')
    
    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace ('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque','')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando musica')
        maquina.runAndWait()
    elif 'criou' in comando:
        criacao = 'Ana Paula Rodrigues'
        maquina.say('Minha criadora é a:' + criacao)
        maquina.runAndWait()
    elif 'lorena' in comando:
        estagiaria = 'estagiaria do programa 4.0'
        maquina.say('Ela é' + estagiaria)
        maquina.runAndWait()
    elif 'prefeita' in comando:
        prefeita = 'Maria Edna de Andrade'
        maquina.say('A prefeita do municipio de Prado Ferreira é a: ' + prefeita)
        maquina.runAndWait()
    elif 'nasceu' in comando:
        nasc = '2022'
        cidade = 'Prado Ferreira'
        maquina.say('Eu nasci no ano de {}, na cidade de {} : ' .format(nasc, cidade))
        maquina.runAndWait()
    elif 'namora' in comando:
        relacionamento = 'solteiro'
        maquina.say('Eu estou {} no momento, fui projetado para estudar'.format(relacionamento))
        maquina.runAndWait()
    elif 'anos' in comando:
        idade = '1 ano'
        maquina.say('Eu fui criado recentemente, tenho {} de idade ' .format(idade))
        maquina.runAndWait()
    elif 'mora' in comando:
        lugar = 'Prado Ferreira'
        endereco = 'Rua Jadir de Caires 445'
        maquina.say('Eu moro em {} na {} ' .format(lugar, endereco))
        maquina.runAndWait()
    elif 'mariana' in comando:
        assistente = 'trabalha no Departamento de Assistência Social'
        maquina.say('A Mariana' + assistente)
        maquina.runAndWait()
    elif 'magna' in comando:
        funcionaria = 'trabalha no departamento de Convênios da Prefeitura'
        maquina.say('A Magna ' + funcionaria)
        maquina.runAndWait()
    elif 'shirley' in comando:
        func1 = 'trabalha na biblioteca e la no esporte'
        maquina.say('Ela ' + func1)
        maquina.runAndWait()
    elif 'time' in comando:
        time = 'Palmeiras'
        maquina.say('Eu torço para o {} '.format(time))
        maquina.runAndWait()
    elif 'mundial' in comando:
        titulo = 'o Palmeiras mesmo assim é o melhor'
        maquina.say('Ainda pelo meu conceito técnico ' + titulo)
        maquina.runAndWait()
    elif 'cor' in comando:
        color = 'azul'
        maquina.say('Eu gosto muito da cor ' + color)
        maquina.runAndWait()    
    elif 'programa' in comando:
        mensagem = """
        A Equipe do Programa Profissão 4.0 está composta pela 
        nossa Assistente Social Mariana Fernandes,
        Pela Magna Regina Gonzales de Moura, chefe do Departamento de Convenios
        Pela Diretora do Departamento de Tecnologia e Informação, Ana Paula Rodrigues
        Pela Prefeita Maria Edna de Andrade.
        Temos também o nosso presidente do Conselho o Senhor Silvio Antonio Damaceno 
        e não podemos deixar de citar do nosso amigo irmão Alex Canziani que nos apoia em tudo!
        Ah e sejam todas bem vindas!"""
        maquina.say(mensagem)
        maquina.runAndWait()   
    elif 'windows' in comando:
        sistema1 = """
        Quem criou o Windows foi o Bill Gueites
        """
        maquina.say(sistema1)
        maquina.runAndWait()
    elif 'mac' in comando:
        sistema2 = """
        Quem criou o Mec foi o Stive Jobs
        """
        maquina.say(sistema2)
        maquina.runAndWait()
    elif 'linux' in comando:
        sistema3 = """
        Quem criou o Linux foi o Linus Torvalds
        """
        maquina.say(sistema3)
        maquina.runAndWait()
    elif '' in comando:
        silencio = 'Você pode fazer outra pergunta?'
        maquina.say('Eu não entendi ' + silencio)
        maquina.runAndWait()    
    elif 'refrigerante' in comando:
        
        apresente = """Sejam todos bem vindos!
        Vou apresentar a história do Programa Profissão 4.0"""
        site = 'https://www.youtube.com/watch?v=bR3SrexuyBM&t=18s'
        maquina.say(apresente, site)
        maquina.runAndWait()
comando_voz_usuario()
