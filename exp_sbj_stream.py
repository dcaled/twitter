"""
Example program for the Stream API. This prints public status messages
from the "sample" stream as fast as possible. Use -h for help.
"""

from __future__ import print_function

import argparse

from twitter.stream import TwitterStream, Timeout, HeartbeatTimeout, Hangup
from twitter.oauth import OAuth
from twitter.util import printNicely

from time import gmtime, strftime
import codecs

def parse_arguments():

    parser = argparse.ArgumentParser(description=__doc__ or "")

    #parser.add_argument('-t',  '--token', required=True,
    #                    help='The Twitter Access Token.')
    #parser.add_argument('-ts', '--token-secret', required=True,
    #                    help='The Twitter Access Token Secret.')
    #parser.add_argument('-ck', '--consumer-key', required=True,
    #                    help='The Twitter Consumer Key.')
    #parser.add_argument('-cs', '--consumer-secret', required=True,
    #                    help='The Twitter Consumer Secret.')
    parser.add_argument('-us', '--user-stream', action='store_true',
                        help='Connect to the user stream endpoint.')
    parser.add_argument('-ss', '--site-stream', action='store_true',
                        help='Connect to the site stream endpoint.')
    parser.add_argument('-to', '--timeout',
                        help='Timeout for the stream (seconds).')
    parser.add_argument('-ht', '--heartbeat-timeout',
                        help='Set heartbeat timeout.', default=90)
    parser.add_argument('-nb', '--no-block', action='store_true',
                        help='Set stream to non-blocking.')
    #parser.add_argument('-tt', '--track-keywords',
    #                    help='Search the stream for specific text.')
    
    return parser.parse_args()

def save(time, tweet):
    # Output directory
    out_dir = 'C:/Users/revy/Desktop/temp/'
    
    # Save
    f = codecs.open(out_dir + "tweet_"+time+".txt","a","utf-8")
    f.write(tweet)
    f.close()

def main():
    args = parse_arguments()
    args.track_keywords = 'temer'
    time = strftime("%Y%m%d_%H%M%S",gmtime())

    # When using twitter stream you must authorize.
    # auth = OAuth(args.token, args.token_secret,
    #             args.consumer_key, args.consumer_secret)
    auth=OAuth(
        "", # OAUTH_TOKEN
        "", # OAUTH_SECRET,
        "", # CONSUMER_KEY,
        "" # CONSUMER_SECRET
        )

    # These arguments are optional:
    stream_args = dict(
        timeout=args.timeout,
        block=not args.no_block,
        heartbeat_timeout=args.heartbeat_timeout)

    query_args = dict()
    if args.track_keywords:
        query_args['track'] = args.track_keywords

    if args.user_stream:
        stream = TwitterStream(auth=auth, domain='userstream.twitter.com',
                               **stream_args)
        tweet_iter = stream.user(**query_args)
    elif args.site_stream:
        stream = TwitterStream(auth=auth, domain='sitestream.twitter.com',
                               **stream_args)
        tweet_iter = stream.site(**query_args)
    else:
        stream = TwitterStream(auth=auth, **stream_args)
        if args.track_keywords:
            tweet_iter = stream.statuses.filter(**query_args)
        else:
            tweet_iter = stream.statuses.sample()

    # Iterate over the sample stream.
    for tweet in tweet_iter:
        # You must test that your tweet has text. It might be a delete
        # or data message.
        if tweet is None:
            printNicely("-- None --")
        elif tweet is Timeout:
            printNicely("-- Timeout --")
        elif tweet is HeartbeatTimeout:
            printNicely("-- Heartbeat Timeout --")
        elif tweet is Hangup:
            printNicely("-- Hangup --")
        elif tweet.get('text'):
            t_data = 'id: ' + str(tweet['id'])
            t_data += '\ndate: ' + tweet['created_at']
            t_data += '\ntext: ' + tweet['text'] + '\n'
            save(time, t_data)

            print(tweet['id'])
            printNicely(tweet['created_at'])
            printNicely(tweet['text'])
            print('\n')
        else:
            printNicely("-- Some data: " + str(tweet))

    
if __name__ == '__main__':
    main()
