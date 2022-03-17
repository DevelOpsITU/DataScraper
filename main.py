from scraper import scraper
from prometheus_client import start_http_server, Gauge
import time
import datetime
import os

PORT = os.environ.get('PORT')
if (PORT == None):
    PORT = 8080
INTERVAL = int(os.environ.get('INTERVAL'))
if (INTERVAL == None):
    INTERVAL = 5

if __name__ == '__main__':
    print('Starting server on port: ' + str(PORT))
    print('Scrapeing data every: ' + str((60 * INTERVAL)) + "s")
    start_http_server(PORT)

    latest = Gauge('latest', 'Latest value from the simulator')
    connectionError = Gauge('group_d_connection_error', 'Current ConnectionError value from the simulator')
    follow = Gauge('group_d_follow', 'Current Follow error value from the simulator')
    tweet = Gauge('group_d_tweet', 'Current Tweet error value from the simulator')
    unfollow = Gauge('group_d_unfollow', 'Current Unfollow error value from the simulator')
    readTimeout = Gauge('group_d_readTimeout', 'Current ReadTimeout error value from the simulator')
    register = Gauge('group_d_register', 'Current Register error value from the simulator')

    while True:
        data = scraper.getData()
        print(str(datetime.datetime.utcnow().isoformat()) + ' => ' + str(data))
        latest.set(data['latest'])
        connectionError.set(data['ConnectionError'])
        follow.set(data['follow'])
        tweet.set(data['tweet'])
        unfollow.set(data['unfollow'])
        readTimeout.set(data['ReadTimeout'])
        register.set(data['register'])

        time.sleep(60 * INTERVAL)
