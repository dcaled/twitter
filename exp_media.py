#!/usr/bin/python

# User timeline daily crawler

from twitter import *
from twitter.util import printNicely

import codecs
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

def save(out_path, filename, tweet):
    # Save
    f = codecs.open(out_path + filename+'.txt','a','utf-8')
    f.write(tweet)
    f.close()
    
# Load config
config = {}
exec(compile(open('config.py', 'rb').read(), 'config.py', 'exec'), config)

def main():
    # Create twitter API object
    twitter = Twitter(auth = OAuth(
        config['access_key'],
        config['access_secret'],
        config['consumer_key'],
        config['consumer_secret']))                  

    # Set output directory
    out_path = config['out_path']

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
        results = twitter.statuses.user_timeline(screen_name = user, count=150)


        # Loop through each status item, and print its content.
        t = 0
        for status in results:
            if not status['text'].startswith('RT') and status['created_at'][:10] == time:
                t+=1
                t_data = str(status['id']) + '\t'
                t_data += status['created_at'] + '\t'
                t_data += status['text'].replace('\t', ' ').replace('\n', ' ') + '\n'
                save(
                    out_path,
                    user.lower() + '_' + yesterday.strftime('%Y_%m_%d'),
                    t_data)

                # print(str(t) + '. (%s) %s' % (status['created_at'], status['text'].encode('ascii', 'ignore')))
                print(status['id'])
                printNicely(status['created_at'])
                printNicely(status['text'])
                print('\n')

if __name__ == '__main__':
    main()
