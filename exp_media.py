#!/usr/bin/python

# User timeline daily crawler

from twitter import *
from time import gmtime, strftime
from datetime import datetime, timedelta

# Run this script at gmt 00:00:00

profiles_list = [
    'oglobopolitica', # Cobertura política feita pela equipe do jornal O Globo
    'folha', # Perfil oficial do jornal Folha de S.Paulo
    'Estadao', # A versão on-line do jornal O Estado de S.Paulo.
    'EstadaoPolitica', #Twitter oficial da editoria de Política do Estadão
    'zerohora', # Jornal do Rio Grande do Sul. Notícias, esportes, política, economia, variedades, trânsito, colunistas e mais. 
    'folha_poder', # Canal de diálogo com o leitor da editoria Poder do jornal Folha de S.Paulo
    'g1politica', # As notícias sobre política no G1
    # Revistas de Esquerda
    'cartamaior', 'cartacapital',
    # Revistas de Direita
    'RevistaISTOE', 'VEJA', 'RevistaEpoca'
    ]

# Load config
config = {}
#execfile('config.py', config)

# Create twitter API object
twitter = Twitter(auth = OAuth(
    '', # OAUTH_TOKEN
    '', # OAUTH_SECRET,
    '', # CONSUMER_KEY,
    '' # CONSUMER_SECRET
    ))
                

# Date
yesterday = datetime.utcnow() - timedelta(days=1)
time=yesterday.strftime('%a %b %d')
print(time)

# Query
for user in profiles_list:

    print('------------------------------------------')
    print(user)
    print('------------------------------------------')
        
    # Query the user timeline.
    # twitter API docs:
    # https://dev.twitter.com/rest/reference/get/statuses/user_timeline
    results = twitter.statuses.user_timeline(screen_name = user, count=50)


    # Loop through each status item, and print its content.
    t = 0
    for status in results:
        if not status['text'].startswith('RT') and status['created_at'][:10] == time:
            t+=1
            print(str(t) + '. (%s) %s' % (status['created_at'], status['text'].encode('ascii', 'ignore')))
